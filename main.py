#===========================================================================
# Cache redirecting to _temp folder
import sys; sys.pycache_prefix = "_temp/cache"
#----------------------------------
# Logging system
import core.file_system.log_manag as lg; lg.run(); lg.run_path()
import logging; logging.debug(lg.run_text())
#===========================================================================
from core.utils import temp_remover, scx; temp_remover()
from core.file_system.repo_manag import logs_deleting, folder_init
folder_init()
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
#gui.menu.start() #deprecated terminal version (pre-alpha 1/2)

try:
    main_circle()
except Exception:
    log.critical("Main chain stopped. Printing the issue.", exc_info=True)
finally:
    logs_deleting(scx("lglm"))