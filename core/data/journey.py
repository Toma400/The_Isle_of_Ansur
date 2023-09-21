from core.data.player.gender import Gender
import logging as log
import os

class Journey:

    def __init__(self):
        # character creation stages finished
        #                           [gender, race, class, name, points]
        #                                                             [religion, origin]
        #                                                                          [settings, summary]
        self.stages  : list[bool]  = [False, False, False, False, False, False, False, False, False]
        self.stage   : int or None = None # selected stage of stages where we are at
        self.name    : str or None = None # only none when game not loaded/character not created
        self.inidata : dict        = {} # dict held only during initial creation (used for -self.init-)
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
        self.inidata[stat] = value

    def validateInit(self):
        # keys that are iterated over during save | -inidata- keys should match TOML keys
        keys_saved = ["gender"]
        for k in keys_saved:
            if k not in self.inidata:
                log.log(log.ERROR, f"Couldn't find {k} in -inidata- dictionary. Printing dictionary contents:")
                for entry, value in self.inidata:
                    log.log(log.INFO, f"- {entry}: {value}")

    def init(self):
        """Initial buffer save, run once when character is created. Single use of -self.inidata-"""
        self.validateInit() # checks if all keys are in -inidata-
        ret = "" # initial string : followed by next lines appended below:
        ret += f"gender = {self.inidata['gender']}" + "\n"
        with open(f"{self.buffdir}/main.toml", "r+") as f:
            f.write(ret)

    #=================================================================================================
    # - TODO -
    #=================================================================================================
    def readBank(self, bank_name: str):
        """Example of Journey-related system that awaits implementation"""