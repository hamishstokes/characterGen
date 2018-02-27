import xml.etree.ElementTree  
xmlPath = 'xmlData.xml'

def editxml():
	lang = ['Gith','Auran','Aquan','Terran','Ignan','Common','Dwarvish','Elvish','Giant','Gnomish','Goblin','Halfling','Orc','Abyssal','Celestial','Draconic','Deep Speech','Infernal','Primordial','Sylvan','Undercommon','Druidic',"Thieves' Cant",'Aarakocra','extra language']
	tree = xml.etree.ElementTree.parse(xmlPath)
	rootNode = tree.getroot()
	xmlRaces = rootNode.find('races')
	for race in xmlRaces.findall('race'):
		for subrace in race.findall('subrace'):
			for trait in subrace.findall('trait'):
				langTrait = trait.find('name').text
				givenLangs = []
				if langTrait == "Languages":
					for texts in trait.findall('text'):
						for language in lang:
							if language in texts.text:
								givenLangs.append(language)
				if len(givenLangs) != 0:
					print('languages',', '.join(givenLangs))
	tree.write('xmlData.xml')
	# 	raceName = race.find('name').text
	# 	race.set('name', raceName)
	# tree.write('out.xml')


		# for race in xmlRaces.findall('race'):
		# for subrace in race.findall('subrace'):
		# 	for trait in subrace.findall('trait'):
		# 		langTrait = trait.find('name').text
		# 		if langTrait == "Languages":
		# 			trait.set('type', 'Languages')
editxml()