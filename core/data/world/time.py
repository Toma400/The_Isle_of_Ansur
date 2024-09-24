from core.gui.manag.langstr import langstring
import logging as log

TICK_LIMIT = 60 # should be average tick amount per second (20?) * amount of seconds needed to pass (15 seconds as default "minute")
MDS = { # month day limits
    1:  31,
    2:  28,
    3:  31,
    4:  30,
    5:  31,
    6:  30,
    7:  31,
    8:  31,
    9:  30,
    10: 31,
    11: 30,
    12: 31
}

class BaeTime:

    def __init__(self, s: (int, int, int, int, int, int, int)):
        self.era   = s[0]
        self.year  = s[1]
        self.month = s[2]
        self.day   = s[3]
        self.wday  = s[4]
        self.hour  = s[5]
        self.min   = s[6]
        self.tick  = 0

    def asStr(self, mode: int = 0) -> str:
        match mode:
            case 0: return f"{self.day} {langstring(f'time__month_{self.month}')} {self.year}"
            case 1: return f"{langstring(f'time__week_{self.wday}')}, {self.hour}:{self.min:02}"

    def incr(self, dt: float) -> bool:
        """Return handling is optional | returns True if limit is exceeded (should be condition for file save)"""
        TL = int(30 // dt) # tick limit
        self.tick += 1
        return self.check(TL)

    def check(self, tl: int) -> bool:
        if self.tick > tl:
            self.min += 1
            self.tick = 0
            if self.min > 59:
                h, m = divmod(self.min, 60) # allows stacking hours
                self.hour += h
                self.min   = m
                if self.hour > 23:
                    d, h = divmod(self.hour, 24) # allows stacking days
                    self.day  += d
                    self.wday += d
                    self.hour  = h
                    if self.wday > 7:
                        _, r = divmod(self.wday, 7)
                        self.wday = r
                    if self.day > (MDS[self.month]):
                        m, d = divmod(self.day, MDS[self.month]) # allows stacking months
                        self.month += m
                        self.day    = d
                        if self.month > 12:
                            y, m = divmod(self.month, 12)# allows stacking years
                            self.year += y
                            self.month = m
            return True
        return False

def parseBaeTime(s: list[int, int, int, int, int, int, int] | None) -> BaeTime | None:
    if s is not None:
        try:
            return BaeTime((s[0],
                            s[1],
                            s[2],
                            s[3],
                            s[4],
                            s[5],
                            s[6]))
        except:
            log.error(f"Couldn't parse string: [{s}]. Invalid BaeTime format.")
    return None