import system.cache.cache_manag
system.cache.cache_manag.cache_redirect()
import gui.menu

gui.menu.start()

#import gui.character
#gui.character.race("Wuwuzela")

import system.int_systems.inv_manag
import system.json_manag
#system.int_systems.inv_manag.del_item ("Terti", "ansur:honey_roll", 2)
#system.int_systems.inv_manag.add_item ("Terti", "ansur:flour")
#system.int_systems.inv_manag.iid_checker("Terti", "ansur:short_sword")

#INV TESTING
#import gui.inventory
#gui.inventory.main_inv("Terti")

#FOR THE FUTURE!!!!
#Write here what was the last thing you worked on. What was the issues you found tiring
#Like "WORKED ON X, BUT Y DEMOTIVATED ME"
#--------------------V------------------
#
# Inventory managment iirc, it might be single-stack items Being difficult to manage
# Slot selecting too btw
# ^ slot selecting could be used by binding 'j' from iterator to specific item
# or just using some sort of "find line X of json file", which would also work*
# * - just remember that it starts from line 3
#
# So if player would choose item "1", it would redirect them for 3rd line
# If player choose "5"th item, it will redirect them to 7th line
#---------------------------------------