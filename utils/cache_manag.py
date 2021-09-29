def cache_deleting():
  try:
    import utils.repo_manag
    utils.repo_manag.file_deleting ("stats/__pycache__")
    utils.repo_manag.file_deleting ("utils/__pycache__")
    utils.repo_manag.file_deleting ("gui/__pycache__")
    utils.repo_manag.file_deleting ("saves/__pycache__")
    utils.repo_manag.file_deleting ("system/__pycache__")
    del utils.repo_manag
  except AttributeError:
    pass