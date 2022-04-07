#----------------------------------------------------------------------
# GUI PACKAGE
# Gui Package is main package used in-game, containing all main
# packages that are interacting with player (by printing messages
# and being some sort of interface).
#
# MENU.PY
# Main menu, nothing really big to explain
#
# CHARACTER.PY
# Character Package is used for character creation and it's first
# package being run after running menu.py into new game.
#
# INTERFACE.PY
# Interface Package handles most of the game, showing player elements
# such as map, actions and so on. It should mostly reference elements,
# so it's less of a holder, more of a linker.
#
# INVENTORY.PY
# Submodule of Inteface, for handling all inventory management of the
# player.
#----------------------------------------------------------------------