import system.log_manag as lg; lg.run(); lg.run_path()
import logging; logging.debug(lg.run_text())
from core.utils import temp_remover; temp_remover()
import system.cache.cache_manag as cmg
cmg.cache_redirect(); cmg.folder_init()
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