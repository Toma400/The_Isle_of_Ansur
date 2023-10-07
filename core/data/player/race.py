from core.data.pack_manag.id import agnosticID
from core.gui.manag.langstr import langjstring
from system.mod_manag import mod_lister
from glob import glob as walkdir
from os.path import exists
import json

class Race:

    cache = None

    def __init__(self, name: str, tr_key: str, mod_id: str):
        self.name   : str = name    # name ID (used for RID)
        self.key    : str = tr_key  # translation key
        self.mod_id : str = mod_id  # mod ID

    def rid(self) -> str:
        """Creates RID representation of race, to export/import during game"""
        return f"{self.mod_id}:{self.name}"

    def langstr(self) -> str:
        """Returns langstring of object based on currently used language"""
        return langjstring(key=self.key, modtype="stats", modid=self.mod_id)

    def descr(self) -> str:
        """Returns description of Race taken from -key[_descr]-"""
        return langjstring(f"{self.key}_descr", "stats", self.mod_id)

    def get(self, attribute: str) -> str | int | float | list | dict:
        """Returns specific attribute from Race file. Any reuse of the same object reads from cache to optimise I/O"""
        if self.cache is None:
            with open(f"stats/{self.mod_id}/races/{self.name}.json") as jf:
                self.cache = json.load(jf)
        return self.cache[attribute]

    def getc(self, category: str, attribute: str) -> str | int | float | list | dict:
        """Returns attribute from category dict. Used mostly with sections like -skills- or -attrs- by Races"""
        return self.get(category)[attribute]

    def __repr__(self) -> str:
        return self.langstr()

    def __str__(self) -> str:
        return self.langstr()

def getRace(rid: str) -> Race:
    """Race constructor that uses RID instead of explicit __init__ constructor. Resource-heavy in iteration compared to getRaces()"""
    rid_ems = rid.split(":")

    def returnKey() -> str: # returns translation key
        with open(f"stats/{rid_ems[0]}/races/{rid_ems[1]}.json") as jf:
            pjf = json.load(jf)
            return pjf["key"]

    return Race(name=rid_ems[1], tr_key=returnKey(), mod_id=rid_ems[0])

def getRaces() -> list[Race]:
    """Main gatherer of race data during load/reload"""
    ret: list[Race] = []
    for stat_pack in mod_lister("stats"):
        if exists(f"stats/{stat_pack}/races"):
            for race_file in walkdir(f"stats/{stat_pack}/races/*.json"):
                race_name = race_file.replace(f"stats/{stat_pack}/races", "").replace(".json", "").strip("\\")
                with open(race_file) as jf:
                    pjf = json.load(jf)
                    ret.append(Race(race_name, pjf["key"], stat_pack))
    return ret

def getRacesTuple() -> list[(str, str)]:
    """PyGame_GUI - friendly variant of Race getter, returning tuple of <translation, RID>"""
    ret: list[(str, str)] = []
    for rc in getRaces():
        ret.append((rc.langstr(), rc.rid()))
    return ret

def getRaceNames(rid: str, gid: str) -> list[(str, str)]:
    """Returns list of names derived from race JSON. Uses tuple for compatibility with PyGame GUI system"""
    ret = []
    try:                                                             # searches for gender specified by GID
        try: # checks for 'female'/'male' etc.
            for name in getRace(rid).getc("names", agnosticID(gid)):
                ret.append((name, name))
        except: # checks for 'ansur:female'/'ansur:male' etc.
            for name in getRace(rid).getc("names", gid):
                ret.append((name, name))
    except:                                                          # runs when specific gender is not found
        try: # checks if 'strict' parameter exists                     # if 'strict' parameter is not True
            if getRace(rid).getc("names", "strict") is False:          # it takes names from all genders
                for gend in getRace(rid).get("names"):
                    for name in getRace(rid).getc("names", gend):
                        ret.append((name, name))
        except: # runs if 'strict' does not exist (defaults to False)
            for gend in getRace(rid).get("names"):
                for name in getRace(rid).getc("names", gend):
                    ret.append((name, name))
    finally:
        ret.sort()
        return ret