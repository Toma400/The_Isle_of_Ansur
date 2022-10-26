# BCS SHOULD BE GENERATOR
# So project folder should not have structure for mod, but rather instructions
# Folder structure should appear only when you click on "export" button, and should be in _bcs folder (sort of _temp variant)
from os import listdir, mkdir
import zipfile

def projectlist():
    return listdir("bcs/projects/")

def projectbuild(name):
    mkdir(f"bcs/projects/{name}")

def projectexport(name):
    obj = zipfile.ZipFile(f"mods/{name}.zip", mode="w")
    for i in listdir(f"bcs/projects/{name}/"):
        obj.write(f"bcs/projects/{name}/{i}", arcname=i)

def helpblit():
    return (
        '''
        | Navigate through the menus via writing words appearing on the screen
        | If there's list of elements, running command which is on the list
        | will activate manager of such element.
        | If command does not match, new element will be created and you will
        | be moved to its manager.
        '''
    )

def prompt_manag(prompt_given, menu, *args):
    if prompt_given == "exit": return exit()
    match menu:
        case "projects":
            if prompt_given in projectlist(): return proj_into(prompt_given)
            else:                             return projectbuild(prompt_given)

        case "start":
            match prompt_given:
                case "project": return proj()
                case "help":    return helpblit()

        case "proj_manag":
            match prompt_given:
                case "music":    pass
                case "panorama": pass
                case "export":   return projectexport(args[0])

def proj():
    while True:
        print("----------------- Baedoor Creation Set -----------------")
        print("                      < projects >                      ")
        for i in projectlist():
            print (f"| * {i}")
        prompt = input("|::: ")
        prompt_manag(prompt, "projects")

def proj_into(proj_name):
    while True:
        print("----------------- Baedoor Creation Set -----------------")
        print(f":: project opened --> {proj_name} ::")
        print("--------------------------------------------------------")
        print('''
        | Use those commands to navigate in your project:
        | 
        | - music -
        | allows you to add your custom music file as a menu background
        | - panorama -
        | allows you to add your custom image as a menu background
        | - export -
        | creates exported .zip file for your mod
        ''')
        prompt = input("|::: ")
        prompt_manag(prompt, "proj_manag", proj_name)

while True:
    print ("----------------- Baedoor Creation Set -----------------")
    print (
    '''
    | Welcome in BCS!
    | Use specific keywords to work with this software:
    |
    | - project -
    | - help - 
    | - exit -
    | 
    | At first, inputting -help- is recommended, to understand some
    | basics about this software.
    ''')
    prompt = input("|::: ")
    prompt_manag(prompt, "start")