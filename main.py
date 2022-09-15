import system.log_manag as lg; lg.run(); lg.run_path()
import logging; logging.debug(lg.run_text())
from core.utils import temp_remover, scx; temp_remover()
import system.cache.cache_manag as cmg
cmg.cache_redirect(); cmg.folder_init()
from core.file_system.repo_manag import logs_deleting
logs_deleting(scx("lglm"))
import traceback
#===========================================================================
# WELCOME IN THE ISLE OF ANSUR
#-------------------------------
# This game operates on heavy modularisation of both code and file systems,
# supporting user-created content in similar way as Forge API for Minecraft,
# or Elder Scrolls modding system, from which it takes inspiration.
# While analysing the code, take in mind those principles.
#-------------------------------
# If you do not understand what specific function does, use IDE and jump
# into said function - almost all non-straightforward functions have
# comments explaining their use and caveats.
# Some of technical backgrounds are also explained in documentation (see
# 'docks/mods' folder bundled with game).
#===========================================================================

from core.circles import *
import gui.menu #deprecated terminal version (pre-alpha 1/2)

try:
    #gui.menu.start() #deprecated terminal version (pre-alpha 1/2)
    main_circle()
except Exception:
    print("---------------------------------------------------------")
    log.critical("Main chain stopped. Printing the issue.", exc_info=True)
    traceback.print_exc()
    print("\n")
    print("---------------------------------------------------------")