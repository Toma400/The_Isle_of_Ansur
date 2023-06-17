import ../../bcs/operators
import std/logging
import std/tables
import nigui

proc mainProjReg (skylight: Skylight, screens: Table[string, LayoutContainer], buttons: Table[string, Button])
proc mainProjSettings (screens: Table[string, LayoutContainer])
proc mainProjEvents (buttons: Table[string, Button])

proc mainProjScreen* (skylight: Skylight, images: Table[string, Image], log: FileLogger, pj_name: string) =
    windowInit(skylight.win) # update for entryScreen
    let mainScreen   = newLayoutContainer(Layout_Vertical)
    let upScreen     = newLayoutContainer(Layout_Horizontal)  # upper bar
    let downScreen   = newLayoutContainer(Layout_Horizontal)  # lower bar
    let sideScreen   = newLayoutContainer(Layout_Vertical)      # sidebar
    let sectScreen   = newLayoutContainer(Layout_Horizontal)    # button sections
    let leftSection  = newLayoutContainer(Layout_Vertical)        # section left
    let rightSection = newLayoutContainer(Layout_Vertical)        # section right

    #[ Game utils ]#
    let scrButton = newButton(langstr("project__scripts"))
    let thmButton = newButton(langstr("project__themes"));    thmButton.enabled = false
    let panButton = newButton(langstr("project__panoramas")); panButton.enabled = false
    let musButton = newButton(langstr("project__music"));     musButton.enabled = false
    #[ Game elements ]#
    let rcButton  = newButton(langstr("project__races"));     rcButton.enabled  = false
    let clButton  = newButton(langstr("project__classes"));   clButton.enabled  = false
    let itmButton = newButton(langstr("project__items"));     itmButton.enabled = false
    let entButton = newButton(langstr("project__entities"));  entButton.enabled = false

    let screens = { "main": mainScreen, "upbar": upScreen, "downbar": downScreen, "sidebar": sideScreen,
                    "section_main": sectScreen, "section_left": leftSection, "section_right": rightSection }.toTable
    let buttons = { "scripts": scrButton, "themes": thmButton, "panoramas": panButton, "music": musButton,
                    "races": rcButton, "classes": clButton, "items": itmButton, "entities": entButton }.toTable

    mainProjSettings(screens)
    mainProjReg(skylight, screens, buttons)
    mainProjEvents(buttons)

proc mainProjSettings (screens: Table[string, LayoutContainer]) =
    block wFrames:
      screens["upbar"].frame        = newFrame()
      screens["downbar"].frame      = newFrame()
      screens["sidebar"].frame      = newFrame()
      screens["section_main"].frame = newFrame()

proc mainProjReg (skylight: Skylight, screens: Table[string, LayoutContainer], buttons: Table[string, Button]) =
    block wScreens:
      skylight.con.add(screens["main"])
      screens["main"].add(screens["upbar"])
      screens["main"].add(screens["downbar"])
      screens["downbar"].add(screens["sidebar"])
      screens["downbar"].add(screens["section_main"])
      screens["section_main"].add(screens["section_left"])
      screens["section_main"].add(screens["section_right"])
    block wButtons:
      screens["section_left"].add(buttons["scripts"])
      screens["section_left"].add(buttons["themes"])
      screens["section_left"].add(buttons["panoramas"])
      screens["section_left"].add(buttons["music"])
      screens["section_right"].add(buttons["races"])
      screens["section_right"].add(buttons["classes"])
      screens["section_right"].add(buttons["items"])
      screens["section_right"].add(buttons["entities"])

proc mainProjDraw () =
    discard

proc mainProjEvents (buttons: Table[string, Button]) =
    buttons["scripts"].onClick = proc (event: ClickEvent) =
        discard

proc enterProject* (skylight: Skylight, images: Table[string, Image], log: FileLogger, pj_name: string) =
    log.log(lvlInfo, "Entering the project with name -" & pj_name & "-")
    windowUpdate(skylight, bcs_name & ": " & pj_name)
    mainProjScreen(skylight, images, log, pj_name)