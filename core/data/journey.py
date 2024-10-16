from core.data.save_system.verify import SaveVerifier
from core.data.world.time import BaeTime
from core.data.player.origin import getOrigin
import os, toml, yaml, json
from os.path import exists
import logging as log
from enum import Enum

class SaveStr(Enum):
    """
    Format:
    `[path to file][ | symbol with space around][key]
    Example:
    `player.toml | location`
    """
    LOCATION = "player.toml | location"
    T_ERA    = "player.toml | time_era"
    T_YEAR   = "player.toml | time_year"
    T_MONTH  = "player.toml | time_month"
    T_DAY    = "player.toml | time_day"
    T_WDAY   = "player.toml | time_wday"
    T_HOUR   = "player.toml | time_hour"
    T_MIN    = "player.toml | time_min"
    GENDER   = "data.toml | gender"
    RACE     = "data.toml | race"
    CLASS    = "data.toml | class"
    ORIGIN   = "data.toml | origin"
    MODS     = "mods.toml"
    ATTRS    = "statistics/attributes.yaml"
    SKILLS   = "statistics/skills.yaml"

class Journey:
    # keys that are iterated over during save | -inidata- keys should match TOML keys
    keys_saved = ["gender", "race", "class", "name", "attr", "skill", "religion", "origin", "history", "settings"]

    def __init__(self):
        # character creation stages finished
        #                           [gender, race, class, name, points]
        #                                                             [religion, origin]
        #                                                                          [settings, summary]
        self.stages   : list[bool]  = [False, False, False, False, False, False, False, False, False]
        self.stage    : int or None     = None                         # selected stage of -stages- (above)
        self.name     : str or None     = None                         # only none when game not loaded/character not created
        self.location : str or None     = None                         # only none before load/creating character
        self.date     : BaeTime or None = None                         #            - ... -
        self.inidata  : dict            = {k: "" for k in self.keys_saved} # dict held only during initial creation (used for -self.init-)
        self.settings : dict            = {"permadeath": False}            # dict holding default game settings
        # technical
        self.verify : SaveVerifier or None = None

    def get(self, save_string: str) -> str | int | float | list | dict:
        """Allows for quick data gathering from save files. Operates on `save_string` format.

        String as `save_string` type should be held, because it makes this system more flexible
        (scripts can use it for non-enum-counted elements)
        """
        save_string_parsed = save_string.split(" | ") if "|" in save_string else [save_string, None]
        save_string_format = save_string_parsed[0].split(".")[1]
        parsed_file        = None

        if exists(f"saves/{self.name}/buffer/{save_string_parsed[0]}"):
            loaded_file = open(f"saves/{self.name}/buffer/{save_string_parsed[0]}", encoding="utf-8")

            match save_string_format:
                case "yaml": parsed_file = yaml.safe_load(loaded_file)
                case "toml": parsed_file = toml.loads(loaded_file.read())
                case "json": parsed_file = json.loads(loaded_file.read())

            loaded_file.close()

        if parsed_file is not None:
            if save_string_parsed[1] is None:
                return dict(parsed_file)
            elif save_string_parsed[1] in parsed_file:
                return parsed_file[save_string_parsed[1]]
            log.error(f"Couldn't find a key: {save_string_parsed[1]} in file: {save_string_parsed[0]}.")
        else:
            log.error(f"Couldn't reach path: {save_string_parsed[0]} because of incorrect save file.")
        raise ValueError("Issue found during performing -get- operation on savefile through Journey handler. See previous log messages for what caused the error.")

    def set(self, save_string: str, value: str | int | float | dict | list):
        """Allows for quick data setting into save files. Operates on `save_string` format.

        String as `save_string` type should be held, because it makes this system more flexible
        (scripts can use it for non-enum-counted elements)

        TODO: Should also have function that allows writing multiple keys into one file, for performance reasons
        (see - time saving example, it basically needs to open player file 7 times)
        """
        save_string_parsed = save_string.split(" | ") if "|" in save_string else [save_string, None]
        save_string_format = save_string_parsed[0].split(".")[1]
        parsed_file        = None

        if exists(f"saves/{self.name}/buffer/{save_string_parsed[0]}"):
            loaded_file = open(f"saves/{self.name}/buffer/{save_string_parsed[0]}", encoding="utf-8")

            match save_string_format:
                case "yaml": parsed_file = yaml.safe_load(loaded_file)
                case "toml": parsed_file = toml.loads(loaded_file.read())
                case "json": parsed_file = json.loads(loaded_file.read())

            loaded_file.close()

        if parsed_file is not None and save_string_parsed[1] is not None:
            parsed_file[save_string_parsed[1]] = value

            with open(f"saves/{self.name}/buffer/{save_string_parsed[0]}", "w+") as f:
                match save_string_format:
                    case "yaml": yaml.dump(parsed_file, f)
                    case "toml": toml.dump(parsed_file, f)
                    case "json": json.dump(parsed_file, f)
                f.flush()
        else:
            log.error(f"Tried to write data: {value} into file: {save_string_parsed[0]} and key: {save_string_parsed[1]}, but error occurred.")

    def pass_time(self, dt: float):
        if self.date is not None:
            if self.date.incr(dt) is True:
                self.set(SaveStr.T_ERA.value,   self.date.era)
                self.set(SaveStr.T_YEAR.value,  self.date.year)
                self.set(SaveStr.T_MONTH.value, self.date.month)
                self.set(SaveStr.T_DAY.value,   self.date.day)
                self.set(SaveStr.T_WDAY.value,  self.date.wday)
                self.set(SaveStr.T_HOUR.value,  self.date.hour)
                self.set(SaveStr.T_MIN.value,   self.date.min)
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
    def save(self):
        """Creates gamesave from buffer save
        TODO: saveBuffer does kinda this feature already, find usages and see which handling is better
        """

    def load(self):
        """Passes gamesave onto buffer save
        TODO: loadBuffer does kinda this feature already, find usages and see which handling is better
        """

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
    def readLocation(vr: SaveVerifier) -> str:
        """Changed from placeholder origin to saved one - please change it back if needed
           TODO: change buffer to adventure? <- negative, see loading process now taking buffer loaded into consideration"""
        ps = toml.load(f"saves/{vr.name}/{vr.varstr}/player.toml")
        return ps["location"]

    @staticmethod
    def readDate(vr: SaveVerifier) -> list[int, int, int, int, int, int, int]:
        """Made on the same basis readLocation is done, so whatever comment was for function above should apply here
           TODO: change buffer to adventure? <- negative, see loading process now taking buffer loaded into consideration"""
        ps = toml.load(f"saves/{vr.name}/{vr.varstr}/player.toml")
        return [ps["time_era"],
                ps["time_year"],
                ps["time_month"],
                ps["time_day"],
                ps["time_wday"],
                ps["time_hour"],
                ps["time_min"]]

    #=================================================================================================
    # - TODO -
    #=================================================================================================
    def readBank(self, bank_name: str):
        """Example of Journey-related system that awaits implementation"""