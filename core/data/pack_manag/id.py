from enum import Enum

# class ID(Enum):
#     CID: "ClassID"
#     RID: "RaceID"
#     GID: "GenderID"
#     AID: "AttributeID"
#     SID: "SkillID"
#     # planned
#     EID: "EntityID"
#     LID: "LocationID"
#     HID: "ChestID"

def agnosticID(string: str) -> str:
    """Converts IDs into non-ID based ones. Currently investigated against `absoluteID` in issue #84"""
    if "ansur:" in string:
        return string.replace("ansur:", "")
    return string

def absoluteID(string: str) -> str:
    """Converts vague IDs into absolute ones, making core modules comparable in system"""
    if ":" not in string:
      return f"ansur:{string}"
    return string