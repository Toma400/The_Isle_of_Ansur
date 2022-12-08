#temporary .py file, just to list all variables that will be needed in RPG system
from core.utils import sysref

class profile:

  def settings_checker(setting):
    import system.settings
    i = system.settings.settings(setting)
    return i

  #stats that are set either by player or game itself \
  not_default_stats = {
    "openable":              True,
    "nuid":                    "", #nuid
    "name":                    "",
    "nuid_key":                "", #nuid+#+name
    "gender":                  "",
    "race":                    "", #rid
    "class":                   "", #cid
    "location": "ansur:beginning", #wid
    "time_day":                 1, #distance from default value (3.10.921 NE); time_day changes drastically if realistic time mode is set
    "time_hour":                1, #value of 1-1440
    "world_tick":               1, #each turn made by player
  }
  
  general_stats = {
    'hp':             100, #amount of hp
    'sp':            1000, #amount of sp (1000 is max)
    'mp':             100, #amount of mp
    'xp':               0, #amount of xp
    'weight':           0, #carried weight
    'hp_level':       100, #max amount of hp (hp/hp_level)
    "mp_level":       100, #max amount of mp (mp/mp_level)
    'xp_level':       100, #xp needed for another level (changeable after each level up)
    'max_weight':      24, #max weight (weight/max_weight)
    'level':            1, #level of the person
    'pwr_tech':         0, #forces (tech/magic/connection/void)
    'pwr_magic':        0,
    'pwr_conn':         0,
    'pwr_void':         0,
    'spec_diamond': False,
    'spec_moon':    False,
    'armour':           0,
  }

  #all attributes are 8 by default
  attributes = {
    'atr_charisma':     8,
    'atr_agility':      8,
    'atr_endurance':    8,
    'atr_intelligence': 8,
    'atr_strength':     8
  }

  skills = {
    'sk_handfight':            1, #positive by default
    'sk_shortswords':          1, #positive by default
    'sk_longswords':           0,
    'sk_polearms':             0,
    'sk_archery':              1, #positive by default
    'sk_firearms':             0,
    'sk_spellcasting':         0,
    'sk_restoration_magic':    0,
    'sk_transformation_magic': 0,
    'sk_destruction_magic':    0,
    'sk_necromancy':           0, #no creative change
    'sk_connection_bond':      0, #no creative change
    'sk_trade':                1, #positive by default
    'sk_persuasion':           1, #positive by default
    'sk_musicality':           0,
    'sk_repair':               0,
    'sk_traps':                0,
    'sk_resource_processing':  0,
    'sk_tools':                0,
    'sk_smithing':             0,
    'sk_herbalism':            0,
    'sk_alchemy':              0,
    'sk_lockpicking':          0,
    'sk_sneaking':             0,
    'sk_stealing':             0,
    'sk_trapdesigning':        0,
    'sk_trapspotting':         0,
    'sk_pickpocketing':        0,
    'sk_healing':              0,
    'sk_cooking':              0,
    'sk_survival':             0,
    'sk_toughness':            0
  }

  perks = {
    'perk_assassin_hit':    False,
    'perk_trader_sight':    False,
    'perk_vehicle_driving': False,
    'perk_toxin_immunity':  False,
    'perk_animal_friend':   False,
    'perk_animal_trainer':  False,
    'perk_berserk':         False,
    'perk_step_on_water':   False,
    'perk_flying_monk':     False,
    'perk_vampirism':       False,
    'perk_ritual_tongue':   False,
    'perk_ancient_tongue':  False
  }

  settings = {
    "save_system":   f"{sysref('save_system')}",
    "time_system":   settings_checker("time_system"),
    "hunger_thirst": settings_checker("hunger_thirst"),
    "permadeath":    settings_checker("permadeath"),
    "saved_on_day":  "",
    "saved_on_hour": ""
  }

  unused_perks = {
    'perk_stheyr':      False,
    'perk_body_eating': False,
    'perk_undead':      False,
  }

class quests:
  #for both quests.json and finished_quests.json

  quests = {}
  #quests are using syntax - qid : status, with True meaning being done (for example - "ansur:welcome" : True)
  mod_quests = {}
  #"mod" is for any additional workspace; in fact, it should be "for N in DIR[worlds]: create new dict with WORKSPACE_quests"
  #in .json they will be set as different object

class inventory:

  main_slots = {
    "inventory":        {},
    "slot_main":        {},
    "slot_alternative": {},
    "slot_helmet":      {},
    "slot_chestplate":  {},
    "slot_leggings":    {},
    "slot_boots":       {},
    "slot_necklace":    {},
    "slot_cape":        {},
    "slot_ring":        {},
    "slot_ring2":       {},
    "slot_ring3":       {}
  }