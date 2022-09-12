import logging

#--------------------------------------
# RUN
# Default config being run, with values
# set later in this module
#--------------------------------------
def run():
    logging.getLogger('PIL').setLevel(logging.INFO)
    logging.basicConfig(level=logging.DEBUG, filename=name_creating(), format=format_creating())

def name_creating(name=""):
    import time
    name_list = ["core/logs/",
                 (time.gmtime(time.time()).tm_year), "_",
                 (time.gmtime(time.time()).tm_mon), "_",
                 (time.gmtime(time.time()).tm_mday), "_",
                 (time.gmtime(time.time()).tm_hour), "_",
                 (time.gmtime(time.time()).tm_min), "_",
                 (time.gmtime(time.time()).tm_sec), "_log.log"]
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
    import os, sys; spath = os.path.dirname(os.path.abspath("main.py"))
    sys.path.insert(0, f'{spath}')

def run_text():
    from system.ref_systems.system_ref import SysRef; import os; import sys
    from core.file_system.repo_manag import deep_file_lister; scripts = deep_file_lister(f"scripts/", ext="py")
    text = f'''
    ---------------------------------------------------------------------------------------
    Hello in {SysRef.name} logging system! 
    This is program initialisation message which will prompt you all important informations
    on current processes. All further info will be wrote during program running.
    
    Printing working directory of program:
    {os.getcwd()}    
    Printing the path of the program:
    {sys.path}
    
    Printing vanilla modules list:
    {SysRef.vanilla_modules}
    Printing scripts:
    {scripts}
    
    Printing init.toml informations:
    Version:     {SysRef.version} 
    Build type:  {SysRef.status}
    ---------------------------------------------------------------------------------------
    '''
    return text
