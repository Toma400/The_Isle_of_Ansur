from core.data.save_system.req_data import SV_KIND
from core.file_system.parsers import loadYAML
from os.path import exists
import yaml

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

    # --- CLASS INVENTORY ---

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