# ------- NIM BCSET -------
import bcs/operators
import std/sequtils
import nigui # either this
import lapis
import os

# --- UTIL ELEMENTS ---
let bcs_name = "Baedoor Creation Set"

let mods_files = get_files("mods/")
let proj_files = get_files("bcs/projects/")
proc list(files: seq[string]) = # prints the above, util proc
  for i in files:
    echo i

# --- BCS MAIN RUN ---
app.init()

echo settings("res_x")

var window = newWindow(bcs_name)
block wS: # windowScreen
  window.width    = ti(settings("res_x"))
  window.height   = ti(settings("res_y"))
  window.iconPath = bcsd() & "/bcs/assets/graphical/bcsx.png"

var projScreen = newLayoutContainer(Layout_Vertical)
block pLS: # projectListScreen
  projScreen.padding = 6
  window.add(projScreen)

window.show()
app.run()