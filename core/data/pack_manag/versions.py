from core.data.pack_manag.info import searchInfo
import logging as log
import re

"""
IoA versioning systems:

      | Example | Unified |
n     | 2       | 2, 0.0  | Single digit
n.n   | 2.1     | 2, 1.0  | Double digit
n.nx  | 2.1b    | 2, 1.1  | Double digit with letter
n.n.n | 2.1.1   | 2, 1.1  | Semantic versioning
"""

def unifiedVersion(ver: str) -> (int, float):
    """Given any proper versioned string (see comment on top of this module), converts it into tuple of (major, minor.micro)"""

    # example: '1'
    if "." not in ver:
        if "+" not in ver:
            return int(ver), 0.0                                         # '1'
        return int(ver.replace("+", "")), 99999.99999                    # '1+'
    # example: '1.1', '1.1b'
    if ver.count(".") == 1:
        parts = ver.split(".")
        if parts[1] == "+":                                              # '1.+'
            return int(parts[0]), 99999.99999
        if any(not char.isdigit() for char in parts[1]):                 # '1.1b'/'1.1+'
            chars = re.sub("[0-9]+", "", parts[1])
            nums  = re.sub("[^0-9]", "", parts[1])
            if chars != "+":
                return int(parts[0]), float(f"{nums}.{ord(chars) - 97}") # '1.1b'
            return int(parts[0]), float(f"{nums}.{99999}")               # '1.1+'
        else:                                                            # '1.1'
            return int(parts[0]), float(parts[1])
    # example: '1.1.1'
    if ver.count(".") == 2:
        parts = ver.split(".")
        if parts[2] != "+":                                              # '1.1.1'
            return int(parts[0]), float(f"{parts[1]}.{parts[2]}")
        return int(parts[0]), float(f"{parts[1]}.{99999}")               # '1.1.+'
    else:
        log.error(f"Couldn't parse version requirement due to not supported format. Supported formats: [n], [n.n], [n.nx], [n.n.n]. Legend: n - digit, x - latin letter. Parsed literal value: {ver}")
        return 0, 0.0

def analyseVersion(req: (int, float), orig: (int, float), req_max: (int, float) = None) -> bool:
    """Analyses whether required version or require range of versions are met. Uses unified version of (int, float) tuple"""
    def flt(f: float) -> int: # helps reaching only floating part
        return int(f"{f}".split(".")[1])

    if req_max is None: req_max = req
    if not req[0] <= orig[0] <= req_max[0]:
        return False
    if not req[0] < orig[0]: # case: 0.5.0 < 1.4.0 (second is smaller, but first is bigger)
        if not req[1] <= orig[1] <= req_max[1]:
            return False
        if not req[1] < orig[1]: # case: 0.5.5 < 0.6.1 (third is smaller, but second is bigger)
            if not flt(req[1]) <= flt(orig[1]) <= flt(req_max[1]):
                return False
    return True

def getVersion(req_id: str) -> (int, float) or None:
    """Gets version from specific -info.toml- file"""
    info_file = searchInfo(req_id)
    if info_file is None:
        return None
    else:
        if "version" in info_file:
            return unifiedVersion(info_file["version"])
        else:
            return None

def unifiedString(ver: (int, float)) -> str:
    """Returns string of unified version"""
    return f"{ver[0]}.{ver[1]}"