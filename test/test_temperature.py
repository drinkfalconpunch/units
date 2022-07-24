from unittest import TestCase

from pytest import approx, raises

from utils.temperature import Temperature
from utils.errors import UnitsError
from utils.enums import TemperatureUnit

class TestTemperature(TestCase):
    def test_convert_units_and_inverse(self):
        """
        Check that converting to a different unit and back returns the original value.
        """
        for unit_a in TemperatureUnit:
            for unit_b in TemperatureUnit:
                if unit_a == unit_b:
                    continue
                value_a = Temperature.temperature_converter(0, unit_a, unit_b)
                value_b = Temperature.temperature_converter(value_a, unit_b, unit_a)
                assert approx(value_b) == 0

    def test_convert_same_unit(self):
        """
        Check that converting to the same unit returns the same value.
        """
        assert Temperature.temperature_converter(0, TemperatureUnit.DEG_F, TemperatureUnit.DEG_F) == 0
        assert Temperature.temperature_converter(0, TemperatureUnit.DEG_C, TemperatureUnit.DEG_C) == 0
        assert Temperature.temperature_converter(0, TemperatureUnit.DEG_K, TemperatureUnit.DEG_K) == 0
        assert Temperature.temperature_converter(0, TemperatureUnit.DEG_R, TemperatureUnit.DEG_R) == 0

    def test_invalid_unit(self):
        """
        Check that an invalid unit raises an error.
        """
        with raises(UnitsError):
            TemperatureUnit['invalid']