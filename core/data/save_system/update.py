from core.data.save_system.update_ref.statistics import updateAttributes, updateSkills
from core.data.save_system.update_ref.packs import updateMods
from core.data.save_system.update_ref.data import updateData
from core.data.save_system.req_data import SV_KIND, REQUIRED_DIRS
from os.path import exists
from os import mkdir

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

    if not exists(f"saves/{name}"):
        mkdir(f"saves/{name}/{SV_KIND.BUFFER.value}")
    for rd in REQUIRED_DIRS:
        if not exists(f"saves/{name}/{SV_KIND.BUFFER.value}/{rd}"):
            mkdir(f"saves/{name}/{SV_KIND.BUFFER.value}/{rd}")
    # REQUIRED_FILES are delayed because they will be added in following function calls

    updateAttributes(name, data)
    updateSkills(name, data)
    updateData(name, data)
    updateMods(name, data) # TODO: returns whether there was issue while loading packs
    # to find place somewhere:
    # - religion (can change)
    # - history (written stuff)

