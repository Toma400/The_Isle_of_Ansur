# BCS SHOULD BE GENERATOR
# So project folder should not have structure for mod, but rather instructions
# Folder structure should appear only when you click on "export" button, and should be in _bcs folder (sort of _temp variant)
from os import listdir, mkdir
import shutil
import zipfile, json

def jsonwrite(path, contents):
    dump_obj = json.dumps(contents, indent=1)
    with open (path, "w") as file:
        file.write(dump_obj)

def jsonread(path):
    with open (path) as file:
        return file.read()

def projectlist():
    return listdir("bcs/projects/")

def projectbuild(name):
    mkdir(f"bcs/projects/{name}")

def projectgenerator(name):
    pass

def projectexport(name):
    # 1. create _bcs temp folder with project files -> project structure
    # 2. zip _bcs folders into .zip file and put it into mods folder

    projectgenerator(name) #-> results on _bcs/projects/{name} folder getting resources

    obj = zipfile.ZipFile(f"mods/{name}.zip", mode="w")
    for i in listdir(f"_bcs/projects/{name}/"):
        obj.write(f"_bcs/projects/{name}/{i}", arcname=i)
    shutil.rmtree(f"_bcs/")