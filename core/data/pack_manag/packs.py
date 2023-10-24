from core.utils import sysref, scx, developer_mode
from core.gui.manag.langstr import langstring
from core.file_system.parsers import loadTOML
from os.path import exists
from glob import glob as walkdir
from enum import Enum
import logging as log
import re
import os

class PackTypes(Enum):
    WORLD_PACK  = "worlds"
    STAT_PACK   = "stats"
    THEME_PACK  = "themes"
    # those are loaded differently, so script below won't work
    # ANY
    # ALL
    # GLOBALPACK

pack_types = [PackTypes.THEME_PACK.value, PackTypes.STAT_PACK.value, PackTypes.WORLD_PACK.value]
packs      = list(filter(lambda ext: ".zip" in ext, os.listdir("packs/")))

def getScripts() -> list[str]:
    """Returns list of script names (as str value)"""
    ret = []
    for py in walkdir(f"scripts/*.py"):
        with open(py, "r") as pyf:
            if "(ioaScript):" in pyf.read():
                ret.append(py.replace("scripts", "").replace(".py", "").strip(r"\\"))
    return ret

def getPacks(kind: PackTypes = None) -> dict[list[str]] | list[str]:
    """Returns dictionary of pack lists, separated by type, or type if argument is filled"""
    if kind is None:
        ret = {"scripts": getScripts()}
        for pack_type in pack_types:
            packs = []
            for pack in walkdir(f"{pack_type}/*/"):
                packs.append(pack.replace(pack_type, "").strip(r"\\"))
            ret[pack_type] = packs
    else:
        ret = []
        for pack in walkdir(f"{kind.value}/*/"):
            ret.append(pack.replace(kind.value, "").strip(r"\\"))
    return ret

def getPacksSimplified(pack_list: dict[list[str]] = getPacks(), langstr: bool = True) -> dict[list[str]]:
    """Returns dictionary of pack IDs and list of types. Useful for situations where we want to know about connected packs
    - pack_list - list of packs that should be analysed (default: currently loaded ones)
    - langstr   - whether types of packs are raw (enums) or translated (GUI-friendly)
    """
    ret   = {}
    for kind in pack_list.keys():
        if kind != "scripts":
            for pack in pack_list[kind]:
                kindstr = langstring(f"pack__{kind}") if langstr else kind
                if pack in ret:
                    ret[pack] = ret[pack] + [kindstr]
                else:
                    ret[pack] = [kindstr]
    return ret

def getGlobalPacks() -> list[str]:
    """Returns global pack type (which means both types having the same ID)"""
    return [p for p in getPacks(PackTypes.WORLD_PACK) if p in getPacks(PackTypes.STAT_PACK)]

def verifyPacks():
    def unifiedVersion(ver: str) -> (int, float):
        # example: '1'
        if "." not in ver:
            return int(ver), 0.0
        # example: '1.1', '1.1b'
        if ver.count(".") == 1:
            parts = ver.split(".")
            if any(not char.isdigit() for char in parts[1]):             # '1.1b'
                chars = re.sub("[0-9]+", "", parts[1])
                nums  = re.sub("[^0-9]", "", parts[1])
                return int(parts[0]), float(f"{nums}.{ord(chars) - 97}")
            else:                                                        # '1.1'
                return int(parts[0]), float(parts[1])
        # example: '1.1.1'
        if ver.count(".") == 2:
            parts = ver.split(".")
            return int(parts[0]), float(f"{parts[1]}.{parts[2]}")
        else:
            log.error(f"Couldn't parse version requirement due to not supported format. Supported formats: [n], [n.n], [n.nx], [n.n.n]. Legend: n - digit, x - latin letter. Parsed literal value: {ver}")
            return 0, 0.0

    def unifiedString(ver: (int, float)) -> str:
        return f"{ver[0]}.{ver[1]}"

    def analyseVersion(req: (int, float), orig: (int, float), req_max: (int, float) = None) -> bool:
        """Analyses whether required version or require range of versions are met"""
        if req_max is None: req_max = req
        if not req[0] <= orig[0] <= req_max[0]:
            return False
        if not req[0] < orig[0]: # case: 0.5.0 < 1.4.0 (second is smaller, but first is bigger)
            if not req[1] <= orig[1] <= req_max[1]:
                return False
            if not req[1] < orig[1]: # case: 0.5.5 < 0.6.1 (third is smaller, but second is bigger)
                if not req[2] <= orig[2] <= req_max[2]:
                    return False
        return True

    def browseInfo(req_id: str) -> dict | None:
        """Browses through all pack folders to find -info.toml- file"""
        for packkind in pack_types:
            if exists(f"{packkind}/{req_id}/info.toml"):
                return loadTOML(f"{packkind}/{req_id}/info.toml")
        return None

    def getVersion(req_id: str) -> (int, float) or None:
        """Gets version from specific -info.toml- file"""
        info_file = browseInfo(req_id)
        if info_file is None:
            return None
        else:
            if "version" in info_file:
                return unifiedVersion(info_file["version"])
            else:
                return None

    vpack  = getPacksSimplified(getPacks(), langstr=False)
    err_fl = open("core/data/pack_manag/pack_errors.yaml", "w")
    errors = {}
    for packID in vpack.keys():
        errors_pack = []
        pack_info = browseInfo(packID) # PyCharm warn here is stupid, it's 'str', not list
        if pack_info is not None:
            if "requirements" in pack_info.keys():
                for req_pack in pack_info["requirements"].keys():
                    if req_pack in vpack.keys():
                        req_init = pack_info["requirements"][req_pack]
                        if req_init == "": # no specific required version, skipping
                            continue
                        elif "-" in req_init: # ranged requirement ('1.1-1.8')
                            req_spl = req_init.replace(" ", "").split("-")
                            req_fin = [unifiedVersion(req_spl[0]), unifiedVersion(req_spl[1])]
                        elif req_init.startswith("<"): # up to version ('<1.1'), inclusive
                            req_fin = [(0, 0.0),                   unifiedVersion(req_init.replace("<", ""))]
                        elif req_init.startswith(">"): # minimal version ('>1.1'), inclusive
                            req_fin = [unifiedVersion(req_init.replace(">", "")), (99999, 99999.99999)]
                        else:
                            req_fin = [unifiedVersion(req_init),   unifiedVersion(req_init)]
                        # requesting mod's version to check
                        reqs_ver = getVersion(req_id=req_pack)
                        if reqs_ver is None:
                            log.error(f"Couldn't verify {req_pack} version due to either -info.toml- missing or version key not being used.")
                        else:
                            if analyseVersion(req_fin[0], reqs_ver, req_fin[1]) is False:
                                log.critical(f"Version requirement of {packID} for module {req_pack} are not met. Required version: {unifiedString(req_fin[0])}-{unifiedString(req_fin[1])}. Available version: {unifiedString(reqs_ver)}.")
                                errors_pack.append([req_pack, f"{unifiedString(req_fin[0])}-{unifiedString(req_fin[1])}", f"{unifiedString(reqs_ver)}"])
                    else:
                        log.error(f"Couldn't find {req_pack} in")
            # creating error entry if any issues are found
            if len(errors_pack) > 0:
                errors[packID] = errors_pack
    if len(errors.keys()) > 0:
        err_msg = ""
        for mod in errors.keys():
            err_msg += f"{mod}:" + "\n"
            for err in errors[mod]:
                err_msg += f"- {err}" + "\n"
        err_fl.write(err_msg)
    err_fl.flush()
    err_fl.close()

def removePacks():
    """Performs cleaning of pack extraction folders. Used to update packs by simply updating .zip file"""
    exclude = ["endermans_journey", "eternal_desert", "tamriel_races"] + sysref("vanilla_modules") # excluded folders
    excludf = ["example_script.py", "guide.toml"]                                                  # excluded files
    dirs    = ["stats", "worlds", "themes", "scripts"]
    if not scx("legu"):
        import shutil

        if developer_mode:
            log.debug(f"Performing clearing of pack files. Excluded pack IDs: {exclude} | Excluded files: {excludf}")
        for sdir in dirs:
            for thing in os.listdir(f"{sdir}/"):
                if (thing not in exclude) and (thing not in excludf):
                    if developer_mode:
                        log.debug(f"Removing: {sdir}/{thing}")
                    try:
                        if os.path.isdir(f"{sdir}/{thing}"):
                            shutil.rmtree(f"{sdir}/{thing}")
                        else:
                            os.remove(f"{sdir}/{thing}")
                    except:
                        if developer_mode:
                            log.error(f"Couldn't remove {sdir}/{thing} due to error:", exc_info=True)

def unpackPacks():
    """Unpacks .zip files from -packs- folder"""
    def unpacking(zfile, zpack):
        whitelist = ["stat", "world", "theme"]
        for foldername in zfile.namelist():
            for packtype in whitelist:
                if f"{packtype}s" in foldername:
                    zfile.extract(foldername, "")
                    log.debug(f"Unpacking {packtype}pack: {zpack}")
            if "scripts/" in foldername:
                zfile.extract(foldername, "")
                log.debug(f"Unpacking scripts of {zpack}:")
                scripts = zfile.open("scripts/")
                for script in scripts.namelist():
                    log.debug(f"- {script}")

    if len(packs) > 0 and not scx("legu"):
        import zipfile

        log.info("Pack unloading process started...")
        for pack in packs:
            if ".zip" in pack:
                log.info(f"Found pack: {pack}. Unzipping...")
                with zipfile.ZipFile("packs/" + pack, "r") as file:
                    unpacking(file, pack)
                    file.close()