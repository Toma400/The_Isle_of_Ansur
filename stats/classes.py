class undefined:
  #has bonus for levelling for levels 1-5
  class_id = "ansur:undefined"
  descript = "Undefined"
  atr_charisma = 1

class fighter:
  class_id = "ansur:fighter"
  descript = "Figter"
  abil_shortswords = 1
  abil_longswords = 1
  abil_toughness = 1
  abil_firearms = -1
  abil_archery = -1

class archer:
  class_id = "ansur:archer"
  descript = "Archer"
  abil_archery = 1
  abil_sneaking = 1
  abil_toughness = -1

class gunslinger:
  class_id = "ansur:gunslinger"
  descript = "Gunslinger"
  pwr_tech = 5
  pwr_magic = -5
  abil_firearms = 2
  abil_repair = 1
  abil_castspelling = -2

class mage:
  class_id = "ansur:regular_mage"
  descript = "Regular Mage"
  pwr_magic = 5
  pwr_tech = -5
  abil_castspelling = 2
  abil_healing = 1
  abil_firearms = -2

class trader:
  class_id = "ansur:trader"
  descript = "Trader"
  abil_trade = 2
  abil_persuasion = 1
  abil_toughness = -2
  perk_trader_sight = True

class rogue:
  class_id = "ansur:rogue"
  descript = "Rogue"
  abil_sneaking = 1
  abil_lockpicking = 1
  abil_pickpocketing = 1
  abil_toughness = -2

class assassin:
  class_id = "ansur:assassin"
  descript = "Assassin"
  abil_sneaking = 1
  abil_shortswords = 1
  abil_toughness = -2
  perk_assassin_hit = True

class mechanic:
  class_id = "ansur:mechanic"
  descript = "Mechanic"
  pwr_tech = 15
  pwr_magic = -15
  abil_repair = 2
  abil_smithery = 1
  abil_castspelling = -2
  perk_vehicle_driving = True

class blacksmith:
  class_id = "ansur:blacksmith"
  descript = "Blacksmith"
  abil_repair = 1
  abil_smithery = 1
  abil_resource_processing = 1
  abil_tools = 1
  abil_shortswords = -1
  abil_longswords = -1
  abil_archery = -1

class outlander:
  class_id = "ansur:outlander"
  descript = "Outlander"
  atr_charisma = -1
  abil_repair = 1
  abil_survival = 1
  abil_trapspotting = 1
  abil_healing = 1
  abil_persuasion = -1

class necromant:
  class_id = "ansur:necromant"
  descript = "Necromant"
  pwr_void = 8
  pwr_conn = -20
  pwr_tech = -5
  pwr_magic = 5
  abil_necromancy = 2
  abil_destruction_magic = 1
  abil_firearms = -2

class priest:
  class_id = "ansur:priest_mage"
  descript = "Priest"
  pwr_magic = 5
  pwr_tech = -5
  abil_restoration_magic = 2
  abil_herbalism = 1
  abil_firearms = -2

class illusionist:
  class_id = "ansur:illusionist_mage"
  descript = "Illusionist"
  pwr_magic = 5
  pwr_tech = -5
  abil_transformation_magic = 2
  abil_alchemy = 1
  abil_firearms = -2

class ormath_shaman:
  class_id = "ansur:ormath_shaman"
  descript = "Ormath Shaman"
  pwr_conn = 10
  pwr_chaos = -10
  abil_connection = 2
  abil_herbalism = 1
  abil_healing = 1
  abil_firearms = -2