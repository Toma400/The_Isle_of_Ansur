from core.data.save_system.update import updateSave
from core.data.save_system.walk import listSaves
from core.file_system.parsers import loadTOML
from os.path import exists

for save in listSaves(False):
    if exists(f"saves/{save}/buffer/presave.toml"):
        data = loadTOML(f"saves/{save}/buffer/presave.toml")
        updateSave(save, data)