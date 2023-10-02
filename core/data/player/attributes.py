from core.gui.manag.langstr import langstring as lstr

class Attribute:

    def __init__(self, name: str, key: str):
        self.name = name
        self.key  = key

    def langstr(self) -> str:
        """Returns langstring of object based on currently used language"""
        return lstr(key=self.key)

    def __repr__(self) -> str:
        return self.langstr()

    def __str__(self) -> str:
        return self.langstr()


def getAttributes() -> list[Attribute]:
    """Main gatherer of attributes available in game"""
    return [
        Attribute("strength",     "stat__atr_strength"),
        Attribute("endurance",    "stat__atr_endurance"),
        Attribute("agility",      "stat__atr_agility"),
        Attribute("intelligence", "stat__atr_intelligence"),
        Attribute("charisma",     "stat__atr_charisma")
    ]

def getAttributesTuple() -> list[(str, str)]:
    """Compatible variant that translates -getAttributes()- into PyGame GUI compatible format"""
    ret = []
    for skill in getAttributes():
        ret.append((skill.langstr(), skill.name))
    return ret