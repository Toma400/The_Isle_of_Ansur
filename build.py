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
from core.file_system.repo_manag import file_lister, dir_lister
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
        full_export_path + "modding_guide.odt",
        # folders not used anymore
        full_export_path + "docs",
        full_export_path + "gui",
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

    # removes logs
    for l in file_lister(f"{DefaultRun.full_export_path}core/logs/"):
        try:
            shutil.rmtree(f"{DefaultRun.full_export_path}core/logs/{l}", onerror=on_rm_error)
        except: pass
    # removes saves
    for s in file_lister(f"{DefaultRun.full_export_path}saves/"):
        try:
            shutil.rmtree(f"{DefaultRun.full_export_path}saves/{s}", onerror=on_rm_error)
        except: pass
    # removes scripts that are not vanilla
    for scr in file_lister(f"{DefaultRun.full_export_path}scripts/"):
        if scr != "example_script.py":
            try:
                shutil.rmtree(f"{DefaultRun.full_export_path}scripts/{scr}", onerror=on_rm_error)
            except: pass
    # removes mods that are not vanilla:
    # statpacks
    for stp in dir_lister(f"{DefaultRun.full_export_path}stats/"):
        if stp != "ansur":
            try:
                shutil.rmtree(f"{DefaultRun.full_export_path}stats/{stp}", onerror=on_rm_error)
            except: pass
    for stp in file_lister(f"{DefaultRun.full_export_path}stats/"):
        try:
            shutil.rmtree(f"{DefaultRun.full_export_path}stats/{stp}", onerror=on_rm_error)
        except: pass
    # worldpacks
    for wdp in dir_lister(f"{DefaultRun.full_export_path}worlds/"):
        if wdp != "ansur":
            try:
                shutil.rmtree(f"{DefaultRun.full_export_path}worlds/{wdp}", onerror=on_rm_error)
            except: pass
    for wdp in file_lister(f"{DefaultRun.full_export_path}worlds/"):
        try:
            shutil.rmtree(f"{DefaultRun.full_export_path}worlds/{wdp}", onerror=on_rm_error)
        except: pass
    for sv in dir_lister(f"{DefaultRun.full_export_path}saves/"):
        try:
            shutil.rmtree(f"{DefaultRun.full_export_path}saves/{sv}", onerror=on_rm_error)
        except: pass

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