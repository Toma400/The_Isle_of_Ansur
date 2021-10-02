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

def json_change(path, element, change_type, change_value):
  if change_type == "replacement":
    #replace .json variable [element] value with [change_value]
    pass
  elif change_type == "maths":
    #do mathematic equation (.json variable value [element] + [change_value]) and write its result back
    pass
  elif change_type == "var_addition":
    #write new variable called [element] in the end of .json file with value of [change_value]
    pass

#+- how could default values be executed into the game/save 
#default_stats will have all statistics that are used by default in beginning of the game, avoiding ofc the ones that are not set by default
for i in default_stats:
  json_change(path, name_of_stats, var_addition, stats_value)