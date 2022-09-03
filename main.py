import system.log_manag; system.log_manag.run()
from core.utils import temp_remover; temp_remover()
import system.cache.cache_manag as cmg
cmg.cache_redirect(); cmg.folder_init()
from utils.text_manag import colour_formatter as cformat
import traceback

from core.circles import *
import gui.menu

try:
    #gui.menu.start()
    main_circle()
except Exception:
    print("---------------------------------------------------------")
    log.critical("Main chain stopped. Printing the issue.", exc_info=True)
    traceback.print_exc()
    print("\n")
    print("---------------------------------------------------------")
    print(cformat("red", "Found an error! See the message above for details"))
    print(cformat("yellow", "You can send message above to developer, reporting the issue"))
    print("\n")
    print(cformat("yellow", "Enter any key to close the game"))
    temp_var = input("")