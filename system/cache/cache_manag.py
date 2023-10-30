from core.decorators import Deprecated
import shutil, os

@Deprecated("core.file_system.repo_manag.deleter()")
def file_deleting (pathage):
  try: shutil.rmtree(pathage)
  except NotADirectoryError: os.remove(pathage)
  except FileNotFoundError: pass

#old function to regular deleting of cache if redirect is not turned on
def cache_deleting():
  file_deleting ("stats/__pycache__")
  file_deleting ("utils2/__pycache__")
  file_deleting ("gui/__pycache__")
  file_deleting ("saves/__pycache__")
  file_deleting ("system/__pycache__")
  #deeper cache deleting
  file_deleting ("system/save_system/__pycache__")

#redirecting
def cache_redirect():
  import sys
  sys.pycache_prefix = "system/cache"

#if redirect gets switched off, this can be used to clear out cache stored in sys/cache
def cache_brutedel():
  file_deleting ("system/cache/__pycache__")
  file_deleting ("system/cache/home")
  file_deleting ("system/cache/usr")
  file_deleting ("system/cache/Ministerstwo Kalibracyjne")
  file_deleting ("system/cache/Users")

@Deprecated("core.file_system.repo_manag.folder_init")
def folder_init():
  # Creates necessary folders for .gitignore elements
  import os; from core.utils import gpath
  folders = [
    f"{gpath}/core/logs", f"{gpath}/saves"
  ]
  for i in folders:
    if not os.path.isdir(i): os.makedirs(i)