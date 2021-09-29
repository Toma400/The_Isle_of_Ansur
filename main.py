import gui.menu
import stats.races
import system.save_system

global player_name
player_name = "Shadow" 
#temporary variable, to be used by sys/save_sys
#system.save_system.folder_creating(player_name)

gui.menu.start()

#cache deletin
import utils.cache_manag
utils.cache_manag.cache_deleting ()