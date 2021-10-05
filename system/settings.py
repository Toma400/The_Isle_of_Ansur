class in_use:

  def default_settings(callout=None):
    time_system = "proportional"
    hunger_thirst = False
    if callout == "time_system":
      return time_system
    elif callout == "hunger_thirst":
      return hunger_thirst

  def version_call(selector):
    if selector == "game version":
      return "pre-alpha 1"
    elif selector == "save system":
      import stats.default_stats
      return stats.default_stats.version_checker()