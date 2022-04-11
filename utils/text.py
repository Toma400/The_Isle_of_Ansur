@DeprecationWarning
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
  elif side == "left_colour":
    aligned = '{:<75}'.format(text)
    return aligned
  elif side == "right_colour":
    aligned = '{:>75}'.format(text)
    return aligned
  elif side == "centre_colour":
    aligned = '{:^75}'.format(text)
    return aligned
  else:
    print ("Alignment error")