from core.data.save_system.req_data import SV_KIND
from core.data.player.origin import getOrigin
from core.file_system.parsers import loadTOML
from os.path import exists
import toml

def updatePlayer(name: str, data: dict = None):

    player_data = {
        "location": None
    }

    player_keys = player_data.keys()
    if exists(f"saves/{name}/{SV_KIND.BUFFER.value}/player.toml"):
        get      = loadTOML(f"saves/{name}/{SV_KIND.BUFFER.value}/player.toml")
        get_keys = get.keys()
        for line in player_keys:
            if line not in get_keys:
                raise KeyError(f"Saved -data.toml- for character: {name} do not contain required key: {line}. Save is either corrupted or needs patch.")
        player_data = get

    # direct handling of `data`
    if data is not None:
        # no need for error check, because if `getc` fails, None is checked later
        player_data["location"] = getOrigin(data["origin"]).getc("new_game", "location")

    # verification
    for player_key in player_keys:
        if player_data[player_key] is None:
            raise KeyError(f"Provided -data- is None: {player_key}")

    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/player.toml", "w") as f:
        toml.dump(player_data, f)
        f.flush()