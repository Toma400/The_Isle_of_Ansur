# BCS SHOULD BE GENERATOR
# So project folder should not have structure for mod, but rather instructions
# Folder structure should appear only when you click on "export" button, and should be in _bcs folder (sort of _temp variant)
# ===========================================================================================================================
from os import listdir, mkdir
import shutil, os, pygame
import zipfile, json
gpath = os.path.dirname(os.path.abspath("bcset.py"))

def settings (key):
    with open(f"{gpath}/settings.json", encoding="utf-8") as json_file:
        return json.load(json_file)[key]

def langstr (key: str):
    def langlist(keyword):
        match keyword:
            case "english": return "en_us"
            case "polish":  return "pl_pl"

    lang = langlist(settings("language"))
    import toml; t = toml.load(f"{gpath}/bcs/lang/{lang}.toml")
    return t[key]

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
    for i in listdir(f"_bcs/export/"):
        obj.write(f"_bcs/export/{i}", arcname=i)
    shutil.rmtree(f"_bcs")

def img_load(path, name="", alpha=False):
    """Function-aimed alternative to Image.reload()"""
    surface = pygame.image.load(f"{gpath}/{path}{name}")
    if alpha is False: return surface.convert()
    else:              return surface.convert_alpha()  # for transparent textures (alpha=True)



class GH:
    W = (settings("res_x"), settings("res_y"))
    X = 0
    Y = 1

def cell(value, axis):
    return int(value * (GH.W[axis] // 100))

def cells(x, y):
    return cell(x, GH.X), cell(y, GH.Y)