import ../../bcs/img_manag
import ../../bcs/operators
import ../../init
import std/strutils
import std/logging
import std/tables
import nigui
# pre-loading later functions
proc entryReg      (window: Window, screens: Table[string, LayoutContainer], buttons: Table[string, Button], projects: ComboBox, project_label: Label)
proc entryDraw     (screens: Table[string, LayoutContainer], images: Table[string, Image])
proc entrySettings (screens: Table[string, LayoutContainer])

#[ --- MAIN BODY --- ]#
proc entryScreen* (window: Window, images: Table[string, Image], log: FileLogger) =
    windowInit(window, res=(700, 470)) # update for entryScreen
    let mainScreen = newLayoutContainer(Layout_Horizontal)
    let left       = newLayoutContainer(Layout_Vertical)
    let right      = newLayoutContainer(Layout_Vertical)
    let nScreen    = newLayoutContainer(Layout_Vertical) # name text
    let bScreen    = newLayoutContainer(Layout_Vertical) # buttons
    let screens    = { "main":  mainScreen, "left":  left, "right": right, "buttons": bScreen, "name": nScreen }.toTable

    let enterButton  = newButton(langstr("login__open"))
    let addButton    = newButton(langstr("login__add"))
    let removeButton = newButton(langstr("login__remove"))
    let buttons      = { "enter": enterButton, "add": addButton, "remove": removeButton }.toTable

    let projLabel = newLabel(langstr("login__listbox"))
    let projList  = newComboBox(get_mods(PT.PROJECTS))

    #
    # enterButton.onClick = proc (event: ClickEvent) =
    #   log.log(lvlDebug, projList.value)

    entrySettings(screens)
    entryReg(window, screens, buttons, projList, projLabel)
    entryDraw(screens, images)

proc entrySettings (screens: Table[string, LayoutContainer]) =
    block wExperimental:
      screens["left"].padding   = 50
      screens["right"].padding  = 200
      screens["name"].padding   = 70
    block wAlign:
      screens["left"].xAlign    = XAlign_Center #.setInnerSize((parseInt(settings("res_x"))/2).int,  (parseInt(settings("res_y"))))
      screens["right"].xAlign   = XAlign_Center #.setInnerSize((parseInt(settings("res_x"))/2).int, (parseInt(settings("res_y"))))
      screens["name"].xAlign    = XAlign_Center
      screens["buttons"].xAlign = XAlign_Center
    block wFrames:
      screens["left"].frame    = newFrame()
      screens["right"].frame   = newFrame(bcs_name & ", version: " & bcs_ver)
      screens["buttons"].frame = newFrame()

proc entryReg (window: Window, screens: Table[string, LayoutContainer], buttons: Table[string, Button], projects: ComboBox, project_label: Label) =
    block wScreens:
      window.add(screens["main"])
      screens["main"].add(screens["left"])
      screens["main"].add(screens["right"])
      screens["left"].add(screens["name"])
      screens["left"].add(screens["buttons"])
    block wButtons:
      screens["buttons"].add(buttons["enter"])
      screens["buttons"].add(buttons["add"])
      screens["buttons"].add(buttons["remove"])
    block wOther:
      screens["left"].add(project_label)
      screens["left"].add(projects)

proc entryDraw (screens: Table[string, LayoutContainer], images: Table[string, Image]) =
    #[ RIGHT SCREEN ]#
    screens["right"].onDraw = proc (event: DrawEvent) =
      let canvas = event.control.canvas
      canvas.drawImage(images["logo"], x=returnCell(5, AXES.X),
                                       y=returnCell(6, AXES.Y),
                                       width=returnCell(33, AXES.X))

    #[ LEFT SCREEN ]#
    screens["name"].onDraw = proc (event: DrawEvent) =
      let canvas = event.control.canvas
      canvas.drawText(bcs_name, x=returnCell(-0.25, AXES.X),
                                y=returnCell(0, AXES.Y))
      # canvas.drawText(bcs_ver, x=returnCell(0, AXES.X),
      #                          y=returnCell(10, AXES.Y))
      canvas.drawTextCentered(bcs_name, x=returnCell(-0.25, AXES.X),
                                        y=returnCell(0, AXES.Y),
                                        width=returnCell(10, AXES.X),
                                        height=returnCell(3, AXES.Y))
      canvas.drawTextCentered(bcs_ver, x=returnCell(2, AXES.X),
                                       y=returnCell(10, AXES.Y),
                                       width=returnCell(10, AXES.X),
                                       height=returnCell(3, AXES.Y))