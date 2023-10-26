from core.data.pack_manag.types import pack_types
from core.file_system.parsers import loadTOML
from os.path import exists

def searchInfo(req_id: str) -> dict | None:
    """Browses through all pack folders to find -info.toml- file"""
    for packkind in pack_types:
        if exists(f"{packkind}/{req_id}/info.toml"):
            return loadTOML(f"{packkind}/{req_id}/info.toml")
    return None