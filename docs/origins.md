# Origins
Origin is feature that allows player to pick the story background for their character.  
It is origin that decides on where and when player starts the game and what will be
the story told by the game.

To create an origin, create folder in `stats/{your mod id}/origins/` and then .json
file with name of your origin.  
Mod ID combined with origin filename will create your origin ID (OID).

### Origin file
Once you created .json file, you can now open it with any text editor and write data
needed for your origin.

To learn what you should write, let's look at vanilla example:
```json
{
  "key": "origin__wanderer",
  "new_game": {
    "location": "ansur:sea__veno_edran__deck0",
    "time":     [2,921,8,23,1,11,0],
    "inventory": [
      {"ansur:letter_to_yourself": 1}
    ]
  }
}
```
### Contents
- `key` - language key for origin name and description
- `new_game` - section related to new game information
  - `location` - location ID for where player will start the game
  - `date` - date in correct format, telling game when player will start the game
  - `inventory` - list of items player will have in their inventory when starting the game

### Date
Date is written in such syntax:
```nim
[era,year,month,day,weekday,hour,minutes]
```