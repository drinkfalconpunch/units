from enum import Enum, unique
from collections import namedtuple
from typing import Self

from .errors import UnitsError

TemperatureScale = namedtuple("TemperatureScale", ["symbol", "absolute_zero"])

@unique
class TemperatureUnit(Enum):
    DEG_F = TemperatureScale("F", -459.67)
    DEG_C = TemperatureScale("C", -273.15)
    DEG_R = TemperatureScale("R", 0)
    DEG_K = TemperatureScale("K", 0)

    @property
    def symbol(self) -> str:
        return self.value.symbol

    @property
    def absolute_zero(self) -> float:
        return self.value.absolute_zero

    @classmethod
    def from_symbol(cls, unit_str: str) -> Self:
        """Lookup a TemperatureUnit by its symbol."""
        if not isinstance(unit_str, str):
            raise ValueError(f"Temperature unit must be a string: {unit_str}.")
        
        unit_str = unit_str.upper()
        for unit in cls:
            if unit.symbol == unit_str:
                return unit

        raise ValueError(f"Invalid temperature unit: {unit_str}.")

if __name__ == "__main__":
    # Testing
    a = TemperatureUnit.from_symbol("C")  # Works
    print(a, a.symbol, a.absolute_zero)
