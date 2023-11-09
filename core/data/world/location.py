from core.gui.manag.langstr import langjstring
import toml

class Location:

    def __init__(self, name: str, tr_key: str, mod_id: str):
        self.name   : str = name       # name ID (used for LID)
        self.key    : str = tr_key     # translation key
        self.mod_id : str = mod_id     # mod ID

    def lid(self) -> str:
        """Creates LID representation of location, to export/import during game"""
        return f"{self.mod_id}:{self.name}"

    def langstr(self) -> str:
        """Returns langstring of object based on currently used language"""
        return langjstring(key=self.key, modtype="worlds", modid=self.mod_id)

    def __repr__(self) -> str:
        return self.langstr()

    def __str__(self) -> str:
        return self.langstr()


def getLocation(lid: str) -> Location:
    """Location constructor that uses LID instead of explicit __init__ constructor. Resource-heavy in iteration compared to getLocations()"""
    lid_ems = lid.split(":")

    def returnKey() -> str: # returns translation key
        pjf = toml.load(f"worlds/{lid_ems[0]}/locations/{lid_ems[1]}.toml")
        return pjf["key"]

    return Location(name=lid_ems[1], tr_key=returnKey(), mod_id=lid_ems[0])