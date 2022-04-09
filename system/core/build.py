#-----------------------------------------------------------
# BUILD
# Module used to build .exe file from current files using
# pyInstaller. All needed documentation is written here
# in further comment blocks.
#-----------------------------------------------------------

import PyInstaller.__main__
import PyInstaller
from distutils.dir_util import copy_tree
from utils.colours import bcolors as colour
from utils.text import text_align as align

#-----------------------------------------------------------
# RUN
# Used to execute pyInstaller commands precised later in
# module.
# References DefaultRun class
#-----------------------------------------------------------
class DefaultRun:

    # values used for run() function
    core_path = "D:/Ministerstwo Kalibracyjne/PyCharm_Projects/Isle_of_Ansur/"
    game_name = "Isle of Ansur"
    icon_path = core_path + "utils/assets/icon.ico"
    export_path = "D:/Ministerstwo Kalibracyjne/PyCharm_Projects/builds/"
    full_export_path = export_path + game_name + "/"
    forge_builder = [
        core_path + "main.py",
        "--onedir",
        "--noupx",  # if you are going to change this, please redirect upx to net source (requests library?)
        "--clean",
        "--name=" + game_name,
        "--icon=" + icon_path,
        "--distpath=" + export_path,
        "--workpath=" + core_path + "system/cache/pyinstaller",
        "--specpath=" + core_path + "system/cache/pyinstaller"
    ]
    ommitted_elements = [  # list of files that are deleted after finishing the build
        full_export_path + ".idea/",
        full_export_path + "_pycache_/",
        full_export_path + ".breakpoints",
        full_export_path + ".gitignore"
    ]

#----------------------------------------------------------------------
# REFERENCE DOCS
# https://github.com/pyinstaller/pyinstaller/blob/v4.5.1/doc/usage.rst
#----------------------------------------------------------------------
def run():
    PyInstaller.__main__.run(
        DefaultRun.forge_builder
    )
    copy_tree(DefaultRun.core_path, DefaultRun.full_export_path) # copies all files over
    print(align(colour.CGREEN + "Build successful" + colour.ENDC, "centre_colour"))

def forge():
    try:
        run()
    except:
        print(align(colour.HEADER + "Build failed" + colour.ENDC, "centre_colour"))

    # NON USED ELEMENTS
    # '--onefile' -> single .exe element
    # '--adddata' -> maybe useful for handling non-module folders

print(align("------------------------------", "centre"))
print(align(" BUILD CONSTRUCTOR ", "centre"))
print("\n")
print(align("----------------------------", "left"))
print(align("------------------------------------------------------------------------------", "centre"))
forge()