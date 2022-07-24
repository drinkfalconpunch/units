from unittest import TestCase

from utils.temperature import Temperature
from utils.enums import TemperatureUnit

class TestTemperature(TestCase):
    def test_temperature_convert(self):
        pass

    def test_absolute_zeros_equal(self):
        assert TemperatureUnit.DEG_F.absolute_zero == -459.67

    def test_change_units_and_inverse(self):
        pass

    def test_same_unit(self):
        assert Temperature.temperature_converter(0, TemperatureUnit.DEG_F, TemperatureUnit.DEG_F) == 0
        assert Temperature.temperature_converter(0, TemperatureUnit.DEG_C, TemperatureUnit.DEG_C) == 0
        assert Temperature.temperature_converter(0, TemperatureUnit.DEG_K, TemperatureUnit.DEG_K) == 0
        assert Temperature.temperature_converter(0, TemperatureUnit.DEG_R, TemperatureUnit.DEG_R) == 0
