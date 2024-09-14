from distutils.dir_util import copy_tree

def saveBuffer(name: str):
    """Saves -buffer- contents into -adventure- format"""
    copy_tree(f"saves/{name}/buffer", f"saves/{name}/adventure")

def saveBufferCyclical(name: str):
    """Saves -buffer- contents into -cyclical- format"""
    copy_tree(f"saves/{name}/buffer", f"saves/{name}/cyclical")

def loadBuffer(name: str):
    """Loads -adventure- contents by overwriting buffer"""
    copy_tree(f"saves/{name}/adventure", f"saves/{name}/buffer")

def loadBufferCyclical(name: str):
    """Loads -cyclical- contents by overwriting buffer"""
    copy_tree(f"saves/{name}/cyclical", f"saves/{name}/buffer")