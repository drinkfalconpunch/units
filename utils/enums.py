from enum import Enum, unique
from collections import namedtuple

TemperatureScale = namedtuple('TemperatureScale', ['symbol', 'absolute_zero'])

@unique
class TemperatureUnit(Enum):
    DEG_F = TemperatureScale('F', -459.67)
    DEG_C = TemperatureScale('C', -273.15)
    DEG_R = TemperatureScale('R', 0)
    DEG_K = TemperatureScale('K', 0)

    @property
    def symbol(self) -> str:
        return self.value.symbol

    @property
    def absolute_zero(self) -> float:
        return self.value.absolute_zero