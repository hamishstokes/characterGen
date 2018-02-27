import coreXMLParser
from characterClass import character


print("Test 1\n=======")
test1 = character({'Strength':12, 'Dexterity':10, 'Constitution':10, 'Intelligence':10, 'Wisdom':10, 'Charisma':10, 'Select':0}, 1, 'Elf', 'High Elf', ['Rogue',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
test1.parseRaceStats()
test1.updateSkills()
test1.parseRaceSize()
print(test1)

print("\n\nTest 2\n=======")
test2 = character({'Strength':12, 'Dexterity':12, 'Constitution':12, 'Intelligence':12, 'Wisdom':12, 'Charisma':12, 'Select':0}, 4, 'Human', 'Human Variant', ['Ranger',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
test2.parseRaceStats()
test2.updateSkills()
print(test2)

print("\n\nTest 3\n=======")
test3 = character({'Strength':8, 'Dexterity':8, 'Constitution':8, 'Intelligence':8, 'Wisdom':8, 'Charisma':8, 'Select':0}, 8, 'Goliath', 'Goliath', ['Ranger',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
test3.parseRaceStats()
test3.updateSkills()
print(test3)


print("\n\nTest 4\n=======")
test4 = character({'Strength':8, 'Dexterity':8, 'Constitution':8, 'Intelligence':8, 'Wisdom':8, 'Charisma':8, 'Select':0}, 8, 'Elf', 'Wood Elf', ['Ranger',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
test4.parseRaceStats()
test4.updateSkills()
print(test4)
test4.race = "Gnome"
test4.subrace = "Deep Gnome"
test4.raceSelectUpdate()
print(test4)
# print("\n\nTest 4\n=======")
# core.core({'Strength':11, 'Dexterity':11, 'Constitution':11, 'Intelligence':11, 'Wisdom':11, 'Charisma':11, 'Select':0}, 11, 'Tiefling', 'Infernal Tiefling', ['Ranger',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


# print("\n\nTest 5\n=======")
# core.core({'Strength':20, 'Dexterity':20, 'Constitution':20, 'Intelligence':20, 'Wisdom':20, 'Charisma':20, 'Select':0}, 16, 'Triton', 'Triton', ['Ranger',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


# print("\n\nTest 6\n=======")
# core.core({'Strength':8, 'Dexterity':12, 'Constitution':8, 'Intelligence':12, 'Wisdom':8, 'Charisma':12, 'Select':0}, 3, 'Human', 'Human Variant', ['Ranger',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


# print("\n\nTest 7\n=======")
# core.core({'Strength':8, 'Dexterity':12, 'Constitution':8, 'Intelligence':12, 'Wisdom':8, 'Charisma':12, 'Select':0}, 20, 'Human', 'Human Standard', ['Ranger',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


# print("\n\nTest 8\n=======")
# core.core({'Strength':8, 'Dexterity':12, 'Constitution':8, 'Intelligence':12, 'Wisdom':8, 'Charisma':12, 'Select':0}, 8, 'Half-Elf', 'Half-Elf (Weapon Training)', ['Ranger',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])