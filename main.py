import menu
import stats.races

def cache_deleting (pathage):
  import os
  import shutil
  try:
    shutil.rmtree(pathage)
  except NotADirectoryError:
    os.remove(pathage)
  except FileNotFoundError:
    pass
  del shutil

menu.start()
print (stats.races.race_saphtri.descript)
temp_stat = 5 + stats.races.race_saphtri.atr_endurance
print ("Endurance with penalty: " + str(temp_stat))

#cache deletin
del stats.races
cache_deleting ("stats/__pycache__")
cache_deleting ("utils/__pycache__")