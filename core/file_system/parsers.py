import yaml, toml, json

#================================================================
# Main parsers
#================================================================
def loadYAML(fpath: str) -> dict | list:
    with open(fpath, encoding="utf-8") as yf:
        ret = yaml.safe_load(yf)
        return ret

def loadTOML(fpath: str) -> dict | list:
    with open(fpath, encoding="utf-8") as yf:
        return toml.loads(yf.read())

def loadJSON(fpath: str) -> dict | list:
    return json.load(fpath)