#---------------------------------
#IMPORT RULES
#'manag' modules should rather be left in name, since they make context most visible
#   import system.id_manag as id_manag
#
#Common importing renamings:
#   from utils.colours import bcolors as colour
#   from utils.text import text_align as align

# > import system.int_systems.inv_manag
# > import system.json_manag
# > system.int_systems.inv_manag.del_item ("Terti", "ansur:honey_roll", 2)
# > system.int_systems.inv_manag.add_item ("Terti", "ansur:flour")
# > system.int_systems.inv_manag.iid_checker("Terti", "ansur:short_sword")

#INV TESTING
#import gui.inventory
#gui.inventory.main_inv("Terti")

#FOR THE FUTURE!!!!
#Write here what was the last thing you worked on. What was the issues you found tiring
#Like "WORKED ON X, BUT Y DEMOTIVATED ME"
#--------------------V------------------
#
# Inventory managment iirc, it might be single-stack items Being difficult to manage
# Slot selecting too btw
# ^ slot selecting could be used by binding 'j' from iterator to specific item
# or just using some sort of "find line X of json file", which would also work*
# * - just remember that it starts from line 3
#
# So if player would choose item "1", it would redirect them for 3rd line
# If player choose "5"th item, it will redirect them to 7th line
#---------------------------------------


#---------------------------------
#just trash stuff that i want to keep here for now, just for reference purposes

#print (stats.races.race_saphtri.descript)
#temp_stat = 5 + stats.races.race_saphtri.atr_endurance
#print ("Endurance with penalty: " + str(temp_stat))
{
"landscape": "✺---------------------------------------------------------------✺",
"landscap2": "| Λ Λ Λ Λ Λ Λ                      )                             |",
"landscap3": "| Λ           ░░░░░░░░░░░░░░░░    (         ~~~                  |",
"landscap4": "|Λ  ░░░░░░░░░░░░░░░░░░░  ♖-------♖ )                           |",
"landscap5": "| Λ ░░░░░░░░░░░░░░░░░░░  |  Baedoor ♖)           ~~~            |",
"landscap6": "|Λ  ░░░░░░░░░░░░░░░░░░░  ♖-------♖⚓)                       ✖ |",
"landscap7": "|Λ  ۩  ░░░░░░░░░░░░░░░░           (         ~~~           <_>    |",
"landscap8": "| Λ Λ Λ Λ Λ Λ Λ   Λ ░░░░░░░░░░░░░  )                     Ansur   |",
"landscap9": "✺---------------------------------------------------------------✺"
}

#everything above is total bullshit, it's just for conceptualisation purposes

#SHORTCUT FOR RID MANAGEMENT (OUTPUT: VALUE_NAME -> VALUE)
import system.id_manag
for i in system.id_manag.rid_conv("ansur:baedoorian"):
  print (i + "-> " + str(system.id_manag.rid_conv("ansur:baedoorian", i)))

#POSSIBLE COMPATIBILITY THINGIES:
#character additional_abilities/additional_attributes list can be made into .json and read from there = can be expanded by mods with additional attributes or abilities
#in character.py it will just be loaded to fit their lists used in character creation

#BOOLEAN TRUE IS SET AS =1 IN STATS

#-------------------------------------------------------------------------------
#TODO

# - item load (stats/items.json)
#   - class (weapons, utils2, etc)                      <- "KEY READER"
#   - values of separate items (damage, quality, etc)  <- "VALUE READER"
# - item inventory load (saves/X/inventory.json)
#   - item values                                      
# - inventory management
#   - item add (with general values + ew. crafting dependent on skill)
#   - item remove
#   - item qualities check ("?" prefix before choice)
#   - equip item on respective slot
#   - slot limit (1)
# - interface (main game)

#-------------------------------------------------------------------------------
{
"stackable": False,       #stacking (if no individual qualities given - True)
#individual qualities (general):
"quality": "good",        #depends on a way item is obtained; can't be higher than max
#non-individual (general):
"item_id": "",            #obvious
"descript": "",           #obvious
"category": "",           #type of item (weapon/etc)
"weight": 1,              #how much inventory space is taken
"max_quality": "good",    #max quality that can be obtained by item
"min_price": 3,           #min price for trade
"max_price": 9,           #max price for trade
                          #trading usually goes towards lower prices if sell, and towards higher if bought
#non-individual (weapons):
"type": "shortsword",     #type of weapon (U+ related)
"average_dmg": 4,         #average dmg
"dmg_yaw": 1,             #offset of average (4+yaw1 = 3-5)
"block_chance": 20,       #base percent chance of blocking, if that option is set
"needs_U+": 0,            #if skill is needed to be used, says which level is needed
#non-individual (food):
"healing": 3,             #how many hp restores for 1 round
"healing_time": 1         #how many rounds healing effect works
}
#-------------------------------------------------------------------------------
#  QUALITY
#  - broken (-5)
#  - weak (-2)
#  - damaged (-1)
#  - average (0)
#  - good (1)
#  - forged (2)
#  - hardened (3)
#  - ultimate (4)

#  CATEGORY -> SLOTS ("weapons": main/alternative)

#  CRAFTING RECIPES + U+ needed WILL BE IN SEPARATE MENU