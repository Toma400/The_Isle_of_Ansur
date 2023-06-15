import ../../bcs/img_manag
import ../../bcs/operators
import ../../init
import std/logging
import std/tables
import nigui

proc entryScreen* (window: Window, images: Table[string, Image], log: FileLogger) =
    var startScreen = newLayoutContainer(Layout_Horizontal)
    var landScreen  = newLayoutContainer(Layout_Vertical)
    var projScreen  = newLayoutContainer(Layout_Vertical)
    var logoScreen  = newLayoutContainer(Layout_Vertical)
    block sN: # screenNavigation
      block screenSettings:
        block landScreenSettings:
          landScreen.padding = 35
          landScreen.spacing = 3
          landScreen.xAlign  = XAlign_Center
          landScreen.frame   = newFrame()
          landScreen.setInnerSize(returnCell(33, AXES.X), returnCell(100, AXES.Y))
        block projScreenSettings:
          projScreen.padding = 25
          projScreen.spacing = 3
          projScreen.xAlign  = XAlign_Center
          projScreen.frame   = newFrame()
          projScreen.setInnerSize(returnCell(33, AXES.X), returnCell(100, AXES.Y))
        block logoScreenSettings:
          logoScreen.padding = 300
          logoScreen.spacing = 3
          logoScreen.xAlign  = XAlign_Center
          logoScreen.frame   = newFrame()
          logoScreen.setInnerSize(returnCell(33, AXES.X), returnCell(100, AXES.Y))
      block screenAdding:
        window.add(startScreen)     # main screen
        startScreen.add(landScreen)   # buttons
        startScreen.add(projScreen)   # project list
        startScreen.add(logoScreen)   # logo image

    var projLabel  = newLabel(langstr("login__listbox"))
    block lB: # labelsBoard
      projScreen.add(projLabel)
      projLabel.yTextAlign = YTextAlign_Center

    var projList = newComboBox(get_mods(PT.PROJECTS))
    projScreen.add(projList)

    var enterButton  = newButton(langstr("login__open"))
    var addButton    = newButton(langstr("login__add"))
    var removeButton = newButton(langstr("login__remove"))
    block bB: # buttonsBoard
      landScreen.add(enterButton)
      landScreen.add(addButton)
      landScreen.add(removeButton)

    logoScreen.onDraw = proc (event: DrawEvent) =
      let canvas = event.control.canvas
      block cO: # canvasOperations
        # canvas.areaColor = rgb(30, 30, 30) # dark grey
        # canvas.fill()
        canvas.drawImage(images["logo"], x=returnCell(20, AXES.X),
                                         y=returnCell(6, AXES.Y),
                                         width=returnCell(33, AXES.X))
        canvas.drawTextCentered(bcs_name, x=returnCell(30, AXES.X),
                                          y=returnCell(52, AXES.Y),
                                          width=returnCell(10, AXES.X),
                                          height=returnCell(3, AXES.Y))
        canvas.drawTextCentered(bcs_ver, x=returnCell(32, AXES.X),
                                         y=returnCell(55, AXES.Y),
                                         width=returnCell(10, AXES.X),
                                         height=returnCell(3, AXES.Y))

    enterButton.onClick = proc (event: ClickEvent) =
      log.log(lvlDebug, projList.value)