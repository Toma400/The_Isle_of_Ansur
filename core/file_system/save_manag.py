from glob import glob as walkdir

def listSaves() -> list[str]:
    ret = []
    for save in walkdir("saves/*/"):
        ret.append(save.replace("saves", "").strip(r"\\"))
    return ret