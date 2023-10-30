from core.decorators import Callable, HelperMethod
from core.utils import gpath, scx
from enum import Enum

class TextKind(Enum):
    RAW             = 0
    TRANSLATED_MAIN = 1
    TRANSLATED_PACK = 2

class Text:

    pass

    # def __init__(self, text: str, is_raw: bool = False):
    #     """
    #     text   | Raw text or language key
    #     is_raw | Indicates whether 'text' should be treated as raw or use language key
    #            | :: defaults to 'False'
    #     """
    #     self.key  : str      = text
    #     self.kind : TextKind = TextKind.RAW if is_raw else TextKind.TRANSLATED
    #     self.text : str      = self.textHelper()
    #
    # # @Callable #TODO! Has quite important difference compared to 'text_manag/Text.langstring' at line 2-3
    # # def langstring(self) -> str:
    # #     """Converts -text- passed to the value of respective key in main language file"""
    # #     import toml; t = toml.load(f"{gpath}/core/lang/{scx('lang')}.toml")
    # #     return t[self.key]
    # #
    # # @Callable #TODO! Has quite important difference compared to 'text_manag/Text.langstring' at line 2-3
    # # def langjstring(self, modtype: str, modid: str = "ansur") -> str:
    # #     """Converts -text- passed to the value of respective key in language file of pack with specified type & ID"""
    # #     try: read = json_read(f"{modtype}/{modid}/lang.json", self.lang)
    # #     except KeyError:
    # #         try: read = json_read(f"{modtype}/{modid}/lang.json", "english")
    # #         except KeyError:
    # #             log.warning(
    # #                 f"Module {modid} does not have properly set language value for {self.key}. Please contact the developer of this module for help.")
    # #             return langstring("system__text_load_fail")
    # #     return read[self.key]
    #
    # @HelperMethod
    # def textHelper(self) -> str:
    #     match self.kind:
    #       case TextKind.RAW:             return self.key
    #       case TextKind.TRANSLATED_MAIN: return self.langstring()
    #       case TextKind.TRANSLATED_PACK: return self.langjstring()