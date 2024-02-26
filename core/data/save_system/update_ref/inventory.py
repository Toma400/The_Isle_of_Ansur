from core.file_system.parsers import loadYAML, loadTOML
from core.data.player.profession import getClass
from core.data.player.origin import getOrigin
from core.data.save_system.req_data import SV_KIND
from os.path import exists
import logging as log
import yaml, toml

def updateInventory(name: str, data: dict = None):
    inv = {
        "loose": [

        ],
        "active": {
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
            "l_hand": "",
            "r_hand": ""
            # special containers
            # "quiver"   -> arrows
            # "scabbard" -> swords
        }
    }

    inv_keys = inv.keys()
    val_keys = inv["active"].keys()

    if exists(f"saves/{name}/{SV_KIND.BUFFER.value}/inventory.yaml"):
        get      = loadYAML(f"saves/{name}/{SV_KIND.BUFFER.value}/inventory.yaml")
        get_keys = get.keys()
        get_vals = get["active"].keys() if "active" in get_keys else None
        for line in inv_keys:
            if line not in get_keys:
                raise KeyError(f"Saved -inventory.yaml- for character: {name} do not contain required key: {line}. Save is either corrupted or needs patch.")
        for line in val_keys:
            if line not in get_vals: # if get_vals is None, it will be catched by previous iterations over get_keys
                raise KeyError(f"Saved -inventory.yaml- for character: {name} do not contain required key: {line}. Save is either corrupted or needs patch.")
        inv = get

    # checking for correctness
    for inv_key in inv_keys:
        if inv_key not in inv:
            raise KeyError(f"Provided -inv- key is None: {inv_key}")
    for val_key in val_keys:
        if val_key not in inv["active"]:
            raise KeyError(f"Provided -inv- key is None: {val_key}")

    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/inventory.yaml", "w") as f:
        yaml.dump(inv, f)
        f.flush()

def addItem(iid: str, name: str, count: int = 1) -> None:
    """Temporary system to add items to inventory. Return is purely for logging purposes"""
    """WARNING: IT IS PURELY FOR STACKABLE ITEMS"""
    def scan(l: list[dict[str, int]], iid: str) -> int:
        pos = 0
        for entry in l:
            if iid in entry:
                return pos
            else:
                pos += 1
        return -1

    if exists(f"saves/{name}/{SV_KIND.BUFFER.value}/inventory.yaml"):
        get = loadYAML(f"saves/{name}/{SV_KIND.BUFFER.value}/inventory.yaml")
        if "loose" in get:
            is_in = scan(get["loose"], iid) # if item is in inventory (if yes = position, else = -1)
            if is_in != -1:
                get["loose"][is_in] = {iid: get["loose"][is_in][iid] + count} # adds the number
            else:
                get["loose"].append({iid: count}) # sets the number

            with open(f"saves/{name}/{SV_KIND.BUFFER.value}/inventory.yaml", "w") as f:
                yaml.dump(get, f)
                f.flush()
            return None
    log.error(f"Tried to add item of ID: {iid}, to the player of name: {name}, but failed.")

def addClassInventory(name: str):
    get = loadTOML(f"saves/{name}/{SV_KIND.BUFFER.value}/data.toml")

    oc  = getClass(get["class"])
    add = oc.getc("new_game", "inventory")

    if add is not None:
        for item in add:
            for iid, val in item.items():
                addItem(iid, name, val)

    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/data.toml", "w") as f:
        toml.dump(get, f)
        f.flush()

def addOriginInventory(name: str):
    get = loadTOML(f"saves/{name}/{SV_KIND.BUFFER.value}/data.toml")

    og  = getOrigin(get["origin"])
    add = og.getc("new_game", "inventory")

    if add is not None:
        for item in add:
            for iid, val in item.items():
                addItem(iid, name, val)

    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/data.toml", "w") as f:
        toml.dump(get, f)
        f.flush()