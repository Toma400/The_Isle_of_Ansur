from core.file_system.repo_manag import file_lister
from core.gui.registry.pgui_objects import PGUI_Helper
from core.decorators import RequiresImprovement, Deprecated
from core.gui.manag.langstr import langjstring
from core.data.world.time import parseBaeTime
from core.data.custom_scripts.travel import travelScript, travelScriptEdit
from core.file_system.parsers import loadYAML, writeYAML
from os.path import exists
import logging as log
import toml

class Location:

    cache = None

    def __init__(self, name: str, tr_key: str, mod_id: str):
        self.name   : str = name       # name ID (used for LID)
        self.key    : str = tr_key     # translation key
        self.mod_id : str = mod_id     # mod ID
        self.img    : str = f"worlds/{mod_id}/assets/{self.get('background')}" if self.get("background") is not None else PGUI_Helper.def_img

    def lid(self) -> str:
        """Creates LID representation of location, to export/import during game"""
        return f"{self.mod_id}:{self.name}"

    def langstr(self) -> str:
        """Returns langstring of object based on currently used language"""
        return langjstring(key=self.key, modtype="worlds", modid=self.mod_id)

    @RequiresImprovement
    def descr(self) -> str:
        """Returns description of Location taken from -key[_descr]-. Should be improved to recognise context and other elements"""
        try:    return langjstring(f"{self.key}_descr", "worlds", self.mod_id)
        except: return ""

    def get(self, attribute: str) -> str | int | float | list | dict | None:
        """Returns specific attribute from Location file. Any reuse of the same object reads from cache to optimise I/O"""
        if self.cache is None:
            self.cache = toml.load(f"worlds/{self.mod_id}/locations/{self.name}/info.toml")
        if attribute in self.cache.keys():
            return self.cache[attribute]
        else:
            return None

    def getc(self, category: str, attribute: str) -> str | int | float | list | dict | None:
        """Returns attribute from category dict."""
        ctg = self.get(category)
        if ctg is not None:
            if attribute in ctg.keys():
                return self.get(category)[attribute]
        return None

    def __repr__(self) -> str:
        return self.langstr()

    def __str__(self) -> str:
        return self.langstr()


def getLocation(lid: str) -> Location:
    """Location constructor that uses LID instead of explicit __init__ constructor"""
    lid_ems = lid.split(":")

    def returnKey() -> str: # returns translation key
        pjf = toml.load(f"worlds/{lid_ems[0]}/locations/{lid_ems[1]}/info.toml")
        return pjf["key"]

    return Location(name=lid_ems[1], tr_key=returnKey(), mod_id=lid_ems[0])

def getDestinations(dyn_screen, lid: str) -> list[(str, dict)]:
    """PyGame_GUI - friendly getter for travel destinations, returning tuple of <translation, destination dict>"""
    ret: list[(str, str)] = []
    lid_ems = lid.split(":")

    if not exists(f"worlds/{lid_ems[0]}/locations/{lid_ems[1]}/destinations"): return ret # early return

    for dest in file_lister(f"worlds/{lid_ems[0]}/locations/{lid_ems[1]}/destinations/", ext="toml"):
        dest_info = toml.load(f"{dest}.toml")
        dest_keys = dest_info.keys()
        if "key" in dest_keys and "destination" in dest_keys:
            if "always_visible" in dest_keys: # hides entry if it doesn't pass checks (default = always visible)
                if dest_info["always_visible"] is False:
                    if checkDestination(dyn_screen, dest) is False:
                        continue
            ret.append((langjstring(dest_info["key"], "worlds", lid_ems[0]), # translation, `dest_info["key"]` yields pure langstr
                        dest))                                          # dict
    return ret

def getDestinationDescr(dyn_screen, dest: str) -> str:
    """`dest` should be path to .toml file of respective destination"""
    if dest is None:               return ""
    if not exists(f"{dest}.toml"): return ""

    dest_info = toml.load(f"{dest}.toml")
    if "descr" in dest_info.keys():
        return langjstring(dest_info["descr"], "worlds", getLocation(dyn_screen.journey.location).mod_id)

def checkDestination(dyn_screen, dest: str) -> bool:
    """`dest` should be path to .toml file of respective destination | only performs `req` and `req_or` checks"""
    if dest is None:               return False
    if not exists(f"{dest}.toml"): return False

    dest_info = toml.load(f"{dest}.toml")
    dest_keys = dest_info.keys()

    out_1 = True
    out_2 = False

    if "req" in dest_keys: # if not, it's just True by default
        for r in dest_info["req"]:
            if travelScript(dyn_screen, r) is False:
                out_1 = False

    if "req_or" not in dest_keys:
        out_2 = True
    else:
        for r in dest_info["req_or"]:
            if travelScript(dyn_screen, r) is True:
                out_2 = True
        if len(dest_info["req_or"]) == 0: # in case someone leaves empty []
            out_2 = True

    return out_1 and out_2

def travelTo(dyn_screen, dest: str):
    """`dest` should be path to .toml file of respective destination | only performs `cost` and `set`"""
    """TODO: perform `cost` and `set` here, also move the character? (this would need Journey ig)"""
    dest_info = toml.load(f"{dest}.toml")
    dest_keys = dest_info.keys()

    if "cost" in dest_keys:
        for r in dest_info["cost"]:
            travelScriptEdit(dyn_screen, r, 0)

    if "set" in dest_keys:
        for r in dest_info["set"]:
            travelScriptEdit(dyn_screen, r, 1)

    # TODO: ideally, there should be a func that updates all object-like Journey fields (so, ones not read from buffer by default) and this section below
    #       should just have .set() to update .toml file (after which dest_info would be read from it)
    dyn_screen.journey.location = dest_info["destination"] # ^ and after that above, this would be `parseLocation` or sth reading from buffer, not destination file
    dyn_screen.journey.set("player.toml | location", dest_info["destination"])
    dyn_screen.journey.date = parseBaeTime(dyn_screen.journey.readDate(dyn_screen.journey.verify))