from core.data.save_system.req_data import REQUIRED_DIRS, REQUIRED_FILES, SV_KIND
from core.data.pack_manag.info import searchInfo
from core.data.pack_manag.id import zipToID
from core.file_system.parsers import loadTOML, loadYAML
from os.path import exists

class SaveVerifier:

    def __init__(self, name: str):
        # vars to use later
        self.name              = name
        self.variant : SV_KIND = SV_KIND.ADVENTURE
        # vars for organisation
        self.save_structure = self.verifySaveStructure()
        self.mods_versions  = self.verifyModsDependencies() if self.save_structure else (False, {}, {}, {})
        if not self.save_structure or not self.mods_versions: # reading from buffer, in case adventure doesn't work
            self.variant: SV_KIND = SV_KIND.BUFFER
            self.save_structure   = self.verifySaveStructure()
            self.mods_versions    = self.verifyModsDependencies() if self.save_structure else (False, {}, {}, {})
        self.varstr         = self.variant.value # stringified variant, so no SV_KIND import is needed elsewhere (important: use only outside file, it's set at the end)
        # bulk bool for both correctness
        #   later replace with save_structure only, and mods_versions being False should prompt the warning only
        self.correct        = self.save_structure and self.mods_versions[0]

    def verifySaveStructure(self) -> bool:
        sdir = f"saves/{self.name}/{self.variant.value}"
        for rd in REQUIRED_DIRS:
            if not exists(f"{sdir}/{rd}"):
                return False
        for rf in REQUIRED_FILES:
            if not exists(f"{sdir}/{rf}"):
                return False
        return True

    def verifyModsDependencies(self) -> (bool, dict[str, str], dict[str, str], list[str], dict[str, str]):
        """Returns whether every dependency is met, and list of current mods (both required and available)
        Returns tuple of:
            bool           - are all dependencies met?
            dict[str, str] - list of packs required by save [ID, version used during save]
            dict[str, str] - list of currently loaded packs [ID, version available]
            dict[str]      - list of missing packs [ID]
            dict[str, str] - list of incorrect packs [ID, version used during save]
        """

        packs_required = loadTOML(f"saves/{self.name}/{self.variant.value}/mods.toml")
        packs_used     = loadYAML("core/data/pack_manag/pack_order.yaml") if exists("core/data/pack_manag/pack_order.yaml") else []
        everything_ok  = True
        packs_final_rq = {}
        packs_final_in = {}
        packs_final_ms = []
        packs_final_er = {}

        packs_used.append("ansur") # TODO: remove it once 'ansur' becomes its own .zip file

        for pack in packs_used:
            p_info = searchInfo(zipToID(pack))
            p_name = pack
            p_ver  = "0.0.0"
            if p_info is not None:
                if "name" in p_info:
                    p_name = p_info["name"]
                if "version" in p_info:
                    p_ver = p_info["version"]
            packs_final_in[p_name] = p_ver

        for pack, ver in packs_required.items():
            p_info = searchInfo(pack)
            p_name = pack
            if p_info is not None:
                if "name" in p_info:
                    p_name = p_info["name"]
            packs_final_rq[p_name] = ver

            if p_name not in packs_final_in.keys():
                packs_final_ms.append(p_name)
                everything_ok = False
            else:
                if ver != packs_final_in[p_name]:
                    packs_final_er[p_name] = ver

        return everything_ok, packs_final_rq, packs_final_in, packs_final_ms, packs_final_er

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