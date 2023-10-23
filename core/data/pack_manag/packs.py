from core.utils import sysref, scx, developer_mode
from core.gui.manag.langstr import langstring
from glob import glob as walkdir
from enum import Enum
import logging as log
import os

class PackTypes(Enum):
    WORLD_PACK  = "worlds"
    STAT_PACK   = "stats"
    THEME_PACK  = "themes"
    # those are loaded differently, so script below won't work
    # ANY
    # ALL
    # GLOBALPACK

pack_types = [PackTypes.THEME_PACK, PackTypes.STAT_PACK, PackTypes.WORLD_PACK]
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
            for pack in walkdir(f"{pack_type.value}/*/"):
                packs.append(pack.replace(pack_type.value, "").strip(r"\\"))
            ret[pack_type.value] = packs
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

def removePacks():
    exclude = ["endermans_journey", "eternal_desert", "tamriel_races"] + sysref("vanilla_modules") # excluded folders
    excludf = ["example_script.py", "guide.toml"]                                                  # excluded files
    dirs    = ["stats", "worlds", "themes", "scripts"]
    if not scx("legu"):
        import shutil

        log.debug(f"Performing clearing of pack files. Excluded pack IDs: {exclude} | Excluded files: {excludf}")
        for sdir in dirs:
            # Faster implementation, but more verbose (os.walk usage) // can use Nim in case this gets rough as well
            #
            # for _, dirs, files in os.walk(f"{sdir}/"):
            #     for bfile in files:
            #         if bfile not in excludf:
            #             try:
            #                 if developer_mode:
            #                     log.debug(f"Removing: {sdir}/{bfile}")
            #                 os.remove(f"{sdir}/{bfile}")
            #             except:
            #                 if developer_mode:
            #                     log.error(f"Couldn't remove {sdir}/{bfile} due to error:", exc_info=True)
            #     for bdir in dirs:
            #         if bdir not in exclude:
            #             try:
            #                 if developer_mode:
            #                     log.debug(f"Removing: {sdir}/{bdir}")
            #                 shutil.rmtree(f"{sdir}/{bdir}")
            #             except:
            #                 if developer_mode:
            #                     log.error(f"Couldn't remove {sdir}/{bdir} due to error:", exc_info=True)

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