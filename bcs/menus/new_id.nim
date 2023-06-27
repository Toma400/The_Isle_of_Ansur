import ../operators
import ../project
import std/logging
import results
import nigui

proc notifID (r: R) =
    #[ if OK = small window with OK; if ERR = small window with ERR ]#
    #if r.err
    discard

proc createNewID* (bgwindow: Skylight, pj: IoaProject) =
    var window = newWindow(langstr("project__add"))
    windowInit(window, res=(300, 110))

    var tScreen = newLayoutContainer(Layout_Vertical)
    var cScreen = newLayoutContainer(Layout_Horizontal)

    var tField = newTextBox()
    var nButt  = newButton(langstr("project__add_new"))
    var cButt  = newButton(langstr("project__add_can"))

    window.add(tScreen)
    tScreen.add(tField)
    tScreen.add(cScreen)
    cScreen.add(nButt)
    cScreen.add(cButt)

    tScreen.xAlign = XAlign_Center

    tField.onTextChange = proc (event: TextChangeEvent) =
        if tField.text in pj.ids:
            nButt.enabled = false
        else:
            nButt.enabled = true

    nButt.onClick = proc (event: ClickEvent) =
        nButt.enabled = false
        window.dispose()
        # notifID(newID(tField.text))

    cButt.onClick = proc (event: ClickEvent) =
        window.dispose()

    window.show()