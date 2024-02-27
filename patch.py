from core.data.save_system.update import updateSave
from core.data.save_system.walk import listSaves
from core.file_system.parsers import loadTOML
from os.path import exists
from os import remove

# PATCH_NAME = Patch_PreAlpha5

try:
    if not exists(".dev"):
        for save in listSaves(False):
            presave = f"saves/{save}/buffer/presave.toml"
            if exists(presave):
                data = loadTOML(presave)
                # filling missing 'settings' data
                data["settings"] = {
                    "permadeath": False
                }
                try:
                    updateSave(save, data)
                    remove(presave)
                except Exception as e:
                    print(e)
        print("Saves updated successfully")
    else:
        print("Developer's build, no updating was performed")
except Exception as e:
    print(e)

input("Press Enter to finish")