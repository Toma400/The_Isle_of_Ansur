scr_res = 900

def returnCell(pos):
    mod = scr_res / 100
    return int(pos * mod)

def returnCells(pos: tuple):
    mod = scr_res / 100
    return int(pos[0] * mod), int(pos[1] * mod)

def revCell(pos):
    mod = scr_res / 100
    return int(pos / mod)

def revCells(pos: tuple):
    mod = scr_res / 100
    return int(pos[0] / mod), int(pos[1] / mod)