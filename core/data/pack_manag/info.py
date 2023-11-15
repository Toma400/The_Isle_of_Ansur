from core.data.pack_manag.types import pack_types
from core.file_system.parsers import loadTOML
from os.path import exists

def searchInfo(req_id: str, union=False) -> dict | None or (str, dict):
    """Browses through all pack folders to find -info.toml- file. Set -union- to True if you want to know where pack is"""
    for packkind in pack_types:
        if exists(f"{packkind}/{req_id}/info.toml"):
            if union:
                return packkind, loadTOML(f"{packkind}/{req_id}/info.toml")
            return loadTOML(f"{packkind}/{req_id}/info.toml")
    return None