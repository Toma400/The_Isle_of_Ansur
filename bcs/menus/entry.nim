import ../../bcs/img_manag
import ../../bcs/operators
import ../../init
import std/strutils
import std/logging
import std/tables
import new_entry
import proj_main
import nigui
# pre-loading later functions
proc entryReg      (skylight: Skylight, screens: Table[string, LayoutContainer], buttons: Table[string, Button], projects: ComboBox, pre_label: Label, project_label: Label)
proc entryDraw     (skylight: Skylight, screens: Table[string, LayoutContainer], images: Table[string, Image])
proc entrySettings (skylight: Skylight, screens: Table[string, LayoutContainer], project_label: Label)

#[ --- MAIN BODY --- ]#
proc entryScreen* (skylight: Skylight, images: Table[string, Image], log: FileLogger) =
    windowInit(skylight.win, res=(700, 420)) # update for entryScreen
    let mainScreen = newLayoutContainer(Layout_Horizontal)
    let left       = newLayoutContainer(Layout_Vertical)
    let right      = newLayoutContainer(Layout_Vertical)
    let nScreen    = newLayoutContainer(Layout_Vertical) # name text
    let bScreen    = newLayoutContainer(Layout_Vertical) # buttons
    let screens    = { "main":  mainScreen, "left":  left, "right": right, "buttons": bScreen, "name": nScreen }.toTable

    let enterButton  = newButton(langstr("login__open"))
    let addButton    = newButton(langstr("login__add"))
    let removeButton = newButton(langstr("login__remove")); removeButton.enabled = false
    let buttons      = { "enter": enterButton, "add": addButton, "remove": removeButton }.toTable

    let prejLabel = newLabel("______________________")
    let projLabel = newLabel("\n " & langstr("login__listbox") & "   \n")
    let projList  = newComboBox(get_mods(PT.PROJECTS))

    enterButton.onClick = proc (event: ClickEvent) =
      enterProject(skylight, images, log, projList.value)

    addButton.onClick = proc (event: ClickEvent) =
      createNewProject(skylight, images, log)

    entrySettings(skylight, screens, projLabel)
    entryReg(skylight, screens, buttons, projList, prejLabel, projLabel)
    entryDraw(skylight, screens, images)

proc entrySettings (skylight: Skylight, screens: Table[string, LayoutContainer], project_label: Label) =
    block wExperimental:
      project_label.fontSize = 18
    block wSize:
      #[ WIDTH ]#
      screens["left"].width  = returnAdjCell(50, AXES.X, 3, skylight.win.width)
      screens["right"].width = returnAdjCell(50, AXES.X, 3, skylight.win.width)
      screens["name"].width  = returnAdjCell(20, AXES.X, -2, skylight.win.width)
      #[ HEIGHT ]#
      screens["left"].height  = returnAdjCell(100, AXES.Y, 9, skylight.win.height - returnCell(4, AXES.Y))
      screens["right"].height = returnAdjCell(100, AXES.Y, 9, skylight.win.height - returnCell(4, AXES.Y))
      screens["name"].height  = returnAdjCell(10, AXES.Y, 1, skylight.win.height)
    block wAlign:
      screens["main"].xAlign    = XAlign_Center
      screens["left"].xAlign    = XAlign_Center
      screens["right"].xAlign   = XAlign_Center
      screens["name"].xAlign    = XAlign_Center
      screens["buttons"].xAlign = XAlign_Center
    block wFrames:
      screens["left"].frame    = newFrame()
      screens["right"].frame   = newFrame()
      screens["buttons"].frame = newFrame()

proc entryReg (skylight: Skylight, screens: Table[string, LayoutContainer], buttons: Table[string, Button], projects: ComboBox, pre_label: Label, project_label: Label) =
    block wScreens:
      skylight.con.add(screens["main"])
      screens["main"].add(screens["left"])
      screens["main"].add(screens["right"])
      screens["left"].add(screens["name"])
      screens["left"].add(screens["buttons"])
    block wButtons:
      screens["buttons"].add(buttons["enter"])
      screens["buttons"].add(buttons["add"])
      screens["buttons"].add(buttons["remove"])
    block wOther:
      screens["left"].add(pre_label)
      screens["left"].add(project_label)
      screens["left"].add(projects)

proc entryDraw (skylight: Skylight, screens: Table[string, LayoutContainer], images: Table[string, Image]) =
    #[ RIGHT SCREEN ]#
    screens["right"].onDraw = proc (event: DrawEvent) =
      let canvas = event.control.canvas
      canvas.drawImage(images["logo"], x=returnAdjCell(5, AXES.X, context=skylight.win.width),
                                       y=returnAdjCell(6, AXES.Y, context=skylight.win.height),
                                       width=returnAdjCell(40, AXES.X, context=skylight.win.width))

    #[ LEFT SCREEN ]#
    screens["name"].onDraw = proc (event: DrawEvent) =
      let canvas = event.control.canvas
      canvas.drawTextCentered(bcs_name, x=0,
                                        y=0,
                                        width=returnAdjCell(20, AXES.X, context=skylight.win.width),
                                        height=returnAdjCell(3, AXES.Y, context=skylight.win.height))
      canvas.drawTextCentered(bcs_ver, x=0,
                                       y=20,
                                       width=returnAdjCell(22, AXES.X, context=skylight.win.width),
                                       height=returnAdjCell(3, AXES.Y, context=skylight.win.height))