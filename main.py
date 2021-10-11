import system.cache.cache_manag
system.cache.cache_manag.cache_redirect()
import gui.menu

#gui.menu.start()

#import gui.character
#gui.character.race("Wuwuzela")

import gui.inventory
import system.json_manag
#gui.inventory.add_item("Terti", "ansur:ayer_knife")
print (gui.inventory.inv_key_manager ("Terti", "ansur:ayer_knife", "quality", "value"))
print (gui.inventory.inv_key_manager ("Terti", "ansur:ayer_knife", "quality", "item_amount"))
gui.inventory.add_item ("Terti", "ansur:bread", 5)