from core.data.save_system.req_data import SV_KIND
from core.file_system.parsers import loadTOML
from os.path import exists
import toml

def updateData(name: str, data: dict = None):
    data_file = {
        "name":     None,
        "gender":   None,
        "race":     None,
        "class":    None,
        "origin":   None
    }

    data_keys = data_file.keys()

    if exists(f"saves/{name}/{SV_KIND.BUFFER.value}/data.toml"):
        get      = loadTOML(f"saves/{name}/{SV_KIND.BUFFER.value}/data.toml")
        get_keys = get.keys()
        for line in data_keys:
            if line not in get_keys:
                raise KeyError(f"Saved -data.toml- for character: {name} do not contain required key: {line}. Save is either corrupted or needs patch.")
        data_file = get

    for data_key in data_keys:
        if data is not None:
            if data_key in data:
                data_file[data_key] = data[data_key]
            else:
                raise KeyError(f"Provided -data- does not contain key {data_key} even though it is required by -data_file-. Printing data:\n{data}")

        if data_file[data_key] is None:
            raise KeyError(f"Provided -data- is None: {data_key}")

    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/data.toml", "w", encoding="utf8") as f:
        toml.dump(data_file, f)
        f.flush()