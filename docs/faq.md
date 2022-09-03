# FAQ
Here you will find all commonly asked questions, or the ones I found important to answer.

* [General Questions](faq.md#general-questions)
* [Technical Questions](faq.md#technical-questions)
* [Modding Support Questions](faq.md#modding-support-questions)
* [Copyright Questions](faq.md#copyright-questions)

***

# General Questions
## 1. How long will you maintain this game? Will you like to add new mod-supporting features once you finish it?
I can't say anything for certain as of right now, but I will try my best to maintain 
the game as long as it will have some issues I can fix. If there's any request for 
specific feature (especially mod-aimed) or pull request with code adding that without 
any issues for backcompatibility, I will also try my best to review it and introduce, 
if it would follow general game way of thinking.

## 2. How much will you add before you see IoA as "finished"?
Well, my main goal is to reintroduce whole Between Shadows and Lights content, this time
though including all mechanics being available, despite BSaL content not giving need
to utilise them all. Also, I want to make IoA having broad modding possibilities, so
I can leave IoA "as is" and be sure that people can infinitely enhance it, adding new
worlds and stories.

There's a chance that I will add new lands, so there's a possibility that it will have 
way more features included and much more lore revealed with its core gameplay. 
It all depends on my time, money and motivation though.

## 3. If you would envision next modules / updates, what those would be?
First development cycle, subtitled **Between Shadows and Light**, will add Ansur isle,
expanded a bit from what was in original BSaL - so, this time you will be able to travel
through the island, and visit second city.  

Second one, which is also likely to be made, called **Xaine's Dreams**, will expand
the lore over *oververse* concept and open modding possibilities towards more lore-friendly
additions of dimensions and universes.  

After that, nothing is really fully planned.   
There are visions over third cycle called "Dust of the Empire", aimed on New Baedoor city, 
and there's also vision of showcasing Agoi Archipelago islands, but I may as well 
just end development on second cycle.

***

# Technical Questions
## 1. I didn't save my game for a long time, and my game crashed/something else happened. Do I need to do everything again?
No, you don't. IoA uses constant autosave in separate directory, 
always allowing you to have "up-to-date" save files.
Go into your saved profile (it is placed in "saves/" directory and 
uses name of your profile) and find folder named "in use". 
Copy its contents outside, replacing them. 
This way you will have latest data "hardsaved" and you will be able to 
come back to it while loading the game from menu.

**Important issue though: if your game crashed during profile creation, 
I'd suggest removing the directory with save and creating new profile in-game - 
just because it means you will not get any statistics bonuses coming from 
non-choosen options. You can refer to your previous profile.json file to 
find out which gender, class or race you chosen.**

## 2. Can I use different settings on different saves?
Yes, you can. Remember though that - if you want to convert them - 
you can only convert non-realistic settings into realistic one. 
It is protection from bugs that could come from time differences and lack of 
statistics.

***

# Modding Support Questions
## 1. I want to upload my mod. Where should I?
You have plenty of options. Obviously, you can host whole new project as GitHub
repository or itch.io one, for example, or share link to Google Drive/DropBox with file.  
But, if you prefer to handle it in less clunky way, you can [join Discord server](https://discord.gg/GbTw9KqnrE)
and share the pack with me - I will investigate it and if it works correctly, it will
be uploaded on [Isle of Ansur Mod Repository](https://github.com/Toma400/Isle_of_Ansur_Mods_Repository)
which is sort of mini-hosting I offer for Isle of Ansur mods (or at least officially
made packs).

## 2. Can I change my pack's name? Or my items/races/classes name?
Yes, and no. You are absolutely free to change any `descript` names in your pack,
since those are mutable values. 

If you attempt to change names that are used for pack's ID though, do it only 
if you never published this pack earlier. ID names are - for now, at least - immutable,
which means that if person played the game with your pack, removing or changing these
values will most likely crash the game.

There's a chance IoA will start to handle such exceptions, but for now I can't promise
it being worked on.

***

# Copyright Questions
## 1. I made a mod. Where can I publish it?
Anywhere you want! As a mod creator, you have full rights to publish it on any page!
EULA restricts you only to not benefit from accessing the mod, so the only requirement
for distributing IoA mods is that they have to be accessible without paying or profitting
from that. 

You can of course put donation links and such on the pages with distribution,
since users donating will not pay for product per se, but more as a support gesture for
you.