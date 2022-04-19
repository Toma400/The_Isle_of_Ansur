import logging

#--------------------------------------
# RUN
# Default config being run, with values
# set later in this module
#--------------------------------------
def run():
    logging.basicConfig(level=logging.DEBUG, filename=name_creating(), format=format_creating())

def name_creating(name=""):
    import time
    name_list = ["system/logs/",
                 (time.gmtime(time.time()).tm_year), "_",
                 (time.gmtime(time.time()).tm_mon), "_",
                 (time.gmtime(time.time()).tm_mday), "_",
                 (time.gmtime(time.time()).tm_hour), "_",
                 (time.gmtime(time.time()).tm_min), "_",
                 (time.gmtime(time.time()).tm_sec), "_log.log"]
    for i in name_list:
        name = name + str(i)
    return name

def format_creating(text=""):
    format_list = ["[",
                   "%(asctime)s", "] [",
                   "%(levelname)s", "] [",
                   "%(message)s", "]"]
    for i in format_list:
        text = text + str(i)
    return text
