from core.data.player.gender import Gender, getGenders
from core.data.player.race import Race, getRaces
from core.data.player.origin import getOrigin
from core.data.pack_manag.packs import getPacks
from core.data.save_system.update import updateSave
from core.utils import sysref
import logging as log
import os, toml

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
        self.location : str or None = None                             # only none before load/creating character
        self.inidata  : dict        = {k: "" for k in self.keys_saved} # dict held only during initial creation (used for -self.init-)
        self.settings : dict        = {"permadeath": False}            # dict holding default game settings
        # technical
        self.verify   : bool        = False

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

    def reset(self):
        """
        Resets values, should be used after init() or quitting the game when, for example, coming back to menu
        It allows for cleaner checks, during load for example: skips issue where load has issues right after creating character,
        or potentially when you want to load the same game you just saved
        """
        self.__init__()

    @staticmethod
    def readLocation(name: str) -> str:
        """Temporary placeholder function"""
        ps = toml.load(f"saves/{name}/buffer/data.toml")
        return getOrigin(ps["origin"]).getc("new_game", "location")

    #=================================================================================================
    # - TODO -
    #=================================================================================================
    def readBank(self, bank_name: str):
        """Example of Journey-related system that awaits implementation"""