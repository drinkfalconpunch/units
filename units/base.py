# https://stackoverflow.com/a/65225753/10107786
from enum import Enum, EnumMeta

from .helpers import isiterable

class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True

class MetaEnumTemperature(MetaEnum):
    """Since we're storing the values of absolute zero with the symbols, split
    out the values and only check for the symbols/strings, i.e. 'C' or 'R'."""
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            try:
                if not isinstance(item, str):
                    return False
                for _, member in cls.__members__.items():
                    if isiterable(member.value):
                        if item in member.value:
                            return True
            except ValueError:
                return False
            return False
        return True


class BaseEnum(Enum, metaclass=MetaEnum):
    pass

class BaseEnumTemperature(Enum, metaclass=MetaEnumTemperature):
    pass