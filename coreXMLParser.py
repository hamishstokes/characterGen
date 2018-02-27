import xml.etree.ElementTree
from characterClass import character

#DATA VARIABLES
xmlPath = 'xmlData.xml'
rootNode = xml.etree.ElementTree.parse(xmlPath).getroot()
xmlClasses = rootNode.find('classes')
xmlRaces = rootNode.find('races')

abbrevMap = {'Str':'Strength', 'Dex':'Dexterity', 'Con':'Constitution', 'Int':'Intelligence', 'Wis':'Wisdom', 'Cha':'Charisma', 'Sel':'Select'}


def parseRaceStats(characterRace, characterSubrace):
	statBonuses = {}
	foundRace = xmlRaces.find("race[@name='{}']".format(characterRace))
	#Pulls stats from subrace if there is one
	if characterRace != characterSubrace:
		foundSubrace = foundRace.find("subrace[@name='{}']".format(characterSubrace))
		ability = foundSubrace.find('ability')
		if ability != None:
			abilityMod = [x.strip() for x in ability.text.split(',')]
			for pair in abilityMod:
				statMod = pair.split(' ')
				statMod[0] = abbrevMap[statMod[0]]
				statBonuses[statMod[0]] = int(statMod[1])
	#Pulls stats from race
	ability = foundRace.find('ability')
	if ability != None:
		abilityMod = [x.strip() for x in foundRace.find('ability').text.split(',')] #reads ability scores into list of pairs
		for pair in abilityMod:
			statMod = pair.split(' ')
			statMod[0] = abbrevMap[statMod[0]]
			statBonuses[statMod[0]] = int(statMod[1])
	return statBonuses

def parseRaceSize(characterRace):
	foundRace = xmlRaces.find("race[@name='{}']".format(characterRace))
	size = foundRace.find('size')
	return size.text

def parseRaceWalkSpeed(characterRace, characterSubrace):
	foundRace = xmlRaces.find("race[@name='{}']".format(characterRace))
	if foundRace.find('speed') != None:
		return foundRace.find('speed').text
	else:
		foundSubrace = foundRace.find("subrace[@name='{}']".format(characterSubrace))
		return foundSubrace.find('speed').text

def parseRaceLanguages(characterRace, characterSubrace):
	languages = []
	foundRace = xmlRaces.find("race[@name='{}']".format(characterRace))
	for trait in foundRace.findall('trait'):
		if 'type' in trait.attrib:
			if trait.attrib['type']=='Languages':
				languages = [x for x in trait.attrib['languages'].split(', ')]
	if characterRace != characterSubrace:
		foundSubrace = foundRace.find("subrace[@name='{}']".format(characterSubrace))
		for trait in foundSubrace.findall('trait'):
				if 'type' in trait.attrib:
					if trait.attrib['type']=='Languages':
						[languages.append(x) for x in trait.attrib['languages'].split(', ')]
	return languages

def parseRaceProficiencies(characterRace, characterSubrace):
	foundRace = xmlRaces.find("race[@name='{}']".format(characterRace))
	proficiencies = foundRace.find('proficiency').text
	if proficiencies != None:
		return proficiencies.split(", ")
	else:
		return []

def parseRaceTraits(characterRace, characterSubrace):
	traits = {}
	foundRace = xmlRaces.find("race[@name='{}']".format(characterRace))
	for trait in foundRace.findall('trait'):
		traits[trait.find('name').text] = [x.text for x in trait.findall('text')]
	print(traits)