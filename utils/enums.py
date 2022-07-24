from __future__ import annotations

from enum import Enum, EnumMeta, unique
from collections import namedtuple

from .errors import UnitsError

TemperatureScale = namedtuple('TemperatureScale', ['symbol', 'absolute_zero'])

class TemperatureUnitMeta(EnumMeta):
    def __getitem__(cls, unit_str: str) -> TemperatureUnit:
        try:
            return super.__getitem__(unit_str)
        except (KeyError, TypeError):
            print(unit_str)
            if not isinstance(unit_str, str):
                raise ValueError(f"Temperature unit must be string: {unit_str}.")
            print("units")
            units = [u for u in TemperatureUnit]
            for unit in units:
                if unit.symbol == unit_str.upper():
                    return unit
            raise ValueError(f"Invalid temperature unit: {unit_str}.")

@unique
class TemperatureUnit(Enum):
    DEG_F = TemperatureScale('F', -459.67)
    DEG_C = TemperatureScale('C', -273.15)
    DEG_R = TemperatureScale('R', 0)
    DEG_K = TemperatureScale('K', 0)

    @property
    def symbol(cls) -> str:
        return cls.value.symbol

    @property
    def absolute_zero(cls) -> float:
        return cls.value.absolute_zero

if __name__ == "__main__":
    # testing indexing with enums
    a = TemperatureUnit['C']