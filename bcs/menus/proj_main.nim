import ../../bcs/operators
import std/logging
import std/tables
import nigui

proc mainProjScreen* (window: Window, images: Table[string, Image], log: FileLogger, pj_name: string) =
    windowInit(window) # update for entryScreen
    let mainScreen = newLayoutContainer(Layout_Horizontal)

    let scrButton = newButton(langstr("project__scripts"))

proc mainProjSettings () =
    discard

proc mainProjReg () =
    discard

proc mainProjDraw () =
    discard

proc enterProject* (window: Window, images: Table[string, Image], log: FileLogger, pj_name: string) =
    log.log(lvlInfo, "Entering the project with name -" & pj_name & "-")
    windowUpdate(window, bcs_name & ": " & pj_name)
    mainProjScreen(window, images, log, pj_name)