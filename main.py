import gui.menu
import stats.races

gui.menu.start()

#cache deletin
import utils.cache_manag
utils.cache_manag.cache_deleting ()
del stats.races
del gui.menu