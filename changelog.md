# <center>Changelog</center>

---

## List of contents
### [Pre-alpha builds](changelog.md#pre-alpha-builds)

---
## Pre-alpha builds
- [Pre-alpha 3b](#centerpre-alpha-3bcenter)
- [Pre-alpha 3](#centerpre-alpha-3center)
- [Pre-alpha 2](#centerpre-alpha-2center)
- [Pre-alpha 1](#centerpre-alpha-1center)

> ---
> ###<center>Pre-alpha 3b</center>
```
> - QoL
>   - You can now go back to previous option in character creation menu
>   - Improvements to graphical interface clarity
> - Polish version
>   - Added custom-made Ferrum font with expanded glyphs
>   - Translated all game contents to Polish
> - Modding
>   - Mods can now be bundled into .zip file and put in 'packs' directory
>     (if legacy unpacking isn't turned on, they will unpack automatically)
> - Technicals
>   - System-accepted languages are now referenced from `system_ref` which makes them
>     less hardcoded and even editable through scripts/mods
> - Fixes
>   - Fixed lore names not showing up (#94)
> 
```
> ---
> ###<center>Pre-alpha 3</center>
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
> ###<center>Pre-alpha 2</center>
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
> ###<center>Pre-alpha 1</center>
> 
> - Added basic elements, such as menu
> - Added character setup
> - Added modding support
>   - Statpacks can be created and used (allowing modders to distribute them via .zip archives)
>   - Modloader accessible via menu, allowing players to see installed mods and deactivate them if needed
> 
> ---