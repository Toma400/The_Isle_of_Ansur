from core.data.player.gender import Gender, getGenders
from core.data.player.race import Race, getRaces
from core.utils import sysref
import logging as log
import os

class Journey:
    # keys that are iterated over during save | -inidata- keys should match TOML keys
    keys_saved = ["gender", "race", "class", "name", "attr", "skill", "religion", "origin", "history", "settings"]

    def __init__(self):
        # character creation stages finished
        #                           [gender, race, class, name, points]
        #                                                             [religion, origin]
        #                                                                          [settings, summary]
        self.stages   : list[bool]  = [False, False, False, False, False, False, False, False, False]
        self.stage    : int or None = None                             # selected stage of -stages- (above)
        self.name     : str or None = None                             # only none when game not loaded/character not created
        self.inidata  : dict        = {k: "" for k in self.keys_saved} # dict held only during initial creation (used for -self.init-)
        self.settings : dict        = {"permadeath": False}            # dict holding default game settings
        # PATHS
        self.buffdir  : str = f"saves/{self.name}/buffer"    # buffer save
        self.savedir  : str = f"saves/{self.name}/adventure" # adventure save (manual)
        self.cycledir : str = f"saves/{self.name}/cycle"     # cyclic save (autosave) -- WIP
        self.arenadir : str = f"saves/{self.name}/arena"     # arena save (multiplayer)

    #=================================================================================================
    # - COMMON PROCEDURES -
    # Procedures used during the game on regular basis.
    #=================================================================================================
    # procedural/object-oriented balance
    # - would require 'name' as identifier (str|None) for data gathering
    # - would use 'stages' for newly created player and/or loading data (so it can be used to validate both kinds of Player creating)
    # - the only system it'd use is readValue/writeValue which would then exchange values with saved files
    #   (could be expanded for different files tho, so 'readValue' could be 'readStatistics' as opposed to 'readChests' for example)
    #                                                        (as chests were considered as different savefile entity for statistics)
    # - in the future, cache browsing could be introduced, that would have certain threshold, but would first search through this
    #   "object pool" and if it doesn't find anything there, it'd make this regular loading process of data
    def readStats(self, stat: str):
        """Reads statistics value from buffer save (not save!)"""

    def updateStats(self, stat: str, value: str | int | bool | list):
        """Allows changing statistics by overwriting buffer save"""

    def save(self):
        """Creates gamesave from buffer save"""

    def load(self):
        """Passes gamesave onto buffer save"""

    #=================================================================================================
    # - INIT STAGE -
    # Run only during character creation, before proper save files are made.
    # Use -setInit- to build -inidata- dictionary and finish by using -init- which makes buffer save.
    #=================================================================================================
    def setInit(self, stat: str, value: str | int | bool | list):
        """Used only during character creation, fills dict with statistics for initial save (later save is used instead)"""
        if stat in self.keys_saved:
            self.inidata[stat] = value
        else: raise KeyError(f"Attempted to write incorrect key: {stat} into -inidata-")

    def validateInit(self):
        for k in self.keys_saved:
            if k not in self.inidata:
                log.log(log.ERROR, f"Couldn't find {k} in -inidata- dictionary. Printing dictionary contents:")
                for entry, value in self.inidata:
                    log.log(log.INFO, f"- {entry}: {value}")
                raise KeyError("Raising crash due to the issue above.")

    def init(self):
        """Initial buffer save, run once when character is created. Single use of -self.inidata-"""
        # TODO: IMPORTANT
        # This piece is saving into `presave` which needs to be yet reloaded and redistributed
        # - in the future, stats should be separate from 'history' being its own TOML file
        # - samely, there will be statistics as hardcoded numbers
        # - currently, there is no redistribution of numbers (class+race+manual) for stats
        #   so things can change if pre-alpha 4 changes statistics
        # - once game is started, those should be evaluated once and then not change unless
        #   it was meant to change by gameplay (but not overall stat changes), like training
        # - in short: this is not proper save, it should be redone to be split onto multiple files
        #   and have better structure
        # - ! This way no migration software will be required, or if it will be, it should work
        #   only once or so
        self.name = self.inidata["name"]
        self.validateInit() # checks if all keys are in -inidata-
        ret = "" # initial string : followed by next lines appended below:
        # ret += f"save_ver = {sysref('release_status')}:{sysref('release_version')}" + "\n"
        # ^ this will be useful once proper save is used, now we can just simply check 'is presave.toml existing'
        ret += f"name     = {self.inidata['name']}"     + "\n"
        ret += f"gender   = {self.inidata['gender']}"   + "\n"
        ret += f"race     = {self.inidata['race']}"     + "\n"
        ret += f"class    = {self.inidata['class']}"    + "\n"
        ret += f"religion = {self.inidata['religion']}" + "\n"
        ret += f"origin   = {self.inidata['origin']}"   + "\n"
        ret += f"attr     = {self.inidata['attr']}"     + "\n" #
        ret += f"skill    = {self.inidata['skill']}"    + "\n" #
        ret += f"history  = \'\'\'"                     + "\n"
        ret += f"{self.inidata['history']}"             + "\n"
        ret += f"\'\'\'"                                + "\n"
        # level, xp and all that should be put when TODO is done, alongside banks, chests and inventory
        with open(f"{self.buffdir}/presave.toml", "r+") as f:
            f.write(ret)

    #=================================================================================================
    # - TODO -
    #=================================================================================================
    def readBank(self, bank_name: str):
        """Example of Journey-related system that awaits implementation"""