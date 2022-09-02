# Officially Supported Mod Types
***
Isle of Ansur is created with system allowing other people to join their own modules 
into Isle of Ansur, making kind of mod-relation for original content. 
Due to that system though, there are three main mod types modders will be able to do.

Note that these three mod types are not the only ones that will be available to make, 
but these three are supported by the game itself and its module managment system.

You can distribute any of these mods either as folders to be put manually, or via 
`.zip` file with same structure as you'd put folders to base game.

If you are not sure if your pack has correct hierarchy, you can refer to 
[this example pack containing folder structure for vanilla](https://drive.google.com/file/d/1XbetQ8Z4n5yiZ0JlUEjQ0VM438LCi1JD/view?usp=sharing).
***
## [Statpack](statpack_tutorial.md)
Statpack is module made only for `/stats/` path, and can contain either new races, 
new classes or new items.

## Worldpack
Worldpack is similarly, module exclusively written for `/worlds/` path, and contain 
any set of locations bound within "world". Worlds will be available during dialogue 
with ship captain.  
Exclusively though, worldpacks allow also for [custom menu panoramas](others_tutorial.md#menu-panoramas).

## Globalpack
These ones can be considered "full mods" in a way, because they introduce both features 
from previous types. Therefore they can not only tell new story and offer quests 
(Worldpack), but also introduce new items (Statpack) obtainable within that world. 
Globalpack uses both paths listed and requires both to be run.
***
## Scripts
Scripts are additional data that can be written in Python and run in specific situation
in game. They are complementary aspect of the game, yet they still need to be properly
introduced.