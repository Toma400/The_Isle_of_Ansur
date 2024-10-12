import yaml, toml, json

#================================================================
# Main parsers
#================================================================
def loadYAML(fpath: str) -> dict | list:
    with open(fpath, encoding="utf-8") as yf:
        ret = yaml.safe_load(yf)
        return ret

def writeYAML(fpath: str, fcont: any):
    with open(fpath, mode="w", encoding="utf-8") as yf:
        yaml.safe_dump(fcont, yf)
        yf.flush()

def loadTOML(fpath: str) -> dict | list:
    with open(fpath, encoding="utf-8") as tf:
        return toml.loads(tf.read())

def writeTOML(fpath: str, fcont: any):
    with open(fpath, mode="w", encoding="utf-8") as tf:
        toml.dump(fcont, tf)
        tf.flush()

def loadJSON(fpath: str) -> dict | list:
    with open(fpath, encoding="utf-8") as jf:
        return json.loads(jf.read())