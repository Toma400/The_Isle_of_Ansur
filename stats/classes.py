class undefined:
  descript = "Undefined"
  atr_charisma = 1

class fighter:
  descript = "Figter"
  abil_shortswords = 1
  abil_longswords = 1
  abil_archery = 1
  abil_firearms = -1
  abil_archery = -1

class archer:
  descript = "Archer"
  abil_archery = 1
  abil_sneaking = 1
  abil_toughness = -1

class gunslinger:
  descript = "Gunslinger"
  pwr_tech = 5
  pwr_magic = -5
  abil_firearms = 2
  abil_repair = 1
  abil_castspelling = -2

class mage:
  descript = "Regular Mage"
  pwr_magic = 5
  pwr_tech = -5
  abil_castspelling = 2
  abil_healing = 1
  abil_firearms = -2

class trader:
  descript = "Trader"
  abil_trade = 2
  abil_toughness = -1

class rogue:
  descript = "Rogue"
  abil_sneaking = 1
  abil_lockpicking = 1
  abil_toughness = -2

class assassin:
  descript = "Assassin"
  abil_sneaking = 1
  abil_shortswords = 1
  abil_toughness = -2
  perk_assassin_hit = True

class mechanic:
  descript = "Mechanic"
  pwr_tech = 15
  pwr_magic = -15
  abil_repair = 2
  abil_smithery = 1
  abil_castspelling = -2
  perk_vehicle_driving = True

class outlander:
  descript = "Outlander"
  atr_charisma = -1
  abil_repair = 1
  abil_survival = 1
  abil_trapspotting = 1
  abil_healing = 1
  abil_persuasion = -1

class necromant:
  descript = "Necromant"
  pwr_void = 8
  pwr_conn = -20
  pwr_tech = -5
  pwr_magic = 5
  abil_necromancy = 2
  abil_destruction_magic = 1
  abil_firearms = -2

class healer:
  descript = "Healer Mage"
  pwr_magic = 5
  pwr_tech = -5
  abil_restoration_magic = 2
  abil_herbalism = 1
  abil_firearms = -2

class illusionist:
  descript = "Illusionist"
  pwr_magic = 5
  pwr_tech = -5
  abil_transformation_magic = 2
  abil_firearms = -2

class ormath_shaman:
  descript = "Ormath Shaman"
  pwr_conn = 10
  pwr_chaos = -10
  abil_connection = 2
  abil_herbalism = 1
  abil_firearms = -2