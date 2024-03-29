from core.data.save_system.req_data import SV_KIND, DEF_ATTR, ADD_ATTR, DEF_SKL, ADD_SKL
from core.data.player.attributes import getAttributes
from core.data.player.profession import getClass
from core.data.player.skills import getSkills
from core.data.player.race import getRace
from core.data.pack_manag.id import absoluteID
from core.file_system.parsers import loadYAML
from os.path import exists
import yaml

def updateAttributes(name: str, data: dict = None):
    """
    Takes TOML file with attributes and check whether all attributes are actually there
    Adds new ones if they don't exist, setting them to default if `data` doesn't bring any bonuses

    Do not check for 'deprecated' attributes, if there's one that is removed, it won't make
    any difference anyway.

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

    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/statistics/attributes.yaml", "w", encoding="utf8") as f:
        yaml.dump(atrout, f)
        f.flush()

def updateSkills(name: str, data: dict = None):
    """
    Takes TOML file with skills and check whether all skills are actually there
    Adds new ones if they don't exist, setting them to default if `data` doesn't bring any bonuses

    Do not check for 'deprecated' attributes, if there's one that is removed, it won't make
    any difference anyway.

    TODO: Check if current getAttributes() and its dependencies aren't using disabled packs
          (found no safeguard for this in code, but maybe there's something protecting from it)
    """
    skills = getSkills()
    skout  = {}
    if exists(f"saves/{name}/{SV_KIND.BUFFER.value}/statistics/skills.yaml"):
        atrout = loadYAML(f"saves/{name}/{SV_KIND.BUFFER.value}/statistics/skills.yaml")

    # checking and resupplying attributes that were not added before
    for sk in skills:
        if sk.sid() not in skout:
            skout[sk.sid()] = DEF_SKL

    # run only when initialising character
    if data is not None:
        # adding manually put attribute
        skout[data["skill"]] = skout[data["skill"]] + ADD_SKL

        # race scan
        rsk = getRace(data["race"]).get("skills")
        if rsk is not None:
            for rskr, rskv in rsk.items():
                skout[absoluteID(rskr)] = skout[absoluteID(rskr)] + rskv

        # class scan
        csk = getClass(data["class"]).get("skills")
        if csk is not None:
            for cskr, cskv in csk.items():
                skout[absoluteID(cskr)] = skout[absoluteID(cskr)] + cskv

    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/statistics/skills.yaml", "w", encoding="utf8") as f:
        yaml.dump(skout, f)
        f.flush()