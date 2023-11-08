from core.file_system.parsers import loadYAML
from core.data.pack_manag.id import absoluteID
from PIL import Image
import os

temp_folder = "_temp/img/avatar/tmp" # without extension

def urlAvatar(url: str) -> bool:
    """Prepares selected URL image entry to save."""
    import requests

    def getExt() -> str | None:
        cfs = [".png", ".jpg", "jpeg", ".webp"]
        for cf in cfs:
            if cf in url:
                return cf
        return None

    req_data = requests.get(url)

    os.makedirs(temp_folder.strip("tmp"), exist_ok=True)

    if req_data.status_code == 200:
        ext = getExt()
        if ext is not None:
            raw = open(f'{temp_folder}{ext}', 'wb')
        else: return False
        raw.write(req_data.content)
        raw.flush()
        raw.close()

        if ext != ".png":
            cv = Image.open(f'{temp_folder}{ext}')
            cv.save(f"{temp_folder}.png")
        return True
    else:
        return False

def pathAvatar(pth: str) -> bool:
    """Prepares selected local image entry to save."""
    os.makedirs(temp_folder.strip("tmp"), exist_ok=True)

    for ext in [".png", ".jpg", ".jpeg"]:
        if pth.endswith(ext):
            cv = Image.open(f'{pth}')
            cv.save(f"{temp_folder}.png")
            return True
    return False

def loreAvatarSelection():
    """Creates _temp file that stores index for currently selected avatar image"""
    os.makedirs(temp_folder.strip("tmp"), exist_ok=True)

    with open(f"{temp_folder}.txt", "x") as isn:
        isn.write("0")
        isn.flush()

def loreAvatars(rid: str, gid: str):
    """Preparation function, should be run once, so it is not included in -loreAvatar-"""
    mod_id, race_uid = rid.split(":")
    rav_path = f"stats/{mod_id}/races/avatars/{race_uid}.yaml"

    avatars = [] # list of shortened paths taken out of JSON
    out     = [] # list of absolute paths being returned

    if os.path.exists(rav_path):
        rjs = loadYAML(rav_path)
        for rjs_key in rjs.keys():
            if absoluteID(rjs_key) == gid:
                avatars = rjs[rjs_key]

    if avatars: # if not empty
        for avatar in avatars:
            out.append(f"stats/{mod_id}/assets/{avatar}")

    os.makedirs(temp_folder.strip("tmp"), exist_ok=True)
    with open(f"{temp_folder}.yaml", "x") as avf:
        for v in out:
            avf.write(f"- {v}\n")

def loreAvatar(avs: list, ix: int) -> bool:
    """Proper picker function. Takes -loreAvatars- as variable & index as second argument. Prepares selected lore image entry to save."""
    os.makedirs(temp_folder.strip("tmp"), exist_ok=True)

    try:
        cv = Image.open(f'{avs[ix]}')
        cv.save(f"{temp_folder}.png")
        return True
    except:
        return False

def saveAvatar(name: str) -> bool:
    """Performs saving of buffered avatar into stable location"""
    os.makedirs(f"saves/{name}/buffer/avatars/", exist_ok=True)

    if os.path.exists(f"{temp_folder}.png"):
        av_copy = Image.open(f"{temp_folder}.png")
        av_copy.save(f"saves/{name}/buffer/avatar.png")
        av_copy.save(f"saves/{name}/buffer/avatars/0.png")
        return True
    return False

# def packAvatar(rid: str, gid: str) -> list[str]:
#     race_pack, race_id = rid.split(":")
#     _, gender_id = gid.split(":")
#     file = f"stats/{race_pack}/assets/avatars/{gender_id}__{race_id}.jpg"
#     # - format should be found
#     # - genders SHOULD ALSO USE _, so PACK ID!
