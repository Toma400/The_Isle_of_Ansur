import logging as log; import system.log_manag; system.log_manag.run()
import system.cache.cache_manag
system.cache.cache_manag.cache_redirect()
from utils.text_manag import colour_formatter as format
import traceback

from core.run_test import *
import gui.menu

try:
    #gui.menu.start()
    testpyg()
except Exception:
    print("---------------------------------------------------------")
    log.critical("Main chain stopped. Printing the issue.", exc_info=True)
    traceback.print_exc()
    print("\n")
    print("---------------------------------------------------------")
    print(format("red", "Found an error! See the message above for details"))
    print(format("yellow", "You can send message above to developer, reporting the issue"))
    print("\n")
    print(format("yellow", "Enter any key to close the game"))
    temp_var = input("")