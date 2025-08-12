from core.file_system.parsers import loadYAML, writeYAML
from os.path import exists
import logging as log
import toml

def _getFile(dyn_screen, t_path) -> dict:
    if exists(f"saves/{dyn_screen.journey.name}/buffer/{t_path}"):
        match t_path.split(".")[1]:
            case "yaml":
                return loadYAML(f"saves/{dyn_screen.journey.name}/buffer/{t_path}")
            case "toml":
                return toml.load(f"saves/{dyn_screen.journey.name}/buffer/{t_path}")

def travelScript(dyn_screen, t: str) -> bool | None:
    ts = t.split(" | ")
    t_path = ts[0]
    t_key  = ts[1]
    t_val  = ts[2]
    file   = _getFile(dyn_screen, t_path)

    if file is not None:
        # note: float conversion allows for both ints and floats to work
        t_keys = t_key.split(" |> ")
        result = file
        for k in t_keys:
            result = result[k]
        # parsing process
        if t_val.startswith(r"'") and t_val.startswith(r"'"):
            return str(result) == str(t_val.replace(r"'", ""))
        elif "true" in t_val or "false" in t_val:
            if "!=" in t_val:
                return bool(result) != bool(t_val.replace("!=", ""))
            return bool(result) == bool(t_val.replace("=", "")) # = is optional
        elif "!=" in t_val:
            return float(result) != float(t_val.replace("!=", ""))
        elif ">" in t_val:
            return float(result) > float(t_val.replace(">", ""))
        elif "<" in t_val:
            return float(result) < float(t_val.replace("<", ""))
        else:
            return float(result) == float(t_val.replace("=", "")) # = is optional
    else:
        log.error(f"Couldn't find or read file evoked by parseDestScript with path: saves/{dyn_screen.journey.name}/buffer/{t_path}. Condition script: {t}")
        return None # (should it be changed to False instead? better CTD or keep it silently running? (stability and save keeping vs less error notice?))

def travelScriptEdit(dyn_screen, t: str, mode: 0 | 1):
    """Mode: 0 is `cost`, 1 is `set`"""
    ts = t.split(" | ")
    t_path = ts[0]
    t_key  = ts[1]
    t_val  = ts[2]
    file   = _getFile(dyn_screen, t_path)

    if file is not None:
        t_keys = t_key.split(" |> ")
        if mode == 0: # if cost (0): checks previous value
            try:
                result = file
                for k in t_keys:
                    result = result[k]
                t_val = float(result) - float(t_val) # to add something, use negative values
            except ValueError: log.error(f"Couldn't run TravelScript: {t} | Data conversion error, the base and cost values should be of float or integer types.")

        else: # if set (1): check if value is convertable
            if t_val in ["true", "false"]:
                                   t_val = bool(t_val)
            if "." in t_val:
                try:               t_val = float(t_val)
                except ValueError: pass
            else:
                try:               t_val = int(t_val)
                except ValueError: pass
            # if neither type, `t_val` remains as string

        dict_in = {t_keys[-1]: t_val}
        if len(t_keys) > 1:
            for k in reversed(t_keys[:-1]):
                dict_in = {k: dict_in}
        file.update(dict_in)
        match t_path.split(".")[1]:
            case "toml":
                with open(f"saves/{dyn_screen.journey.name}/buffer/{t_path}", mode="w") as file_out:
                    toml.dump(file, file_out)
            case "yaml":
                writeYAML(f"saves/{dyn_screen.journey.name}/buffer/{t_path}", file)
    else:
        log.error(f"Couldn't find or read file evoked by parseDestScript with path: saves/{dyn_screen.journey.name}/buffer/{t_path}. Edit script: {t} | Mode: {mode}")
        return None # (should it be changed to False instead? better CTD or keep it silently running? (stability and save keeping vs less error notice?))