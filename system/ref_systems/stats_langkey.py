vals = {
    # ATTRIBUTES
    'atr_charisma':               "stat__atr_charisma",
    'atr_dexterity':              "stat__atr_agility",
    'atr_endurance':              "stat__atr_endurance",
    'atr_intelligence':           "stat__atr_intelligence",
    'atr_strength':               "stat__atr_strength",

    # SKILLS
    'abil_shortswords':           "stat__sk_shortswords",
    'abil_longswords':            "stat__sk_longswords",
    'abil_archery':               "stat__sk_archery",
    'abil_firearms':              "stat__sk_firearms",
    'abil_castspelling':          "stat__sk_castspelling",
    'abil_restoration_magic':     "stat__sk_restoration",
    'abil_transformation_magic':  "stat__sk_transformation",
    'abil_destruction_magic':     "stat__sk_destruction",
    'abil_necromancy':            "stat__sk_necromancy",
    'abil_connection':            "stat__sk_connection",
    'abil_trade':                 "stat__sk_trade",
    'abil_persuasion':            "stat__sk_persuasion",
    'abil_musicality':            "stat__sk_musicality",
    'abil_repair':                "stat__sk_repair",
    'abil_traps':                 "stat__sk_traps",
    'abil_resource_processing':   "stat__sk_resources",
    'abil_tools':                 "stat__sk_tools",
    'abil_smithery':              "stat__sk_smithery",
    'abil_herbalism':             "stat__sk_herbalism",
    'abil_alchemy':               "stat__sk_alchemy",
    'abil_lockpicking':           "stat__sk_lockpicking",
    'abil_sneaking':              "stat__sk_sneaking",
    'abil_trapspotting':          "stat__sk_trapspotting",
    'abil_pickpocketing':         "stat__sk_pickpocketing",
    'abil_healing':               "stat__sk_healing",
    'abil_cooking':               "stat__sk_cooking",
    'abil_survival':              "stat__sk_survival",
    'abil_toughness':             "stat__sk_toughness",

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

    # UNUSED PERKS
    'perk_step_on_water':         "stat__perk_step_on_water",
    'perk_flying_monk':           "stat__perk_flying_monk",
    'perk_stheyr':                "stat__perk_stheyr",
    'perk_body_eating':           "stat__perk_body_eating",
    'perk_undead':                "stat__perk_undead",
    'perk_vampirism':             "stat__perk_vampirism",
}

def get_lkey (statname: str = None):
    if statname is None:
        return vals
    else:
        return vals[statname]