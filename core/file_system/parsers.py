import yaml, toml, json

#================================================================
# Main parsers
#================================================================
def loadYAML(fpath: str) -> dict | list:
    with open(fpath, encoding="utf-8") as yf:
        ret = yaml.safe_load(yf)
        return ret

def loadTOML(fpath: str) -> dict | list:
    with open(fpath, encoding="utf-8") as tf:
        return toml.loads(tf.read())

def loadJSON(fpath: str) -> dict | list:
    with open(fpath, encoding="utf-8") as jf:
        return json.loads(jf)