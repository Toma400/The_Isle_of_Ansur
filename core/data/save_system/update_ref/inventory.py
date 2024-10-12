from core.file_system.parsers import loadYAML, loadTOML
from core.data.player.profession import getClass
from core.data.player.origin import getOrigin
from core.data.player.inventory import addItem
from core.data.save_system.req_data import SV_KIND
from os.path import exists
import logging as log
import yaml, toml

def updateInventory(name: str, data: dict = None):
    inv = {
        "stackables": {

        },
        "uniques": [

        ]
    }
    eq = {
            # jewelry
            "amulet" : "",
            "ring1"  : "",
            "ring2"  : "",
            # armour
            "head"    : "", # used for: helmets, hats, circlets, crowns
            "torso"   : "", # used for: cuirass, shirt
            "greaves" : "",
            "boots"   : "", # used for: boots, shoes
            # major clothing
            "shirt" : "",
            "pants" : "",
            # minor clothing
            "belt"   : "",
            "glove"  : "",
            # weapons / tools / shields / other
            "l_hand" : "",
            "r_hand" : ""
            # special containers
            # "quiver"   -> arrows
            # "scabbard" -> swords
    }

    inv_keys = inv.keys()
    eq_keys  = eq.keys()

    if exists(f"saves/{name}/{SV_KIND.BUFFER.value}/inventory.yaml"):
        get      = loadYAML(f"saves/{name}/{SV_KIND.BUFFER.value}/inventory.yaml")
        get_keys = get.keys()
        for line in inv_keys:
            if line not in get_keys:
                raise KeyError(f"Saved -inventory.yaml- for character: {name} do not contain required key: {line}. Save is either corrupted or needs patch.")
        inv = get
    if exists(f"saves/{name}/{SV_KIND.BUFFER.value}/equip.yaml"):
        get      = loadYAML(f"saves/{name}/{SV_KIND.BUFFER.value}/equip.yaml")
        get_keys = get.keys()
        for line in eq_keys:
            if line not in get_keys:
                raise KeyError(f"Saved -equip.yaml- for character: {name} do not contain required key: {line}. Save is either corrupted or needs patch.")
        eq = get

    # checking for correctness
    for inv_key in inv_keys:
        if inv_key not in inv:
            raise KeyError(f"Provided -inv- key is None: {inv_key}")
    for eq_key in eq_keys:
        if eq_key not in eq:
            raise KeyError(f"Provided -eq- key is None: {eq_key}")

    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/inventory.yaml", "w", encoding="utf8") as f1:
        yaml.dump(inv, f1)
        f1.flush()
    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/equip.yaml", "w", encoding="utf8") as f2:
        yaml.dump(eq, f2)
        f2.flush()

def addClassInventory(name: str):
    get = loadTOML(f"saves/{name}/{SV_KIND.BUFFER.value}/data.toml")

    oc  = getClass(get["class"])
    add = oc.getc("new_game", "inventory")

    if add is not None:
        if "stackables" in add.keys():
            for iid, val in add["stackables"].items():
                addItem(name, iid, val)
        if "uniques" in add.keys():
            for item in add["uniques"]:
                (iid, val), = item.items()
                addItem(name, iid, val)

def addOriginInventory(name: str):
    get = loadTOML(f"saves/{name}/{SV_KIND.BUFFER.value}/data.toml")

    og  = getOrigin(get["origin"])
    add = og.getc("new_game", "inventory")

    if add is not None:
        if "stackables" in add.keys():
            for iid, val in add["stackables"].items():
                addItem(name, iid, val)
        if "uniques" in add.keys():
            for item in add["uniques"]:
                (iid, val), = item.items()
                addItem(name, iid, val)