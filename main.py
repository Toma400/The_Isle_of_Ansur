import gui.menu
import stats.races
import utils.repo_manag

gui.menu.start()
print (stats.races.race_saphtri.descript)
temp_stat = 5 + stats.races.race_saphtri.atr_endurance
print ("Endurance with penalty: " + str(temp_stat))

#cache deletin
utils.repo_manag.cache_deleting ("stats/__pycache__")
utils.repo_manag.cache_deleting ("utils/__pycache__")
utils.repo_manag.cache_deleting ("gui/__pycache__")
utils.repo_manag.cache_deleting ("saves/__pycache__")
del stats.races
del gui.menu
del utils.repo_manag