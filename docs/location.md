# Location
Location is a basic element that represents world in Isle of Ansur game.  
It is made by creating folder in `worlds/{your mod id}/locations/`. Name of the folder
created together with mod ID will become a location ID (LID).

- [Destinations](#destinations)
  - [Contents](#contents)
  - [Script syntax](#script-syntax)

### Destinations
To create a destination player can travel to from specific location, create `destinations`
folder. Next, create a .toml file [with name of your choice](#destination-filename-is-not-id).

It should look like that:
```toml
key         = "loc__sea__veno_edran_deck0"
destination = "ansur:sea__veno_edran__deck0"
always_visible = true

descr = "loc__sea__veno_edran_deck1to0"
req = [
    "statistics/skills.yaml | ansur:blunts | = 3"
]
req_or = [
    
]
cost = [
    
]
set = [
    
]
```
#### Contents
- `key` - language key for location name and description
- `destination` - location ID (LID) for the location you want teleport player to
- `always_visible` - optional, defaults to `true`. If set to `false`, it will hide the
  destination from travel menu
- `descr` language key for travel description
- `req` - all scripts in this list must return true
- `req_or` - any of scripts in this list must return true
- `cost` - scripts in this list will change player statistics
  (value must be `int` type)
- `set` - scripts in this list will set value to player statistics

#### Script syntax
Scripts are made with flexibility in mind, so their structure is fairly easy to explain:
```elixir
file_path | optional_categories |> key | value
```
- `file_path` - should include file with all folders needed in between
  (accepts only .yaml and .toml files)
- `optional_categories` - if categories exist, they should be separated by `|>` and
  be ordered by their depth from highest to lowest
- `key` - key in the dictionary
- `value` - value that needs to be checked or edited:
  - in conditional scripts (`req`, `req_or`) it follows this logic:
    - no symbol or `=` included check if value is equal
    - `>` value checks if value is smaller than given
    - `<` value checks if value is bigger than given
  - in `cost` it must be `int` type, and by default performs subtraction
    - use negative number to increase the value
  - in `set`, the default value type is `int`, and yields `str` if it can't be parsed

#### Destination filename is not ID
It is important to remember destination filename doesn't matter. Aside of filenames not
being able to include `:` symbol, it makes little sense to include ID in it:
- there's no situation when you won't open the file anyway
- it makes no sense to include more than 10 at once, so reaching RAM cap isn't an issue
- multiple files with the same destination are possible
- it makes it very easy to overwrite the file with different contents