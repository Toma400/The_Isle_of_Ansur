from core.data.save_system.update import updateSave
from core.data.save_system.walk import listSaves
from core.file_system.parsers import loadTOML
from os.path import exists
from os import remove

# PATCH_NAME = LocationUpdatePatch

if not exists(".dev"):
    for save in listSaves(False):
        presave = f"saves/{save}/buffer/presave.toml"
        if exists(presave):
            data = loadTOML(presave)
            updateSave(save, data)
            remove(presave)