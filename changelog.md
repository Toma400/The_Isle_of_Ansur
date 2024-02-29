# <center>Changelog</center>

---

## List of contents
### [Pre-alpha builds](changelog.md#pre-alpha-builds)

---
## Pre-alpha builds
- [Pre-alpha 6](#pre-alpha-6)
- [Pre-alpha 5](#pre-alpha-5)
- [Pre-alpha 4](#pre-alpha-4)
- [Pre-alpha 3b](#pre-alpha-3b)
- [Pre-alpha 3](#pre-alpha-3)
- [Pre-alpha 2](#pre-alpha-2)
- [Pre-alpha 1](#pre-alpha-1)

> ---
```
> ### Pre-alpha 6
> - Fixes
>   - Fixed not recognising uppercased file extensions (#118)
>
```
> ### Pre-alpha 5
> - Gameplay
>   - You can now load your game
>     - If save has wrong/old structure, it will show an error
>     - Saves made previously need patching to update their structure
>       to current system
> - Technicals
>   - Save system was entirely remade to match new requirements
>     - Patch that allows updating old saves is delivered with release
>   - Added inventory and item systems (heavily WIP and unseen in game though)
>     - Origin and class can now add initial items added when game starts
> - Polish version
>   - Moved into [separate mod](https://github.com/Toma400/The_Isle_of_Ansur_PL)
>     for the time being
> - Fixes
>   - Fixed crash to desktop on loading menu (#111)
> ### Pre-alpha 4
> - Gameplay
>   - Added possibility to add avatars during character creation
>     - Avatar can be added by using URL linked to image, or file path
>     - But also picked from avatars built for each race/gender
>       - No avatars are available at the moment due to time constraints
>     - You can see your character avatar in loading menu
> - Mod Manager Menu (MMM)
>   - Introduces Mod Loading Order (MLO) and way to change it
>   - Allows for disabling zip packs (results in them not unpacking)
>   - You can now make logo of your mod visible in-game
>     (`logo` key in info.toml file)
> - Quality-of-Life
>   - Tooltip now appears whenever you hover on GUI elements having it
>     - You can turn tooltips in settings
>   - Text resizing is automatical with every resolution change now
>     (no more changes to 400x400 resolution while keeping big text!)
> - Fixes
>   - Fixed Polish letters not being recognised (#104)
> ### Pre-alpha 3b
> - Gameplay
>   - Removed `Human, Born in Moon Continent` race due to BRPGS 3.0 changes
>     (if you saved character with it, the save will probably not load)
>   - Improved descriptions of all game elements
> - Quality-of-Life
>   - You can now go back to previous option in character creation menu
>   - Improvements to graphical interface clarity
>   - You can now remove savegames
> - Polish version
>   - Added custom-made Ferrum font with expanded glyphs
>   - Translated all game contents to Polish
> - Modding
>   - Mods can now be bundled into .zip file and put in 'packs' directory
>     (if legacy unpacking isn't turned on, they will unpack automatically)
>   - If unpacking is enabled, contents of 'stats', 'worlds', 'themes' and 'scripts'
>     is removed during load (before unpacking, which reloads contents this way)
>   - `Info.toml` now allows you for stating mod requirements, as well as specific
>     version (it can also check vanilla version). Version ranges are supported
>     - If version is not met, error message is shown and some menu options are disabled
>   - Script function that runs during event is now called 'tick' (earlier: 'run')
>     - This is build-up for a bit more nuanced scripting system in the future
>   - Mods adding genders can now customise wording through special language rules
> - Technicals
>   - System-accepted languages are now referenced from `system_ref` which makes them
>     less hardcoded and even editable through scripts/mods
>   - Theme-driven elements should now be consistent
>     (previously it mixed theming with hardcoded values)
> - Fixes
>   - Fixed lore names not showing up (#94)
>   - Fixed data hanging during saving game (#93)
>
> ---
> ### Pre-alpha 3
>
> - **Full overhaul of file system**
> - **Switching to graphical interface**
> - Expanded modding possibilities
>   - **Scripting system allowing you to implement Python code during gameplay**
>   - Modders now can add their custom background images and music
>   - Added `themepack` which controls several aesthetical elements 
> - Some QoL additions
>   - Update notification system which will notify about possibility to update the game
> - Updated to Python 3.10
> - Further updates to match current Baedoor RPG System
> 
> ---
> ### Pre-alpha 2
> 
> <span style="color:#871C2C; font-weight:bold">IT IS NOT SAFE TO CREATE MODS NOR SAVES FROM THIS POINT ON. NEXT RELEASES WILL INTRODUCE GAMEBREAKING CHANGES.</span>  
> <span style="color:#A44B58; font-weight:bold">Even though, changelog notes will list all technical changes which can be followed by mod creators to adjust their mods to new versions.</span>
> 
> - Updated to current Baedoor RPG System
>   - Changes of several namings and added/removed some elements to match
> - Added language support
>   - Modders will need to adjust their packs to match language files being required (`lang.json`)
> - Huge code optimalisations
> - Log system introduced
> - Changed some IDs in vanilla elements
>   - Old saves will not be compatibile. Please recreate your character or edit the IDs manually; no tools for conversion are made yet
> 
> ---
> ### Pre-alpha 1
> 
> - Added basic elements, such as menu
> - Added character setup
> - Added modding support
>   - Statpacks can be created and used (allowing modders to distribute them via .zip archives)
>   - Modloader accessible via menu, allowing players to see installed mods and deactivate them if needed
> 
> ---