# standard lib
from enum import unique

# third-party
from attrs import define, field, validators

# mine
from .base import BaseEnumTemperature
from .errors import UnitsError

@unique
class TemperatureUnit(BaseEnumTemperature):
    # (symbol, absolute_zero)
    DEG_F = ('F', -459.67)
    DEG_C = ('C', -273.15)
    DEG_R = ('R', 0)
    DEG_K = ('K', 0)

    @property
    def unit_string(self):
        return self.value[0]

    @property
    def absolute_zero(self):
        return self.value[1]

@define
class Temperature:
    value: float = field()
    unit: TemperatureUnit = field(validator=validators.instance_of(TemperatureUnit))

    @property
    def unit_string(self):
        return self.unit.unit_string

    @property
    def absolute_zero(self):
        return self.unit.absolute_zero

    def change_units(self, to_unit: TemperatureUnit) -> float:
        # Change the value and units of the temperature
        self.value = Temperature.temperature_converter(self.value, self.unit, to_unit)
        self.unit = to_unit

    @staticmethod
    def temperature_converter(temperature: float, from_unit: TemperatureUnit, to_unit: TemperatureUnit) -> float:
        # Convert temperature from one unit to another
        if from_unit not in TemperatureUnit:
            raise UnitsError(f'Invalid from_unit {from_unit}.')
        if to_unit not in TemperatureUnit:
            raise UnitsError(f'Invalid to_unit {to_unit}.')
        if from_unit == to_unit:
            return temperature
        if from_unit == TemperatureUnit.DEG_F:
            if to_unit == TemperatureUnit.DEG_C:
                return Temperature.temperature_F_to_C(temperature)
            elif to_unit == TemperatureUnit.DEG_R:
                return Temperature.temperature_F_to_R(temperature)
            elif to_unit == TemperatureUnit.DEG_K:
                return Temperature.temperature_F_to_K(temperature)
        elif from_unit == TemperatureUnit.DEG_C:
            if to_unit == TemperatureUnit.DEG_F:
                return Temperature.temperature_C_to_F(temperature)
            elif to_unit == TemperatureUnit.DEG_R:
                return Temperature.temperature_C_to_R(temperature)
            elif to_unit == TemperatureUnit.DEG_K:
                return Temperature.temperature_C_to_K(temperature)
        elif from_unit == TemperatureUnit.DEG_R:
            if to_unit == TemperatureUnit.DEG_F:
                return Temperature.temperature_R_to_F(temperature)
            elif to_unit == TemperatureUnit.DEG_C:
                return Temperature.temperature_R_to_C(temperature)
            elif to_unit == TemperatureUnit.DEG_K:
                return Temperature.temperature_R_to_K(temperature)
        else:
            if to_unit == TemperatureUnit.DEG_F:
                return Temperature.temperature_K_to_F(temperature)
            elif to_unit == TemperatureUnit.DEG_C:
                return Temperature.temperature_K_to_C(temperature)
            elif to_unit == TemperatureUnit.DEG_R:
                return Temperature.temperature_K_to_R(temperature)

    ## Fahrenheit to X converters
    @staticmethod
    def temperature_F_to_C(temperature_F: float) -> float:
        # Convert degrees Fahrenheit to degrees Celsius
        if temperature_F < -459.67:
            raise ValueError('Invalid temperature. Must be >= -459.67 (F)')
        return (temperature_F - 32) * (5/9)

    @staticmethod
    def temperature_F_to_R(temperature_F: float) -> float:
        # Convert degrees Fahrenheit to degrees Rankine
        if temperature_F < -459.67:
            raise ValueError('Invalid temperature. Must be >= -459.67 (F)')
        return temperature_F + 459.67

    @staticmethod
    def temperature_F_to_K(temperature_F: float) -> float:
        # Convert degrees Fahrenheit to degrees Kelvin
        if temperature_F < -459.67:
            raise ValueError('Invalid temperature. Must be >= -459.67 (F)')
        return (temperature_F + 459.67) / 1.8

    ## Celcius to X converters

    @staticmethod
    def temperature_C_to_F(temperature_C: float) -> float:
        # Convert degrees Celsius to degrees Fahrenheit
        if temperature_C < -273.15:
            raise ValueError('Invalid temperature. Must be >= -273.15 (C)')
        return temperature_C * 1.8 + 32

    @staticmethod
    def temperature_C_to_K(temperature_C: float) -> float:
        # Convert degrees Celsius to Kelvin
        if temperature_C < -273.15:
            raise ValueError('Invalid temperature. Must be >= -273.15 (C)')
        return temperature_C + 273.15

    @staticmethod
    def temperature_C_to_R(temperature_C: float) -> float:
        # Convert degrees Celsius to degrees Rankine
        if temperature_C < -273.15:
            raise ValueError('Invalid temperature. Must be >= -273.15 (C)')
        return temperature_C * 1.8 + 491.67

    ## Rankine to X converters

    @staticmethod
    def temperature_R_to_F(temperature_R: float) -> float:
        # Convert degrees Rankine to degrees Fahrenheit
        if temperature_R < 0:
            raise ValueError('Invalid temperature. Must be >= 0 (R)')
        return temperature_R - 459.67

    @staticmethod
    def temperature_R_to_C(temperature_R: float) -> float:
        # Convert degrees Rankine to degrees Celsius
        if temperature_R < 0:
            raise ValueError('Invalid temperature. Must be >= 0 (R)')
        return temperature_R / 1.8 - 273.15

    @staticmethod
    def temperature_R_to_K(temperature_R: float) -> float:
        # Convert degrees Rankine to Kelvin
        if temperature_R < 0:
            raise ValueError('Invalid temperature. Must be >= 0 (R)')
        return temperature_R / 1.8

    ## Kelvin to X converters

    @staticmethod
    def temperature_K_to_F(temperature_K: float) -> float:
        # Convert Kelvin to degrees Fahrenheit
        if temperature_K < 0:
            raise ValueError('Invalid temperature. Must be >= 0 (K)')
        return temperature_K * 1.8 - 459.67

    @staticmethod
    def temperature_K_to_C(temperature_K: float) -> float:
        # Convert Kelvin to degrees Celsius
        if temperature_K < 0:
            raise ValueError('Invalid temperature. Must be >= 0 (K)')
        return temperature_K - 273.15

    @staticmethod
    def temperature_K_to_R(temperature_K: float) -> float:
        # Convert Kelvin to degrees Rankine
        if temperature_K < 0:
            raise ValueError('Invalid temperature. Must be >= 0 (K)')
        return temperature_K * 1.8