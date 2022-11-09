import functools
import logging

def SoftDeprecated(func):
    """Used to indicate functions with flaws, but having no direct alternatives, so user need to come up with their own solutions"""
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        logging.debug(f'''
        Used function marked as soft-deprecated: [{func.__name__}].
        It is recommended to not use it, if there's a way to create code in clearer way, but this function will work normally.
        Soft-deprecation is used for features that can't be put other way, but their current implementation is code-inefficient.
        ''')
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_func


def Deprecated(func_rdir: str = None):
    """Used for functions which are no longer supported and may be removed in future versions (contrary to @DeprecationWarning, allows for run)"""
    def DecDeprecated(func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            logging.debug(f'''
            Used deprecated function: [{func.__name__}].
            It is recommended to not use it and update your code, as deprecated functions are not getting any support and have most
            likely their alternatives already. Code will work, but can break in future versions.

            If there's recommended alternative for the function, it is written below:
            ----
            Recommended alternative for deprecated function (module.func path): [{func_rdir}].
            ----
            ''')
            func(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper_func

    return DecDeprecated


def RequiresImprovement(func):
    """Serves as a placeholder decorator to signify code which is not readable enough"""

    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_func

def HelperMethod(func):
    """Serves as indicator that the function is not destined to be used outside of the class (i.e. being called by instance)"""

    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_func

def Callable(func):
    """Used for class methods which return self - signifies methods which can be used during object initialising (onelined)"""

    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
        return args[0]

    return wrapper_func