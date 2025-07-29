from core.file_system.parsers import loadYAML
from os.path import exists
import logging as log
import toml

def travelScript(dyn_screen, t: str) -> bool | None:
    ts = t.split(" | ")
    t_path = ts[0]
    t_key  = ts[1]
    t_val  = ts[2]
    file   = None
    if exists(f"saves/{dyn_screen.journey.name}/buffer/{t_path}"):
        match t_path.split(".")[1]:
            case "yaml":
                file = loadYAML(f"saves/{dyn_screen.journey.name}/buffer/{t_path}")
            case "toml":
                file = toml.load(f"saves/{dyn_screen.journey.name}/buffer/{t_path}")
    if file is not None:
        # note: float conversion allows for both ints and floats to work
        t_keys = t_key.split(" |> ")
        result = file
        for k in t_keys:
            result = result[k]
        if t_val.startswith(r"'") and t_val.startswith(r"'"):
            return str(result) == str(t_val.replace(r"'", ""))
        elif "true" in t_val or "false" in t_val:
            if "!=" in t_val:
                return bool(result) != bool(t_val.replace("!=", ""))
            return bool(result) == bool(t_val.replace("=", "")) # = is optional
        elif ">" in t_val:
            return float(result) > float(t_val.replace(">", ""))
        elif "<" in t_val:
            return float(result) < float(t_val.replace("<", ""))
        else:
            return float(result) == float(t_val.replace("=", "")) # = is optional
    else:
        log.error(f"Couldn't find or read file evoked by parseDestScript with path: saves/{dyn_screen.journey.name}/buffer/{t_path}. Condition script: {t}")
        return None # (should it be changed to False instead? better CTD or keep it silently running? (stability and save keeping vs less error notice?))