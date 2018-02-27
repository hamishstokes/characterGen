import coreXMLParser

class character:
	def __init__(self, statsInput, levelInput, raceInput, subraceInput, classesInput):
		# Stores stats 0-total 1-base 2-racial bonuses
		self.stats = {
			'Strength': [0, statsInput['Strength'], 0],
			'Dexterity': [0, statsInput['Dexterity'], 0],
			'Constitution': [0, statsInput['Constitution'], 0],
			'Intelligence': [0, statsInput['Intelligence'], 0],
			'Wisdom': [0, statsInput['Wisdom'], 0],
			'Charisma': [0, statsInput['Charisma'], 0]
		}
		self.statBonus = [{}, statsInput['Select']]
		self.level = levelInput
		self.race = raceInput
		self.subrace = subraceInput
		self.classes = classesInput
		#Store skill values 0-total 1-governing stat 2-proficient 3-other bonus 4-placeholder
		self.raceProficiencies = coreXMLParser.parseRaceProficiencies(self.race,self.subrace)
		self.skills = {
			'Acrobatics': [0, 'Dexterity', False, 0, 0],
			'Animal Handling': [0, 'Wisdom', False, 0, 0],
			'Arcana': [0, 'Intelligence', False, 0, 0],
			'Athletics': [0, 'Strength', False, 0, 0],
			'Deception': [0, 'Charisma', False, 0, 0],
			'History': [0, 'Intelligence', False, 0, 0],
			'Insight': [0, 'Wisdom', False, 0, 0],
			'Intimidation': [0, 'Charisma', False, 0, 0],
			'Investigation': [0, 'Intelligence', False, 0, 0],
			'Medicine': [0, 'Wisdom', False, 0, 0],
			'Nature': [0, 'Intelligence', False, 0, 0],
			'Perception': [0, 'Wisdom', False, 0, 0],
			'Performance': [0, 'Charisma', False, 0, 0],
			'Persuasion': [0, 'Charisma', False, 0, 0],
			'Religion': [0, 'Intelligence', False, 0, 0],
			'Sleight of Hand': [0, 'Dexterity', False, 0, 0],
			'Stealth': [0, 'Dexterity', False, 0, 0],
			'Survival': [0, 'Wisdom', False, 0, 0],
			'Strength': [0, 'Strength', False, 0, 0],
			'Dexterity': [0, 'Dexterity', False, 0, 0],
			'Constitution': [0, 'Constitution', False, 0, 0],
			'Intelligence': [0, 'Intelligence', False, 0, 0],
			'Wisdom': [0, 'Wisdom', False, 0, 0],
			'Charisma': [0, 'Charisma', False, 0, 0]
		}
		self.size = coreXMLParser.parseRaceSize(self.race)
		self.walkSpeed = coreXMLParser.parseRaceWalkSpeed(self.race, self.subrace)
		self.languages = coreXMLParser.parseRaceLanguages(self.race, self.subrace)
		self.raceTraits = coreXMLParser.parseRaceTraits(self.race, self.subrace)

		# Set-up methods
		self.updateRaceProfs(True)

	def __repr__(self):
		return "Race: {}\nSubrace: {}\nLevel: {}\n\nWalk Speed: {}\n\nSize: {}\n\nLanguages: {}\n\nStats\n-----\nStrength: {}\nDexterity: {}\nConstitution: {}\nIntelligence: {}\nWisdom: {}\nCharisma: {}\n\nSaves\n-----\nStrength: {}\nDexterity: {}\nConstitution: {}\nIntelligence: {}\nWisdom: {}\nCharisma: {}\n\nSkills\n-----\nAcrobatics: {}\nAnimal Handling: {}\nArcana: {}\nAthletics: {}\nDeception: {}\nHistory: {}\nInsight: {}\nIntimidation: {}\nInvestigation: {}\nMedicine: {}\nNature: {}\nPerception: {}\nPerformance: {}\nPersuasion: {}\nReligion: {}\nSleight of Hand: {}\nStealth: {}\nSurvival: {}\n".format(self.race, self.subrace, self.level,self.walkSpeed,self.size,self.languages,self.stats["Strength"],self.stats["Dexterity"],self.stats["Constitution"],self.stats["Intelligence"],self.stats["Wisdom"],self.stats["Charisma"],self.skills["Strength"],self.skills["Dexterity"],self.skills["Constitution"],self.skills["Intelligence"],self.skills["Wisdom"],self.skills["Charisma"],self.skills['Acrobatics'],self.skills['Animal Handling'],self.skills['Arcana'],self.skills['Athletics'],self.skills['Deception'],self.skills['History'],self.skills['Insight'],self.skills['Intimidation'],self.skills['Investigation'],self.skills['Medicine'],self.skills['Nature'],self.skills['Perception'],self.skills['Performance'],self.skills['Persuasion'],self.skills['Religion'],self.skills['Sleight of Hand'],self.skills['Stealth'],self.skills['Survival'])

	#Take input stats and inserts them into stats dictionary then recalculates
	def updateBaseStats(self, newStats):
		for stat in newStats:
			self.stats[stat][1] = newStats[stat]
		self.updateStats()

	#This method should process the results of a race selection
	def raceSelectUpdate(self):
		self.parseRaceStats()
		self.parseRaceSize()
		self.parseRaceSpeed()
		self.parseRaceLanguages()
		self.parseRaceProficiencies()

	#Gets stat bonuses from XML and stores in stats dictionary in index 2
	def parseRaceStats(self):
		for stat in self.stats:
			self.stats[stat][2] = 0
		self.raceStatBonuses = coreXMLParser.parseRaceStats(self.race, self.subrace)
		for stat in self.raceStatBonuses:
			if stat != 'Select':
				self.stats[stat][2] = self.raceStatBonuses[stat]
			else:
				self.statBonus[1] = self.raceStatBonuses[stat]
		self.updateStats()
	def parseRaceSize(self):
		self.size = coreXMLParser.parseRaceSize(self.race)
	def parseRaceLanguages(self):
		self.languages = coreXMLParser.parseRaceLanguages(self.race, self.subrace)
	def parseRaceSpeed(self):
		self.walkSpeed = coreXMLParser.parseRaceWalkSpeed(self.race, self.subrace)
	def parseRaceProficiencies(self):
		self.updateRaceProfs(False)
		self.raceProficiencies = coreXMLParser.parseRaceProficiencies(self.race, self.subrace)


	#Calculates total stat value - base + racial
	#TODO: Add user select and feat bonuses - percolate changes to dependencies
	def updateStats(self):
		for stat in self.stats:
			self.stats[stat][0] = self.stats[stat][1] + self.stats[stat][2]
		self.updateSkills()

	#updates skills and saves after stat changes
	def updateSkills(self):
		for skill in self.skills:
			self.updateSkill(skill)
	#updates prof from Race
	def updateRaceProfs(self, toggleProf):
		for skill in self.raceProficiencies:
			self.updateSkillProf(skill, True)

	#updates specified skill
	#TODO: utilise where efficient
	def updateSkill(self, skillName):
		skillValue = self.getStatMod(self.skills[skillName][1])
		#add proficiency bonus if applicable
		if self.skills[skillName][2]:
			skillValue = skillValue + self.getProficiencyBonus()
		#add misc skill bonus
		if self.skills[skillName][3] != 0:
			skillValue = skillValue + self.skills[skillName][3]
		#apply value to variable
		self.skills[skillName][0] = skillValue

	def updateSkillProf(self, skillName, toggleProf):
		self.skills[skillName][2] = toggleProf
		self.updateSkill(skillName)

	def addSkillBonus(self, skillName, bonusValue):
		self.skills[skillName][3] = bonusValue
		self.updateSkill(skillName)

	

	#utilities
	def getStat(self, statName):
		return self.stats[statName][0]
	def getProficiencyBonus(self):
		return (7 + self.level) // 4
	def calculateModifier(self, statValue):
		return (statValue - 10)//2
	def getStatMod(self, statName):
		return self.calculateModifier(self.getStat(statName))