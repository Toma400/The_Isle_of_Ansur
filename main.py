import gui.menu
import stats.races

gui.menu.start()

#cache deletin
import utils.repo_manag
utils.repo_manag.cache_deleting ("stats/__pycache__")
utils.repo_manag.cache_deleting ("utils/__pycache__")
utils.repo_manag.cache_deleting ("gui/__pycache__")
utils.repo_manag.cache_deleting ("saves/__pycache__")
del stats.races
del gui.menu
del utils.repo_manag