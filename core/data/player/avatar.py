from PIL import Image
import os

temp_folder = "_temp/img/avatar/tmp" # without extension

def urlAvatar(url: str) -> bool:
    import requests

    def getExt() -> str | None:
        cfs = [".png", ".jpg", ".webp"]
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
    os.makedirs(temp_folder.strip("tmp"), exist_ok=True)

    for ext in [".png", ".jpg"]:
        if pth.endswith(ext):
            cv = Image.open(f'{pth}')
            cv.save(f"{temp_folder}.png")
            return True
    return False

def saveAvatar(name: str) -> bool:
    if os.path.exists(f"{temp_folder}.png"):
        av_copy = Image.open(f"{temp_folder}.png")
        av_copy.save(f"saves/{name}/buffer/avatar.png")
        return True
    return False

# def packAvatar(rid: str, gid: str) -> list[str]:
#     race_pack, race_id = rid.split(":")
#     _, gender_id = gid.split(":")
#     file = f"stats/{race_pack}/assets/avatars/{gender_id}__{race_id}.jpg"
#     # - format should be found
#     # - genders SHOULD ALSO USE _, so PACK ID!
