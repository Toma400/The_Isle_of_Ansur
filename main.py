import system.cache.cache_manag
system.cache.cache_manag.cache_redirect()
from utils.text_manag import colour_formatter as format
import gui.menu
import traceback
# import win_unicode_console
# win_unicode_console.enable() <- not useful after all

try:
    gui.menu.start()
except:
    print("---------------------------------------------------------")
    traceback.print_exc()
    print("\n")
    print("---------------------------------------------------------")
    print(format("red", "Found an error! See the message above for details"))
    print(format("yellow", "You can send message above to developer, reporting the issue"))
    print("\n")
    print(format("yellow", "Enter any key to close the game"))
    temp_var = input("")