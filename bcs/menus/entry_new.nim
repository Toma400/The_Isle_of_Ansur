import ../operators
import std/strutils
import std/logging
import std/tables
import std/os
import proj_main
import nigui

proc createNewProject* (bgwindow: Window, images: Table[string, Image], log: FileLogger) =
    let prL = get_mods(PT.PROJECTS)
    var window = newWindow(langstr("login__add"))
    windowInit(window, res=(300, 110))

    var tScreen = newLayoutContainer(Layout_Vertical)
    var cScreen = newLayoutContainer(Layout_Horizontal)

    var tField = newTextBox()
    var nButt  = newButton(langstr("login__add_new"))
    var cButt  = newButton(langstr("login__add_can"))

    window.add(tScreen)
    tScreen.add(tField)
    tScreen.add(cScreen)
    cScreen.add(nButt)
    cScreen.add(cButt)

    tScreen.xAlign = XAlign_Center

    tField.onTextChange = proc (event: TextChangeEvent) =
        if tField.text in prL:
            nButt.enabled = false
        else:
            nButt.enabled = true

    nButt.onClick = proc (event: ClickEvent) =
        nButt.enabled = false
        try:
          createDir(getCurrentDir() & "/bcs/projects/" & tField.text)
          log.log(lvlInfo, "Created new project of name '" & tField.text & "'.")
          enterProject(bgwindow, images, log, tField.text); window.dispose()
        except Exception:
          log.log(lvlError, "Couldn't create project with name '" & tField.text & "'. Reason:\n" & $getCurrentExceptionMsg())

    cButt.onClick = proc (event: ClickEvent) =
        window.dispose()

    window.show()