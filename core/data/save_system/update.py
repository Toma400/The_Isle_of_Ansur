from core.data.save_system.update_ref.statistics import updateAttributes, updateSkills
from core.data.save_system.update_ref.inventory import updateInventory, addOriginInventory, addClassInventory
from core.data.save_system.update_ref.player import updatePlayer
from core.data.save_system.update_ref.packs import updateMods
from core.data.save_system.update_ref.data import updateData
from core.data.save_system.req_data import SV_KIND, REQUIRED_DIRS
from os.path import exists
from os import makedirs
import logging as log

def updateSave(name: str, data: dict = None):
    """
    Should be cast during:
    - initialising character (`data` is journey.inidata)
    - loading game           (`data` is None)
    It manages both existence of certain folder structure,
    updating of attributes/skills/etc. if new mods are
    added, and everything else.

    This should be run instead of Journey system, because
    Journey was not meant to handle saves and all that
    data - it only makes more mess, as it adds more tasks
    to module that was meant to be just class to hold
    all things you encounter during gameplay.

    TODO: Reflect differences between BUFFER and ADVENTURE, because if we load from
          BUFFER, it will not make sense for loading savegames
          But writing things to buffer first should be priority, as it is where
          in general writing is meant to be
    """
    # SV_DIR = SV_KIND.BUFFER.value if data is None else SV_KIND.ADVENTURE.value
    validateData(data)

    if not exists(f"saves/{name}"):
        makedirs(f"saves/{name}/{SV_KIND.BUFFER.value}")
    for rd in REQUIRED_DIRS:
        if not exists(f"saves/{name}/{SV_KIND.BUFFER.value}/{rd}"):
            makedirs(f"saves/{name}/{SV_KIND.BUFFER.value}/{rd}")
    # REQUIRED_FILES are delayed because they will be added in following function calls

    updateAttributes(name, data)
    updateSkills(name, data)
    updatePlayer(name, data)
    updateData(name, data)
    updateMods(name) # TODO: returns whether there was issue while loading packs

    updateInventory(name, data)
    if data is not None:
        addOriginInventory(name)
        addClassInventory(name)
    # to find place somewhere:
    # - settings
    # - religion (can change)
    # - history (written stuff)
    # - origin-related:
    #   - inventory

def validateData(data: dict):
    """Checks passed `data` to updateSave to see whether all elements exist there"""
    keys_saved = ["gender", "race", "class", "name", "attr", "skill", "religion", "origin", "history", "settings"]

    for k in keys_saved:
        if k not in data:
            log.log(log.ERROR, f"Couldn't find {k} in -inidata- dictionary. Printing dictionary contents:")
            for entry, value in data:
                log.log(log.INFO, f"- {entry}: {value}")
            raise KeyError("Raising crash due to the issue above.")