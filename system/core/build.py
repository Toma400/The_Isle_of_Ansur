#-----------------------------------------------------------
# BUILD
# Module used to build .exe file from current files using
# pyInstaller. All needed documentation is written here
# in further comment blocks.
#-----------------------------------------------------------

import PyInstaller.__main__
import PyInstaller
from distutils.dir_util import copy_tree
from utils.text_manag import bcolors as colour
from utils.text_manag import align as align
from utils.repo_manag import file_deleting as delete

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
    core_path = "D:/Ministerstwo Kalibracyjne/PyCharm_Projects/Isle_of_Ansur/"
    game_name = "Isle of Ansur"
    icon_path = core_path + "utils/assets/icon.ico"
    # directory for outcome
    export_path = "D:/Ministerstwo Kalibracyjne/PyCharm_Projects/builds/"
    full_export_path = export_path + game_name + "/"
    # ----------------------------------------------------------------------
    # REFERENCE DOCS
    # https://github.com/pyinstaller/pyinstaller/blob/v4.5.1/doc/usage.rst
    # ----------------------------------------------------------------------
    forge_builder = [
        core_path + "main.py",
        "--onedir",
        "--noupx",  # if you are going to change this, please redirect upx to net source (requests library?) or import files if license allows you to do so
        "--clean",
        "--name=" + game_name,
        "--icon=" + icon_path,
        "--distpath=" + export_path,
        "--workpath=" + core_path + "system/cache/pyinstaller",
        "--specpath=" + core_path + "system/cache/pyinstaller"
    ]
    ommitted_elements = [  # list of files that are deleted after finishing the build
        full_export_path + ".idea",
        full_export_path + "__pycache__",
        full_export_path + ".breakpoints",
        full_export_path + ".gitignore",
        full_export_path + "test.py"
    ]

# function used to delete elements excluded in list above
def file_deleting(delete_list):
    j = 0
    for i in delete_list:
        delete(delete_list[j])
        j += 1

# main function for running builder
def forge():
    PyInstaller.__main__.run(
        DefaultRun.forge_builder
    )
    copy_tree(DefaultRun.core_path, DefaultRun.full_export_path) # copies all files over
    file_deleting(DefaultRun.ommitted_elements) # deletes files excluded in list
    print(align(colour.CGREEN + "Build successful" + colour.ENDC, "centre_colour"))

print(align(colour.CVIOLET + "------------------------------"))
print(align(" ISLE OF ANSUR BUILD CONSTRUCTOR "))
print("\n")
print(align("----------------------------"))
print(align("------------------------------------------------------------------------------" + colour.ENDC))
forge()