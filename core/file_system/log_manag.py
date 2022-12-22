from core.file_system.repo_manag import deep_file_lister
from core.utils import sysref
import logging
import time
import sys
import os

# --------------------------------------
# RUN
# Default config being run, with values
# set later in this module
# --------------------------------------
def run():
    logging.getLogger('PIL').setLevel(logging.INFO)
    logging.basicConfig(level=logging.DEBUG, filename=name_creating(), format=format_creating())


def name_creating(name=""):
    name_list = ["core/logs/",
                 (time.gmtime(time.time()).tm_year), "_",
                 (time.gmtime(time.time()).tm_mon),  "_",
                 (time.gmtime(time.time()).tm_mday), "_",
                 (time.gmtime(time.time()).tm_hour), "_",
                 (time.gmtime(time.time()).tm_min),  "_",
                 (time.gmtime(time.time()).tm_sec),  "_log.log"]
    for i in name_list:
        name = name + str(i)
    return name


def format_creating(text=""):
    format_list = ["[",
                   "%(asctime)s", "] [",
                   "%(levelname)s", "] [",
                   "%(message)s", "]"]
    for i in format_list:
        text = text + str(i)
    return text


def run_path():
    spath = os.path.dirname(os.path.abspath("main.py"))
    sys.path.insert(0, f'{spath}')


def run_text():
    scripts = deep_file_lister(f"scripts/", ext="py")
    text = f'''
    ---------------------------------------------------------------------------------------
    Hello in {sysref('name')} logging system! 
    This is program initialisation message which will prompt you all important informations
    on current processes. All further info will be wrote during program running.

    Printing working directory of program:
    {os.getcwd()}    
    Printing the path of the program:
    {sys.path}

    Printing vanilla modules list:
    {sysref('vanilla_modules')}
    Printing packs:
    [Awaits implementation]
    Printing scripts:
    {scripts}

    Printing init.toml informations:
    Version:     {sysref('version')} 
    Build type:  {sysref('status')}
    ---------------------------------------------------------------------------------------
    '''
    return text
