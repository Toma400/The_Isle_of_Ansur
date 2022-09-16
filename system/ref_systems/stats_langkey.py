vals = {
    # ATTRIBUTES
    'atr_charisma':             "stat__atr_charisma",
    'atr_agility':              "stat__atr_agility",
    'atr_endurance':            "stat__atr_endurance",
    'atr_intelligence':         "stat__atr_intelligence",
    'atr_strength':             "stat__atr_strength",

    # SKILLS
    'sk_handfight':             "stat__sk_handfight",
    'sk_shortswords':           "stat__sk_shortswords",
    'sk_longswords':            "stat__sk_longswords",
    'sk_polearms':              "stat__sk_polearms",
    'sk_archery':               "stat__sk_archery",
    'sk_firearms':              "stat__sk_firearms",
    'sk_spellcasting':          "stat__sk_spellcasting",
    'sk_restoration_magic':     "stat__sk_restoration",
    'sk_transformation_magic':  "stat__sk_transformation",
    'sk_destruction_magic':     "stat__sk_destruction",
    'sk_necromancy':            "stat__sk_necromancy",
    'sk_connection_bond':       "stat__sk_connection",
    'sk_trade':                 "stat__sk_trade",
    'sk_persuasion':            "stat__sk_persuasion",
    'sk_musicality':            "stat__sk_musicality",
    'sk_repair':                "stat__sk_repair",
    'sk_traps':                 "stat__sk_traps",
    'sk_resource_processing':   "stat__sk_resources",
    'sk_tools':                 "stat__sk_tools",
    'sk_smithing':              "stat__sk_smithing",
    'sk_herbalism':             "stat__sk_herbalism",
    'sk_alchemy':               "stat__sk_alchemy",
    'sk_lockpicking':           "stat__sk_lockpicking",
    'sk_sneaking':              "stat__sk_sneaking",
    'sk_stealing':              "stat__sk_stealing",
    'sk_trapspotting':          "stat__sk_trapspotting",
    'sk_trapdesigning':         "stat__sk_trapdesigning",
    'sk_pickpocketing':         "stat__sk_pickpocketing",
    'sk_healing':               "stat__sk_healing",
    'sk_cooking':               "stat__sk_cooking",
    'sk_survival':              "stat__sk_survival",
    'sk_toughness':             "stat__sk_toughness",

    # GENERAL
    "name":                       "stat__gen_name",
    "gender":                     "stat__gen_gender",
    "location":                   "stat__gen_location",

    # STATS
    'hp':                         "stat__hint_hp",
    'sp':                         "stat__hint_sp",
    'mp':                         "stat__hint_mp",
    'xp':                         "stat__hint_xp",
    'weight':                     "stat__hint_weight",
    'xp_level':                   "stat__hint_xp_required",
    'level':                      "stat__hint_level",
    'pwr_tech':                   "stat__hint_pwr_tech",
    'pwr_magic':                  "stat__hint_pwr_magic",
    'pwr_conn':                   "stat__hint_pwr_conn",
    'pwr_void':                   "stat__hint_pwr_void",
    'spec_diamond':               "stat__hint_pwm_diamond",
    'spec_moon':                  "stat__hint_pwm_moon",
    'armour':                     "stat__hint_armour",

    # PERKS
    'perk_assassin_hit':          "stat__perk_assassin_hit",
    'perk_trader_sight':          "stat__perk_trader_sight",
    'perk_vehicle_driving':       "stat__perk_vehicle_driving",
    'perk_toxin_immunity':        "stat__perk_toxin_immunity",
    'perk_animal_friend':         "stat__perk_animal_friend",
    'perk_animal_trainer':        "stat__perk_animal_trainer",
    'perk_berserk':               "stat__perk_berserk_tongue",
    'perk_step_on_water':         "stat__perk_step_on_water",
    'perk_flying_monk':           "stat__perk_flying_monk",
    'perk_vampirism':             "stat__perk_vampirism",
    'perk_ritual_tongue':         "stat__perk_ritual_tongue",
    'perk_ancient_tongue':        "stat__perk_ancient_tongue"
}

def get_lkey (statname: str = None):
    if statname is None:
        return vals
    else:
        return vals[statname]