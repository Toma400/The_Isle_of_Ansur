from core.decorators import Deprecated

#old function to regular deleting of cache if redirect is not turned on
def cache_deleting():
  import utils.repo_manag
  utils.repo_manag.file_deleting ("stats/__pycache__")
  utils.repo_manag.file_deleting ("utils2/__pycache__")
  utils.repo_manag.file_deleting ("gui/__pycache__")
  utils.repo_manag.file_deleting ("saves/__pycache__")
  utils.repo_manag.file_deleting ("system/__pycache__")
  #deeper cache deleting
  utils.repo_manag.file_deleting ("system/save_system/__pycache__")
  del utils.repo_manag

#redirecting
def cache_redirect():
  import sys
  sys.pycache_prefix = "system/cache"

#if redirect gets switched off, this can be used to clear out cache stored in sys/cache
def cache_brutedel():
  import utils.repo_manag
  utils.repo_manag.file_deleting ("system/cache/__pycache__")
  utils.repo_manag.file_deleting ("system/cache/home")
  utils.repo_manag.file_deleting ("system/cache/usr")
  utils.repo_manag.file_deleting ("system/cache/Ministerstwo Kalibracyjne")
  utils.repo_manag.file_deleting ("system/cache/Users")

@Deprecated("core.file_system.repo_manag.folder_init")
def folder_init():
  # Creates necessary folders for .gitignore elements
  import os; from core.utils import gpath
  folders = [
    f"{gpath}/core/logs", f"{gpath}/saves"
  ]
  for i in folders:
    if not os.path.isdir(i): os.makedirs(i)