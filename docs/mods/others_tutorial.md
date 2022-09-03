# Tutorial on smaller features
This section is dedicated for all features that are not fully statpacks/worldpacks, but
they are still available for modders to use.

- [Menu panoramas](others_tutorial.md#menu-panoramas)
- [Menu music](others_tutorial.md#menu-music)
***
### Menu panoramas
One can add new panoramas to main menu, using their own worldpack folder, or by just
appending panoramas to vanilla folder (in second case, though, [they cannot be autoupdated](mechanics.md#loading-of-mods-and-autoupdating),
which makes it more difficult for the user).

Appending new panoramas is amazingly easy - the only thing you need to do is creating
specific directory path in your mod's workspace:
```
/ worlds / your_mod_id / assets / backgrounds /  
```
Everything put in that directory with `.jpg` or `.png` extension will be counted as
panorama to be randomly chosen at the start of the game.

If you want your panorama to overwrite vanilla ones, add `%PR_` to the name of the image.
Panoramas using this key are prioritised, so if any mod adds such, game will only
shuffle through the ones sharing this key.

### Menu music
Similarly to menu panoramas, music can be added via putting `.mp3`, `.wav` or `.ogg`
files into specific directory of your mod's workspace:
```
/ worlds / your_mod_id / music / backgrounds /
```
The same way as in panoramas, if you want to overwrite vanilla music, just add `%PR_`
key to your music filename. Music with this key use separate shuffler which selects
only files using them.