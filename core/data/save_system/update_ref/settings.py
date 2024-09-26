from core.data.save_system.req_data import SV_KIND
from core.file_system.parsers import loadTOML
from os.path import exists
import toml

def updateSettings(name: str, data: dict = None):

    sett_data = {
        "permadeath": None
    }

    sett_keys = sett_data.keys()

    if exists(f"saves/{name}/{SV_KIND.BUFFER.value}/settings.toml"):
        get = loadTOML(f"saves/{name}/{SV_KIND.BUFFER.value}/settings.toml")
        get_keys = get["settings"].keys()
        for line in sett_keys:
            if line not in get_keys:
                raise KeyError(
                    f"Saved -settings.toml- for character: {name} do not contain required key: {line}. Save is either corrupted or needs patch.")
        sett_data = get

    for sett_key in sett_keys:
        if data is not None:
            if sett_key in data["settings"]:
                sett_data[sett_key] = data["settings"][sett_key]
            else:
                raise KeyError(
                    f"Provided -settings- does not contain key {sett_key} even though it is required by -sett_data-. Printing data:\n{data}")

        if sett_data[sett_key] is None:
            raise KeyError(f"Provided -settings- is None: {sett_key}")

    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/settings.toml", "w", encoding="utf8") as f:
        toml.dump(sett_data, f)
        f.flush()