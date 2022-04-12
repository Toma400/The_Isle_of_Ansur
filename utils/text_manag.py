class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' #for normal writing
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m' #for technical warnings
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m' #for in-game warnings, not bugs/crashes
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'
#class call: bcolors.HEADER

#------------------------------------------------------------------
# TEXT FORMATTERS
#------------------------------------------------------------------
def colour_formatter(colour, text, alignment="centre", keying="c"):
    # ------------------------
    # colour bounding
    if colour == "red":
        text = bcolors.CRED + text + bcolors.ENDC
    if colour == "blue":
        text = bcolors.CBLUE + text + bcolors.ENDC
    if colour == "blue+":
        text = bcolors.OKBLUE + text + bcolors.ENDC
    if colour == "green":
        text = bcolors.CGREEN + text + bcolors.ENDC
    if colour == "violet":
        text = bcolors.CVIOLET + text + bcolors.ENDC
    if colour == "cyan":
        text = bcolors.OKCYAN + text + bcolors.ENDC
    if colour == "yellow":
        text = bcolors.CYELLOW2 + text + bcolors.ENDC
    #------------------------
    #alignment bounding
    if alignment == "centre":
        text = align(text, "centre_colour")
    elif alignment == "left":
        text = align(text, "left_colour")
    return text

#---------------------------------------------------
# TEXT ALIGN
# Used to align text to specific part of the console
# Takes a bit different values if used with colours
#---------------------------------------------------
def align (text, side="centre"):
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
  elif side == "centre_colour+":
    aligned = '{:^85}'.format(text)
    return aligned
  else:
    print ("Alignment error")