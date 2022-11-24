import os; fpath = os.path.dirname(os.path.abspath("build.py"))
from distutils.dir_util import copy_tree
import PyInstaller.__main__
import PyInstaller
import traceback
import shutil

def delete (pathage):
  try:                       shutil.rmtree(pathage)
  except NotADirectoryError: os.remove(pathage)
  except FileNotFoundError:  pass

class DefaultRun:
  # ----------------------------------------------------------------------
  # CONFIGURATION OF BUILD
  # Adjust values here to make build customised more to your needs
  # ----------------------------------------------------------------------
  # directory of the game
  core_path = f"{fpath}/"
  game_name = "Baedoor Creation Set"
  icon_path = core_path + "bcs/assets/graphical/bcs.ico"
  # directory for outcome
  export_path = "D:/Ministerstwo Kalibracyjne/PyCharm_Projects/[builds]/"
  full_export_path = export_path + "Isle of Ansur" + "/"
  # ----------------------------------------------------------------------
  # REFERENCE DOCS
  # https://github.com/pyinstaller/pyinstaller/blob/v4.5.1/doc/usage.rst
  # ----------------------------------------------------------------------
  forge_builder = [
    core_path + "bcset.py",
    "--onedir",
    "--onefile",
    "--noupx",
    # if you are going to change this, please redirect upx to net source (requests library?) or import files if license allows you to do so
    "--clean",
    "--name=" + game_name,
    "--icon=" + icon_path,
    "--distpath=" + full_export_path,
    "--workpath=" + core_path + "system/cache/pyinstaller",
    "--specpath=" + core_path + "system/cache/pyinstaller"
  ]
  ommitted_elements = [  # list of files that are deleted after finishing the build
    full_export_path + ".idea",
    full_export_path + "__pycache__",
    full_export_path + ".breakpoints",
    full_export_path + ".gitignore",
    full_export_path + "test.py",
    # caches
    full_export_path + "bcs/__pycache__",
    full_export_path + "system",
    core_path + "system"
  ]

# function used to delete elements excluded in list above
def file_deleting(delete_list):
  j = 0
  for i in delete_list:
    delete(delete_list[j])
    j += 1

def cache_clearing():
  delete("system/cache/Ministerstwo Kalibracyjne")
  delete("system/cache/Users")
  delete("system/cache/pyinstaller/Isle of Ansur")

# main function for running builder
def forge():
  issues = 0
  try:
    PyInstaller.__main__.run(
      DefaultRun.forge_builder
    )
    copy_tree(DefaultRun.core_path, DefaultRun.full_export_path)  # copies all files over
    file_deleting(DefaultRun.ommitted_elements)  # deletes files excluded in list
  except:
    issues += 1
    traceback.print_exc()
  return issues

print(f"----------------- Baedoor Creation Set -----------------")
print(f"| BCS build is starting to run...")
breaks = forge()
#cache_clearing()
print(f"| BCS build is complete, with {breaks} errors!")
if breaks > 0:
  temp = input(f"| Click anything to end the program.")