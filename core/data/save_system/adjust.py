from core.data.save_system.req_data import SV_KIND, REQUIRED_DIRS, DEF_ATTR, ADD_ATTR
from core.data.player.attributes import getAttributes
from core.data.player.profession import getClass
from core.data.player.race import getRace
from core.data.pack_manag.id import absoluteID
from core.file_system.parsers import loadYAML
from os.path import exists
from os import mkdir
import yaml

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
    # all other update thingies

def updateAttributes(name: str, data: dict = None):
    """
    Takes TOML file with attributes and check whether all attributes are actually there
    Adds new ones if they don't exist, setting them to default if `data` doesn't bring any bonuses

    Do not check for 'deprecated' attributes, if there's one that is removed, it won't make
    any difference anyway.

    TODO: Check if TOML can accept keys with ":" symbol, so we can use AID (later other IDs too)
          as keys, or if we should go for YAML instead
    TODO: Check if current getAttributes() and its dependencies aren't using disabled packs
          (found no safeguard for this in code, but maybe there's something protecting from it)
    """
    attrs  = getAttributes()
    atrout = {}
    if exists(f"saves/{name}/{SV_KIND.BUFFER.value}/statistics/attributes.yaml"):
        atrout = loadYAML(f"saves/{name}/{SV_KIND.BUFFER.value}/statistics/attributes.yaml")

    # checking and resupplying attributes that were not added before
    for attr in attrs:
        if attr.aid() not in atrout:
            atrout[attr.aid()] = DEF_ATTR

    # run only when initialising character
    if data is not None:
        # adding manually put attribute
        atrout[data["attr"]] = atrout[data["attr"]] + ADD_ATTR

        # race scan
        rat = getRace(data["race"]).get("attributes")
        if rat is not None:
            for ratr, ratv in rat.items():
                atrout[absoluteID(ratr)] = atrout[absoluteID(ratr)] + ratv

        # class scan
        cat = getClass(data["class"]).get("attributes")
        if cat is not None:
            for catr, catv in cat.items():
                atrout[absoluteID(catr)] = atrout[absoluteID(catr)] + catv

    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/statistics/attributes.yaml", "w") as f:
        yaml.dump(atrout, f)
        f.flush()

    # use 'data', and also use 'readTOML' if it exists (if not, create it)
