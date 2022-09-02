# Mechanics
This section uncovers some of technical details about how The Isle of Ansur works, which
can be useful for some more insightful modders out here.

### Loading of mods and autoupdating
Currently, mods are meant to be packed in .zip archives, storing all the hierarchy coherent
to what they want to append.  
This system allows the game to remove all non-vanilla packs and unpack them right away, 
when game starts. As much as this may sound unintuitive, it serves simple purpose: when
you update your mods, old files of those do not need to be manually removed.  
Instead, all files are removed, but then exact copy from .zip file is taken out again.  
This is what is called **autoupdating** of mods.

#### Legacy unpacking
In early stage of game development, there was manual system for all those, now being called
as **Legacy Unpacking**. Even though it gave you full control over files, the benefits of
it weren't really strong - but for ones who would prefer this approach, there's respective
option available in menu to be activated.

#### Removal details
Current loading of mods do not remove vanilla folders (as they have no .zip folder to
be referred), and they do their removal only on `/stats/` and `/worlds/` folders, so
statpacks, worldpacks and globalpacks can benefit from this system.  
This also means though, that if your pack overwrite `/ansur/` ID, it will not be possible
to revert those - so use overwriting with caution!  

In most cases, there's a way to overwrite vanilla aspects without touching vanilla
worldpacks, so less conflictive ways are always recommended.