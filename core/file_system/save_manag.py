from glob import glob as walkdir

def listSaves(pgui: bool = True) -> list[str] | list[(str, str)]:
    ret = []
    for save in walkdir("saves/*/"):
        if pgui: # sets compatibility with tuple-based PyGameGUI
            ret.append((save.replace("saves", "").strip(r"\\"), save.replace("saves", "").strip(r"\\")))
        else:
            ret.append(save.replace("saves", "").strip(r"\\"))
    return ret