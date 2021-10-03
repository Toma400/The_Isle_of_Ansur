class in_use:

  def default_settings(callout=None):
    time_system = "proportional"
    hunger_thirst = False
    if callout == "time_system":
      return time_system
    elif callout == "hunger_thirst":
      return hunger_thirst