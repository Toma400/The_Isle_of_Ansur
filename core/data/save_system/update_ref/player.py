from core.data.save_system.req_data import SV_KIND
from core.data.player.origin import getOrigin
from core.file_system.parsers import loadTOML
from os.path import exists
import toml

def updatePlayer(name: str, data: dict = None):

    player_data = {
        "location":   None,
        "time_era":   None,
        "time_year":  None,
        "time_month": None,
        "time_day":   None,
        "time_wday":  None,
        "time_hour":  None,
        "time_min":   None,
        "religion":   None,
        "history":    None
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
        time = getOrigin(data["origin"]).getc("new_game", "time")

        player_data["location"]   = getOrigin(data["origin"]).getc("new_game", "location")
        player_data["time_era"]   = time[0]
        player_data["time_year"]  = time[1]
        player_data["time_month"] = time[2]
        player_data["time_day"]   = time[3]
        player_data["time_wday"]  = time[4]
        player_data["time_hour"]  = time[5]
        player_data["time_min"]   = time[6]
        player_data["religion"]   = data["religion"]
        player_data["history"]    = data["history"]

    # verification
    for player_key in player_keys:
        if player_data[player_key] is None:
            raise KeyError(f"Provided -data- is None: {player_key}")

    with open(f"saves/{name}/{SV_KIND.BUFFER.value}/player.toml", "w", encoding="utf8") as f:
        toml.dump(player_data, f)
        f.flush()