def text_align (text, side):
  if side == "left":
    aligned = '{:<65}'.format(text)
    return aligned
  elif side == "right":
    aligned = '{:>65}'.format(text)
    return aligned
  elif side == "centre":
    aligned = '{:^65}'.format(text)
    return aligned
  else:
    print ("Alignment error")