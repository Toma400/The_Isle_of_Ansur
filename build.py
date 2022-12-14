#-----------------------------------------------------------
# BUILD
# Module used to build .exe file from current files using
# pyInstaller. All needed documentation is written here
# in further comment blocks.
#-----------------------------------------------------------
import sys; sys.pycache_prefix = "_temp/cache"

import PyInstaller.__main__
import PyInstaller
import os; fpath = os.path.dirname(os.path.abspath("build.py"))
from core.file_system.repo_manag import file_lister
from distutils.dir_util import copy_tree
import stat, shutil, traceback
#-----------------------------------------------------------
# FORGE
# Function used to execute pyInstaller commands precised
# later in module
# References DefaultRun class as configurator for all
# options (when changing devices, change directories paths)
#-----------------------------------------------------------
class DefaultRun:
    # ----------------------------------------------------------------------
    # CONFIGURATION OF BUILD
    # Adjust values here to make build customised more to your needs
    # ----------------------------------------------------------------------
    # directory of the game
    core_path = f"{fpath}/"
    game_name = "Isle of Ansur"
    icon_path = core_path + "ioa.ico"
    # directory for outcome
    export_path = "D:/Ministerstwo Kalibracyjne/PyCharm_Projects/[builds]/"
    full_export_path = export_path + game_name + "/"
    # ----------------------------------------------------------------------
    # REFERENCE DOCS
    # https://github.com/pyinstaller/pyinstaller/blob/v4.5.1/doc/usage.rst
    # ----------------------------------------------------------------------
    forge_builder = [
        core_path + "main.py",
        "--onedir",
        "--onefile",
        "--noupx",  # if you are going to change this, please redirect upx to net source (requests library?) or import files if license allows you to do so
        "--clean",
        "--name=" + game_name,
        "--icon=" + icon_path,
        "--distpath=" + export_path + game_name + "/",
        "--workpath=" + core_path + "system/cache/pyinstaller",
        "--specpath=" + core_path + "system/cache/pyinstaller"
    ]
    ommitted_elements = [  # list of files that are deleted after finishing the build
        full_export_path + ".git",
        full_export_path + ".idea",
        full_export_path + ".breakpoints",
        full_export_path + ".gitignore",
        full_export_path + "test.py",
        # caches
        full_export_path + "_temp",
        full_export_path + "__pycache__",
        full_export_path + "gui/__pycache__",
        full_export_path + "system/__pycache__",
        full_export_path + "utils/__pycache__",
        full_export_path + "system/core/__pycache__",
        full_export_path + "system/cache/__pycache__",
        full_export_path + "system/cache/pyinstaller"
    ]

# function used to delete elements excluded in list above
def file_deleting(delete_list):
    def on_rm_error(func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        os.unlink(path)

    for i in delete_list:
        try:
            shutil.rmtree(i, onerror=on_rm_error)
        except FileNotFoundError: pass

    for l in file_lister(f"{DefaultRun.full_export_path}core/logs/"):
        os.remove(f"{DefaultRun.full_export_path}core/logs/{l}")

# main function for running builder
def forge():
    PyInstaller.__main__.run(
        DefaultRun.forge_builder
    )
    copy_tree(DefaultRun.core_path, DefaultRun.full_export_path) # copies all files over
    file_deleting(DefaultRun.ommitted_elements)                  # deletes files excluded in list

#================================================================================================================
print('{:^65}'.format("\33[35m    ------------------------------"))
print('{:^65}'.format(" ISLE OF ANSUR BUILD CONSTRUCTOR "))
print("\n")
print('{:^65}'.format("----------------------------"))
print('{:^65}'.format("------------------------------------------------------------------------- \033[0m"))
try:
    forge()
    print('{:^75}'.format("\033[92m Build successful \033[0m"))
except:
    traceback.print_exc()