# GLOSSARY

## List of Contents

* [Basic Technical Concepts](glossary.md#basic-technical-concepts)
* [More In-depth Elements](glossary.md#more-in-depth-elements)
* [Game Versioning](glossary.md#game-versioning)

---

### BASIC TECHNICAL CONCEPTS

---

###### IDs
There are several IDs in Isle of Ansur, all of them being used to differentiate
between specific elements of objects used during the game.

* CID (Class ID)
* IID (Item ID)
* RID (Race ID)

All of these IDs follow the same pattern: each of them contain `namespace` and
`raw ID`, separated by the colon. Correct ID looks like this:

`namespace:raw_ID`

IDs are generated automatically during data loading stage of the game, although
mod creators are asked to attach them to their content additionally for data safety
purposes.

---

### MORE IN-DEPTH ELEMENTS 

---

###### Call Stack Killer
Usually a loop. Used for elements that would not finish the function, leaving them open
and making recursions. Indicator for functions that are now "stable", at least at
that point, and pointer of hierarchy ("root" being `interface.py` module being main 
element of the game)

Still work in progress, since it is new issue to be handled for me.

---

### GAME VERSIONING

---

Game versioning requires separate section for listing all stages.

> **PRE-ALPHA**
> 
> Version of game not really possible to be played, containing mainly not-fully-
> implemented systems and elements that require lots of testing to be working correctly.
> 
> Released pre-alpha builds are only for later testing, and are usually unstable.<br>
> Can contain specific feature only, or game with implemented-yet features.

#### LIST OF RELEASED VERSIONS

    * Pre-Alpha 1