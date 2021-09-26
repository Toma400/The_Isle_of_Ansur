def text_align (text, side, width):
  if side == "left":
    str.ljust(text, width, " ")
  elif side == "right":
    str.rjust(text, width, " ")
  elif side == "centre":
    str.center(text, width, " ")
  else:
    print ("Alignment error")