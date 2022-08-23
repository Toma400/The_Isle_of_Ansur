# Statpack Tutorial
***
## What is statpack?
Statpack is set of one or more .json files adding one of following features:
* [Races](statpack_tutorial.md#racesjson)
* [Classes](statpack_tutorial.md#classesjson)
* [Items](statpack_tutorial.md#itemsjson--craftingjson)

For each of these features it is needed respectively named .json file 
(races.json, classes.json, items.json + crafting.json), by default, 
placed in "stats/name_of_statpack/" directory.  
Files themselves needs to contain specific keys and values.

* [General races/classes values](statpack_tutorial.md#list-of-general-player-statistics)
* [General items values](statpack_tutorial.md#list-of-general-item-statistics)

Additionally, you need to attach language file to the directory, so you will be
able to provide translations for your mods' contents, using keys.

Remember that your statpack folder name has to be lowercased and use 
underline instead of spaces. Folder name is considered as your mod ID and 
it is used for any further [ID types](/docs/glossary.md#ids) (RID/CID/IID), therefore using other 
ways of writing it can cause issues.
Don't also forget about JSON syntax, since examples mentioned here shows how it 
should be done for one element. For more than one, 
you will need to follow syntax rules (files put in links can help to see 
syntax patterns). Remember that numerical values don't use quotation marks, 
same with booleans taking only `true/false` values.
***
## Races.json
Races represent main factor of creating character statistics, 
adding bonuses for attributes, powers, sometimes also perks and abilities.
You can start by seeing vanilla template uploaded 
[here](https://drive.google.com/file/d/1ffEDK6phESfF4N3DQMUbyXUAc3wqlNXe/view?usp=sharing).

One of races uploaded can look like this:
```
{
  "baedoorian": [
    {
      "descript": "races__baedoorian",
      "atr_strength": 2,
      "atr_charisma": 1,
      "atr_intelligence": 1,
      "atr_endurance": -1,
      "pwr_tech": 3,
      "abil_firearms": 1,
      "abil_persuasion": 1,
      "spec_diamond": false,
      "spec_moon": false
    }
  ]
}
```
As you see, it contains main key ("baedoorian" on top) and several values. 
While statistics are pretty straight-forward (you can see them listed 
[below](statpack_tutorial.md#list-of-general-player-statistics)), 
other values could be explained:

| In file        | What is it?    | Description                                                                                                    |
|----------------|----------------|----------------------------------------------------------------------------------------------------------------|
| "baedoorian"   | main key       | name of your race, following rules of creating a folder (lowercase, underline). Used as a second part for RID. |
| "descript"     | language key   | language key to viewable name of your race in-game. It refers to `lang.json` file value.                       |
| "spec_diamond" | power modifier | boolean value, set by default to false. Makes player ignore Tech - Magic relation penalty.                     |
| "spec_moon"    | power modifier | boolean value, set by default to false. Makes player ignore Void - Connection relation penalty.                |

## Classes.json
Classes are almost identical to races, the difference is only focus: they 
mostly add abilities, and bonus for attributes is really rare. 
Perks can be added, though, same with powers. 
Using `spec_diamond/spec_moon` is not prohibited, 
but it's definitely lore-unfriendly, as this bonus comes only with race.

Example file with vanilla classes can be found 
[here](https://drive.google.com/file/d/1tP1ZKsBqBjoKnlj47js23hGpjHIirqm7/view?usp=sharing).

If you want to make your class exclusive to specific race, you can use 
`race_exclusive: RID` value, stating RID of selected race.

## Items.json (& crafting.json)
These two .json files control existence of items (items.json) and their crafting
(crafting.json). Choice of which ones should exist in your mod folder depends on 
purpose:
* items.json alone is useful mostly if you create Globalpack (so items will not be 
  craftable, but you will be able to find them in world)
* crafting.json alone is useful if you want to add more recipes to vanilla items
* both .json files are useful for any item-adding mod, whether it is pure Statpack 
  or Globalpack

Differences between each .jsons aren't big, they only differ by used keys - 
let's look:
```
{
  "ayer_knife": [
    {
      "category": "weapon",
      "type": "shortsword",
      "descript": "Ayer Knife",
      "stackable": false,
      "weight": 1,
      "max_quality": "good",
      "min_price": 22,
      "max_price": 25,
      "average_dmg": 4,
      "dmg_yaw": 1,
      "block_chance": 10,
      "needs_U+": 0
    }
  ]
}
```
This is items.json file, limited for Ayer Knife item only. 
It has several keys, stating values needed for gameplay - 
values are explained in [this section](statpack_tutorial.md#list-of-general-item-statistics).
```
{
  "ansur:ayer_knife": [
    {
      "workplace": "anvil",
      "material_1": "ansur:iron_ingot",
      "material_2": "ansur:wooden_handle",
      "skill_needed": "smithery",
      "skill_level": 2,
      "sp_spent": 45
    }
  ]
}
```
In the meanwhile, here we have crafting.json file. It differs by:
* using IID in main key ("ansur:ayer_knife"), while items.json uses only latter part
* using different keys inside main key: they state crafting-related properties, such as where you can use the item

Values are so short that we can explain them here:
* `workplace` - is used to recognise which workplace it uses to be crafted. Handheld crafting items are counted as workplace too
* `material_n` - material used for crafting (IID). Amount of keys can differ, depending on how advanced that crafting is
* `skill_needed` - name of skill used for that crafting
* `skill_level` - level of the skill mentioned above. Set it to 0 to make crafting available for almost everyone
* `sp_spent` - stamina spent on that crafting action (amount should depend on effort, as in real life)
  * 5-15 - for really small tasks
  * 15-30 - for medium tasks
  * 30-100 - for big tasks
* `repair_material` - not necessary. If used, it allows player to repair item with this specific item (IID is used).

You can see list of workplaces [here](statpack_tutorial.md#workplaces).

***
## List of general player statistics
It is list of all statistics values you can use for races/classes creation. 
Values effects in-game are further explained [here](/docs/creation/statistics.md).
If you want to create bonus points to specific element, use positive value 
(n) - and for depleting element, use negative ones (-n).

#### Powers
`   'pwr_tech': n`
`   'pwr_magic': n`
`   'pwr_conn': n`
`   'pwr_void': n`

#### Attributes

`   'atr_charisma' : n`
`   'atr_dexterity' : n`
`   'atr_endurance' : n`
`   'atr_intelligence' : n`
`   'atr_strength' : n`

#### Abilities

* `   'abil_shortswords' : n`
`   'abil_longswords' : n`
`   'abil_archery' : n`
`   'abil_firearms' : n`
`   'abil_castspelling' : n`
* `   'abil_restoration_magic' : n`
`   'abil_transformation_magic' : n`
`   'abil_destruction_magic' : n`
`   'abil_necromancy' : n`
`   'abil_connection' : n`
* `   'abil_trade' : n`
`   'abil_persuasion' : n`
`   'abil_repair' : n`
`   'abil_traps' : n`
* `   'abil_resource_processing' : n`
`   'abil_tools' : n`
`   'abil_smithery' : n`
`   'abil_herbalism' : n`
`   'abil_alchemy' : n`
* `   'abil_lockpicking' : n`
`   'abil_sneaking' : n`
`   'abil_trapspotting' : n`
`   'abil_pickpocketing' : n`
* `   'abil_healing' : n`
`   'abil_cooking' : n`
`   'abil_survival' : n`
`   'abil_toughness' : n`

#### Perks
Perks should have usually boolean value (true/false). Boolean perks are listed with `m`, integer (numerical) perks are listed with `n`.

`   'perk_assassin_hit' : m`
`   'perk_trader_sight' : m`
`   'perk_vehicle_driving' : m`
`   'perk_toxin_immunity' : n`
`   'perk_animal_friend' : m`
`   'perk_animal_trainer' : m`

Remember that perks should be rare, because they can give huge advantage for each race/class using it. It can balance out your race/class, though, so also don't restrict yourself if you find it fitting for the race. Use of perk usually comes with other statistics being a bit weaker than for non-perk class/race.

***
## List of general item statistics
This lists all statistics used by items in vanilla Isle of Ansur. Some of them depends on item category. Order doesn't matter, but it is better to make properties organised anyway.

### General statistics
* `item_id` - similarly to player statistics, this one states ID, in this case of an item (called also IID). It's syntax is "mod_name:item_name"
* `category` - one of the most important elements of an item, states what this item do. List of categories will be below
* `descript` - it states in-game name of an item
* `stackable` - refers whether item uses any individual properties or not, using logic values "true/false" ("false" only if it has individual properties)
* `weight` - how much item weights
* `min_price` and `max_price` - gives borders for prices, stating item price between these two

### Categories
Categories refer to item usability and all other statistics are based on specific category. There are several categories:
* **weapon** - used to fight; use value `"stackable": false` with it
* **cloth** - counting also armour and jewelry, used to be equipped in slots
* **food** - counting also drinks, used to heal and restore your hunger/thirst if realistic system is turned on
* **plant** - counting both normal and dried versions of plants
* **tool** - used to craft things or use in specific action
* **weapon_tool** - used for multitools, used for both fight and other actions; uses both exclusive statistics
* **material** - any resources used directly to make parts or items
* **part** - parts of items (tools, weapons, clothes, and more), used in crafting
* **utility** - other items used for random actions

### Statistics: Weapon Category
* `type` - refers to type of weapon item represents. It is, in itself, similar to "category", because it separates some properties
  * `shortsword` and `longsword` - swords
  * `bow` and `crossbow` - classic ranged weapons
  * `firearm` - any kind of guns
  * `ranged` - other throwables, base on slightly different skill math (general experience and ranged weapons)
* `subtype` - optional. Refers for special subtypes of weapons, such as
  * `rapier` - has chance to deal second weaker attack during player's turn
  * `vanishable` - for `ranged` type, it means that after using item is removed from inventory
    * can be stackable
    * durability is usually 1, as it is single use (setting item on 1 durability can also achieve the same effect without vanishable key)
* `max_quality` - refers to most advanced quality weapon can get (during crafting or trade, it will obtain random quality)
  * `broken` - it is not useful at all
  * `weak` - it is heavily damaged and works poorly
  * `damaged` - it is not bad weapon, but it can work worse at some cases
  * `average` - it works just fine, sometimes having troubles
  * `good` - it is rather reliable weapon
  * `forged` - it is solid weapon you can trust
  * `hardened` - the best quality you can get in normal situation
  * `ultimate` - unbreakable and extremely reliable weapon (used mostly for end-game weapons)
* `durability` - number of uses before weapon turns to "broken" quality. You can repair it before it breaks to avoid that
* `average_dmg` - damage value
* `dmg_yaw` - yaw of damage value (so, final damage has range between "average - yaw" and "average + yaw")
* `block_chance` - **only for sword types** | percent chance of blocking damage if specific attack is used
* `needs_U+` - states if you need experience to use that weapon (set to 0 enables weapon to almost everyone)
* `self-harm_chance` - optional, states if player can be harmed with damage
  * `self-harm_skill` - if above is used, states if skills can make chance smaller
  * `self-harm_percent` - if above is used, this value states how much of initial damage player takes
    * `self-harm_yaw` - optional, states how much percent difference can randomly be chosen
### Statistics: Food Category
* `healing` - value of healing
* `healing_time` - time of healing (in turns); final healing value is result of multiplying `healing` with `healing_time`
* `hunger_thirst` - says whether it is potion or food
* `ht_restore` - points of hunger/thirst values restored
* `out` - use IID if food leaves item when eaten (if not, use "false"); usually used only for bottle-related potions

### Workplaces
In case you want your item be craftable, here is the list of workplaces you can use for your crafting. Remember that you should type them without spaces and using lowercase characters in .jsons, names here are mostly to be more intuitive. 
So, "Carry-on Woodprocessing Ensemble" will be "carry-on_woodprocessing_ensemble".
* `Anvil` - used for smithing recipes
* `Carry-on Woodprocessing Ensemble` - used with item in inventory, enables player to process wood into parts
* `Fire` - fireplaces of any kind, used for cooking and roasting food
* `Furnace` - used for some resource-converting recipes, such as raw ores processing
* `Gristmill` - used to process grain into flour
* `Herbalist String` - used to dry plants
* `Oven` - used for any more advanced meal-processing
* `Well` - self-explainable, used to obtain water