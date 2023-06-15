import ../../bcs/img_manag
import ../../bcs/operators
import ../../init
import std/strutils
import std/logging
import std/tables
import nigui
# pre-loading later functions
proc entryReg      (window: Window, screens: Table[string, LayoutContainer], buttons: Table[string, Button], projects: ComboBox, project_label: Label)
proc entrySettings (screens: Table[string, LayoutContainer])

#[ --- MAIN BODY --- ]#
proc entryScreen* (window: Window, images: Table[string, Image], log: FileLogger) =
    let mainScreen = newLayoutContainer(Layout_Horizontal)
    let left       = newLayoutContainer(Layout_Vertical)
    let right      = newLayoutContainer(Layout_Vertical)
    let bScreen    = newLayoutContainer(Layout_Vertical) # buttons
    let screens    = { "main":  mainScreen, "left":  left, "right": right, "buttons": bScreen }.toTable

    let enterButton  = newButton(langstr("login__open"))
    let addButton    = newButton(langstr("login__add"))
    let removeButton = newButton(langstr("login__remove"))
    let buttons      = { "enter": enterButton, "add": addButton, "remove": removeButton }.toTable

    let projLabel = newLabel(langstr("login__listbox"))
    let projList  = newComboBox(get_mods(PT.PROJECTS))

    #[ TODO:
      - logo img
    ]#


    # var startScreen = newLayoutContainer(Layout_Horizontal)
    # var landScreen  = newLayoutContainer(Layout_Vertical)
    # var projScreen  = newLayoutContainer(Layout_Vertical)
    # var logoScreen  = newLayoutContainer(Layout_Vertical)
    # block sN: # screenNavigation
    #   block screenSettings:
    #     block landScreenSettings:
    #       landScreen.padding = 35
    #       landScreen.spacing = 3
    #       landScreen.xAlign  = XAlign_Center
    #       landScreen.frame   = newFrame()
    #       landScreen.setInnerSize(returnCell(33, AXES.X), returnCell(100, AXES.Y))
    #     block projScreenSettings:
    #       projScreen.padding = 25
    #       projScreen.spacing = 3
    #       projScreen.xAlign  = XAlign_Center
    #       projScreen.frame   = newFrame()
    #       projScreen.setInnerSize(returnCell(33, AXES.X), returnCell(100, AXES.Y))
    #     block logoScreenSettings:
    #       logoScreen.padding = 300
    #       logoScreen.spacing = 3
    #       logoScreen.xAlign  = XAlign_Center
    #       logoScreen.frame   = newFrame()
    #       logoScreen.setInnerSize(returnCell(33, AXES.X), returnCell(100, AXES.Y))
    #   block screenAdding:
    #     window.add(startScreen)     # main screen
    #     startScreen.add(landScreen)   # buttons
    #     startScreen.add(projScreen)   # project list
    #     startScreen.add(logoScreen)   # logo image
    #

    # block lB: # labelsBoard
    #   projScreen.add(projLabel)
    #   projLabel.yTextAlign = YTextAlign_Center
    #
    #
    # block bB: # buttonsBoard
    #   landScreen.add(enterButton)
    #   landScreen.add(addButton)
    #   landScreen.add(removeButton)

    right.onDraw = proc (event: DrawEvent) =
      let canvas = event.control.canvas
    #block cO: # canvasOperations
      # canvas.areaColor = rgb(30, 30, 30) # dark grey
      # canvas.fill()
      canvas.drawImage(images["logo"], x=returnCell(20, AXES.X),
                                       y=returnCell(6, AXES.Y),
                                       width=returnCell(33, AXES.X))
      # canvas.drawTextCentered(bcs_name, x=returnCell(30, AXES.X),
      #                                   y=returnCell(52, AXES.Y),
      #                                   width=returnCell(10, AXES.X),
      #                                   height=returnCell(3, AXES.Y))
      # canvas.drawTextCentered(bcs_ver, x=returnCell(32, AXES.X),
      #                                  y=returnCell(55, AXES.Y),
      #                                  width=returnCell(10, AXES.X),
      #                                  height=returnCell(3, AXES.Y))
    #
    # enterButton.onClick = proc (event: ClickEvent) =
    #   log.log(lvlDebug, projList.value)

    entrySettings(screens)
    entryReg(window, screens, buttons, projList, projLabel)

proc entrySettings (screens: Table[string, LayoutContainer]) =
    block wAlign:
      screens["left"].xAlign    = XAlign_Center #.setInnerSize((parseInt(settings("res_x"))/2).int,  (parseInt(settings("res_y"))))
      screens["right"].xAlign   = XAlign_Center #.setInnerSize((parseInt(settings("res_x"))/2).int, (parseInt(settings("res_y"))))
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
      screens["left"].add(screens["buttons"])
    block wButtons:
      screens["buttons"].add(buttons["enter"])
      screens["buttons"].add(buttons["add"])
      screens["buttons"].add(buttons["remove"])
    block wOther:
      screens["left"].add(project_label)
      screens["left"].add(projects)