import ../../bcs/img_manag
import ../../bcs/operators
import ../../bcs/project
import std/logging
import std/tables
import results
import nigui

proc mainProjReg (skylight: Skylight, screens: Table[string, LayoutContainer], buttons: Table[string, Button], ids: ComboBox, labels: Table[string, Label])
proc mainProjSettings (skylight: Skylight, screens: Table[string, LayoutContainer], buttons: Table[string, Button], ids: ComboBox, labels: Table[string, Label])
proc mainProjEvents (buttons: Table[string, Button])

proc mainProjScreen* (skylight: Skylight, images: Table[string, Image], pj: var IoaProject) =
    windowInit(skylight.win) # update for entryScreen
    for pjids in pj.ids:
        pj.lge(lvlInfo, "Loading project " & pj.name & ". Recognised ID: " & pjids)

    let mainScreen   = newLayoutContainer(Layout_Vertical)
    let upScreen     = newLayoutContainer(Layout_Horizontal)  # upper bar
    let upLScreen    = newLayoutContainer(Layout_Horizontal)    # return button
    let upRScreen    = newLayoutContainer(Layout_Horizontal)    # title
    let downScreen   = newLayoutContainer(Layout_Horizontal)  # lower bar
    let sideScreen   = newLayoutContainer(Layout_Vertical)      # sidebar
    let sectScreen   = newLayoutContainer(Layout_Horizontal)    # button sections
    let leftSection  = newLayoutContainer(Layout_Vertical)        # section left
    let rightSection = newLayoutContainer(Layout_Vertical)        # section right

    #[ Game utils ]#
    let scrButton = newButton(langstr("project__scripts"));   scrButton.enabled = false
    let fntButton = newButton(langstr("project__fonts"));     fntButton.enabled = false
    let panButton = newButton(langstr("project__panoramas")); panButton.enabled = false
    let musButton = newButton(langstr("project__music"));     musButton.enabled = false
    #[ Game elements ]#
    let rcButton  = newButton(langstr("project__races"));     rcButton.enabled  = false
    let clButton  = newButton(langstr("project__classes"));   clButton.enabled  = false
    let itmButton = newButton(langstr("project__items"));     itmButton.enabled = false
    let entButton = newButton(langstr("project__entities"));  entButton.enabled = false
    #[ Sidebar elements ]#
    let idCombBox = newComboBox(pj.ids)
    let nidButton = newButton(langstr("project__new_id")); nidButton.enabled = false
    let expButton = newButton(langstr("project__export")); expButton.enabled = false
    #[ Upperbar elements ]#
    let bkButton = newButton("<<"); bkButton.enabled = false
    let pjLabel  = newLabel(boundText(pj.name))

    let screens = { "main": mainScreen, "upbar": upScreen, "downbar": downScreen, "sidebar": sideScreen,
                    "section_main": sectScreen, "section_left": leftSection, "section_right": rightSection,
                    "upbar_l": upLScreen, "upbar_r": upRScreen }.toTable
    let buttons = { "scripts": scrButton, "fonts": fntButton, "panoramas": panButton, "music": musButton,
                    "races": rcButton, "classes": clButton, "items": itmButton, "entities": entButton,
                    "back": bkButton, "new_id": nidButton, "export": expButton }.toTable
    let labels  = { "pj_name": pjLabel }.toTable

    mainProjSettings(skylight, screens, buttons, idCombBox, labels)
    mainProjReg(skylight, screens, buttons, idCombBox, labels)
    mainProjEvents(buttons)

proc mainProjSettings (skylight: Skylight, screens: Table[string, LayoutContainer], buttons: Table[string, Button],
                       ids: ComboBox, labels: Table[string, Label]) =
    block wAlign:
      screens["sidebar"].xAlign       = XAlign_Center
      screens["section_main"].xAlign  = XAlign_Center
      screens["section_left"].xAlign  = XAlign_Center
      screens["section_right"].xAlign = XAlign_Center
      screens["upbar_l"].xAlign       = XAlign_Center
      screens["upbar_r"].xAlign       = XAlign_Center
    block wSize:
      #[ screens ]#
      screens["upbar"].width        = returnAdjCell(100, AXES.X, 3, skylight.win.width)
      screens["upbar_r"].width      = returnAdjCell(80,  AXES.X, 2, skylight.win.width)
      screens["downbar"].width      = returnAdjCell(100, AXES.X, 3, skylight.win.width)
      screens["sidebar"].width      = returnAdjCell(25,  AXES.X, 2, skylight.win.width)
      screens["section_main"].width = returnAdjCell(74,  AXES.X, 2, skylight.win.width)
      #[ buttons ]#
      buttons["scripts"].width      = returnAdjCell(35,  AXES.X, 2, skylight.win.width)
      buttons["fonts"].width        = returnAdjCell(35,  AXES.X, 2, skylight.win.width)
      buttons["panoramas"].width    = returnAdjCell(35,  AXES.X, 2, skylight.win.width)
      buttons["music"].width        = returnAdjCell(35,  AXES.X, 2, skylight.win.width)
      buttons["races"].width        = returnAdjCell(35,  AXES.X, 2, skylight.win.width)
      buttons["classes"].width      = returnAdjCell(35,  AXES.X, 2, skylight.win.width)
      buttons["items"].width        = returnAdjCell(35,  AXES.X, 2, skylight.win.width)
      buttons["entities"].width     = returnAdjCell(35,  AXES.X, 2, skylight.win.width)
      buttons["back"].width   = returnAdjCell(10, AXES.X, 2, skylight.win.width)
      buttons["new_id"].width = returnAdjCell(20, AXES.X, 2, skylight.win.width)
      buttons["export"].width = returnAdjCell(20, AXES.X, 2, skylight.win.width)
      ids.width               = returnAdjCell(20, AXES.X, 2, skylight.win.width)
      #[ text ]#
      labels["pj_name"].fontSize = 18
    block wFrames:
      screens["upbar"].frame        = newFrame()
      screens["downbar"].frame      = newFrame()
      screens["sidebar"].frame      = newFrame()
      screens["section_main"].frame = newFrame()

proc mainProjReg (skylight: Skylight, screens: Table[string, LayoutContainer], buttons: Table[string, Button],
                  ids: ComboBox, labels: Table[string, Label]) =
    block wScreens:
      skylight.con.add(screens["main"])
      screens["main"].add(screens["upbar"])
      screens["main"].add(screens["downbar"])
      screens["downbar"].add(screens["sidebar"])
      screens["downbar"].add(screens["section_main"])
      screens["section_main"].add(screens["section_left"])
      screens["section_main"].add(screens["section_right"])
    block wBars:
      #[ upperbar ]#
      screens["upbar"].add(screens["upbar_l"])
      screens["upbar"].add(screens["upbar_r"])
      screens["upbar_l"].add(buttons["back"])
      screens["upbar_r"].add(labels["pj_name"])
      #[ sidebar ]#
      screens["sidebar"].add(ids)
      screens["sidebar"].add(buttons["new_id"])
      screens["sidebar"].add(buttons["export"])
    block wButtons:
      #[ left section ]#
      screens["section_left"].add(horizLine(hls=" "))
      screens["section_left"].add(buttons["scripts"])
      screens["section_left"].add(buttons["fonts"])
      screens["section_left"].add(buttons["panoramas"])
      screens["section_left"].add(buttons["music"])
      screens["section_left"].add(horizLine(hls=" "))
      #[ right section ]#
      screens["section_right"].add(horizLine(hls=" "))
      screens["section_right"].add(buttons["races"])
      screens["section_right"].add(buttons["classes"])
      screens["section_right"].add(buttons["items"])
      screens["section_right"].add(buttons["entities"])
      screens["section_right"].add(horizLine(hls=" "))

proc mainProjDraw () =
    discard

proc mainProjEvents (buttons: Table[string, Button]) =
    buttons["scripts"].onClick = proc (event: ClickEvent) =
        discard

proc enterProject* (skylight: Skylight, images: Table[string, Image], log: FileLogger, pj_name: string) =
    log.log(lvlInfo, "Entering the project with name -" & pj_name & "-")
    var pj = buildProject(pj_name, log)
    windowUpdate(skylight, bcs_name & ": " & pj_name)
    mainProjScreen(skylight, images, pj)