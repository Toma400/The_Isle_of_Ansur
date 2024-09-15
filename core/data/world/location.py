from core.file_system.repo_manag import file_lister
from core.gui.registry.pgui_objects import PGUI_Helper
from core.decorators import RequiresImprovement
from core.gui.manag.langstr import langjstring
from os.path import exists
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

def getDestinations(lid: str) -> list[(str, str)]:
    """PyGame_GUI - friendly getter for travel destinations, returning tuple of <translation, LID>"""
    ret: list[(str, str)] = []
    lid_ems = lid.split(":")

    if not exists(f"worlds/{lid_ems[0]}/locations/{lid_ems[1]}/destinations"): return ret # early return

    for dest in file_lister(f"worlds/{lid_ems[0]}/locations/{lid_ems[1]}/destinations/", ext="toml"):
        dest_info = toml.load(f"{dest}.toml")
        dest_id  = None
        dest_key = None
        if "key"         in dest_info.keys(): dest_key = langjstring(dest_info["key"], "worlds", lid_ems[0]) # translation, `dest_info["key"]` yields pure langstr
        if "destination" in dest_info.keys(): dest_id  = dest_info["destination"]
        if dest_id is not None and dest_key is not None:
            ret.append((dest_key, dest_id))
    return ret