from core.data.save_system.req_data import REQUIRED_DIRS, REQUIRED_FILES, SV_KIND
from os.path import exists

def verifySave(name: str, variant: SV_KIND = SV_KIND.BUFFER) -> bool:
    sdir = f"saves/{name}/{variant.value}"
    for rd in REQUIRED_DIRS:
        if not exists(f"{sdir}/{rd}"):
            return False
    for rf in REQUIRED_FILES:
        if not exists(f"{sdir}/{rf}"):
            return False
    return True

# TODO:
# ANCITIPATED STRUCTURE
# - {avatars}
# - statistics
#   - attributes.toml
#   - skills.toml
# - inventory
#
# - data.toml
# - {avatar.png}