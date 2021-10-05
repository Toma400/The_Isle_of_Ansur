#just trash stuff that i want to keep here for now, just for reference purposes

print (stats.races.race_saphtri.descript)
temp_stat = 5 + stats.races.race_saphtri.atr_endurance
print ("Endurance with penalty: " + str(temp_stat))

      print ('''✺--------------------------------------------------------------✺
| Λ Λ Λ Λ Λ Λ                      )                           |
| Λ           ░░░░░░░░░░░░░░░░    (         ~~~                |
|Λ  ░░░░░░░░░░░░░░░░░░░  ♖-------♖ )                           |
| Λ ░░░░░░░░░░░░░░░░░░░  |  Baedoor ♖)           ~~~           |
|Λ  ░░░░░░░░░░░░░░░░░░░  ♖-------♖⚓)                          |
|Λ  ۩  ░░░░░░░░░░░░░░░░           (         ~~~        ✖       |
| Λ Λ Λ Λ Λ Λ Λ   Λ ░░░░░░░░░░░░░  )                           |
✺--------------------------------------------------------------✺''')

default_stats = {}

#everything above is total bullshit, it's just for conceptualisation purposes

#SHORTCUT FOR RID MANAGEMENT (OUTPUT: VALUE_NAME -> VALUE)
import system.id_manag
for i in system.id_manag.rid_conv("ansur:baedoorian", 0, True):
  print (i + "-> " + str(system.id_manag.rid_conv("ansur:baedoorian", i)))

#POSSIBLE COMPATIBILITY THINGIES:
#character additional_abilities/additional_attributes list can be made into .json and read from there = can be expanded by mods with additional attributes or abilities
#in character.py it will just be loaded to fit their lists used in character creation

#BOOLEAN TRUE IS SET AS =1 IN STATS

#BLACKSMITH/CLASSES/RACES BEING WEIRDLY USING THEIR STATS (NOT REALLY CORRECT)