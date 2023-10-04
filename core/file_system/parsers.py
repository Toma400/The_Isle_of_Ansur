import yaml, toml, json

#================================================================
# Main parsers
#================================================================
def loadYAML(fpath: str) -> dict | list:
    with open(fpath) as yf:
        ret = yaml.safe_load(yf)
        return ret

def loadTOML(fpath: str) -> dict | list:
    return toml.load(fpath)

def loadJSON(fpath: str) -> dict | list:
    return json.load(fpath)