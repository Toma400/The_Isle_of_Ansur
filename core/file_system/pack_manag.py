from core.file_system.repo_manag import file_lister
from core.utils import *
import shutil

#=================|=====================================================================
# PACK MANAGEMENT | Allows for managing packs located in /packs/ directory and contents
#-----------------┘ related to it.
# Allows unzipping mods from /pack/ dir and updating
#=======================================================================================
# Remover of pack's unzipped contents
def pack_remover():
  if not scx("legu"): # checks if Legacy Unpacking isn't used
    non_removable_keys = sysref("vanilla_modules")
    stats_rv = os.listdir(f"{gpath}/stats/"); worlds_rv = os.listdir(f"{gpath}/worlds/")
    scripts_rv = os.listdir(f"{gpath}/scripts/"); scripts_frv = file_lister(f"{gpath}/scripts/")
    def rv(t, tc):
      if os.path.isdir(t) and tc not in non_removable_keys:
        shutil.rmtree(t)

    for i in stats_rv:
      rv(f"{gpath}/stats/{i}", i)
    for i in worlds_rv:
      rv(f"{gpath}/worlds/{i}", i)
    for i in scripts_rv:
      rv(f"{gpath}/scripts/{i}", i)
    for i in scripts_frv:
      os.remove(i)