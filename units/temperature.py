# standard lib
from collections import namedtuple

# third-party
from attrs import define, field, validators

# mine
from .errors import TemperatureError
from .enums import TemperatureUnit


@define
class Temperature:
    value: float = field()
    unit: TemperatureUnit = field() #validator=validators.instance_of(TemperatureUnit))

    @unit.validator
    def _check_unit(self, attribute, value):
        if value not in TemperatureUnit:
            raise TemperatureError.invalid_unit(value)

    @property
    def symbol(self) -> str:
        return self.unit.symbol

    @property
    def absolute_zero(self) -> float:
        return self.unit.absolute_zero

    def change_units(self, to_unit: TemperatureUnit) -> None:
        # Change the value and units of the temperature
        self.value = Temperature.temperature_converter(self.value, self.unit, to_unit)
        self.unit = to_unit

    @staticmethod
    def is_valid_temperature(temperature: float, unit: TemperatureUnit) -> bool:
        return temperature >= unit.absolute_zero

    @staticmethod
    def temperature_converter(temperature: float, from_unit: TemperatureUnit, to_unit: TemperatureUnit) -> float:
        # Convert temperature from one unit to another
        # if isinstance(from_unit, str):
        #     from_unit = TemperatureUnit[from_unit]
        # if isinstance(to_unit, str):
        #     to_unit = TemperatureUnit[to_unit]
        if from_unit not in TemperatureUnit:
            raise TemperatureError.invalid_unit(from_unit)
        if to_unit not in TemperatureUnit:
            raise TemperatureError.invalid_unit(to_unit)
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
        if not Temperature.is_valid_temperature(temperature_F, TemperatureUnit.DEG_F):
            raise TemperatureError.invalid_temperature(temperature_F, TemperatureUnit.DEG_F)
        return (temperature_F - 32) * (5/9)

    @staticmethod
    def temperature_F_to_R(temperature_F: float) -> float:
        # Convert degrees Fahrenheit to degrees Rankine
        if not Temperature.is_valid_temperature(temperature_F, TemperatureUnit.DEG_F):
            raise TemperatureError.invalid_temperature(temperature_F, TemperatureUnit.DEG_F)
        return temperature_F + 459.67

    @staticmethod
    def temperature_F_to_K(temperature_F: float) -> float:
        # Convert degrees Fahrenheit to degrees Kelvin
        if not Temperature.is_valid_temperature(temperature_F, TemperatureUnit.DEG_F):
            raise TemperatureError.invalid_temperature(temperature_F, TemperatureUnit.DEG_F)
        return (temperature_F + 459.67) / 1.8

    ## Celcius to X converters

    @staticmethod
    def temperature_C_to_F(temperature_C: float) -> float:
        # Convert degrees Celsius to degrees Fahrenheit
        if not Temperature.is_valid_temperature(temperature_C, TemperatureUnit.DEG_C):
            raise TemperatureError.invalid_temperature(temperature_C, TemperatureUnit.DEG_C)
        return temperature_C * 1.8 + 32

    @staticmethod
    def temperature_C_to_K(temperature_C: float) -> float:
        # Convert degrees Celsius to Kelvin
        if not Temperature.is_valid_temperature(temperature_C, TemperatureUnit.DEG_C):
            raise TemperatureError.invalid_temperature(temperature_C, TemperatureUnit.DEG_C)
        return temperature_C + 273.15

    @staticmethod
    def temperature_C_to_R(temperature_C: float) -> float:
        # Convert degrees Celsius to degrees Rankine
        if not Temperature.is_valid_temperature(temperature_C, TemperatureUnit.DEG_C):
            raise TemperatureError.invalid_temperature(temperature_C, TemperatureUnit.DEG_C)
        return temperature_C * 1.8 + 491.67

    ## Rankine to X converters

    @staticmethod
    def temperature_R_to_F(temperature_R: float) -> float:
        # Convert degrees Rankine to degrees Fahrenheit
        if not Temperature.is_valid_temperature(temperature_R, TemperatureUnit.DEG_R):
            raise TemperatureError.invalid_temperature(temperature_R, TemperatureUnit.DEG_R)
        return temperature_R - 459.67

    @staticmethod
    def temperature_R_to_C(temperature_R: float) -> float:
        # Convert degrees Rankine to degrees Celsius
        if not Temperature.is_valid_temperature(temperature_R, TemperatureUnit.DEG_R):
            raise TemperatureError.invalid_temperature(temperature_R, TemperatureUnit.DEG_R)
        return temperature_R / 1.8 - 273.15

    @staticmethod
    def temperature_R_to_K(temperature_R: float) -> float:
        # Convert degrees Rankine to Kelvin
        if not Temperature.is_valid_temperature(temperature_R, TemperatureUnit.DEG_R):
            raise TemperatureError.invalid_temperature(temperature_R, TemperatureUnit.DEG_R)
        return temperature_R / 1.8

    ## Kelvin to X converters

    @staticmethod
    def temperature_K_to_F(temperature_K: float) -> float:
        # Convert Kelvin to degrees Fahrenheit
        if not Temperature.is_valid_temperature(temperature_K, TemperatureUnit.DEG_K):
            raise TemperatureError.invalid_temperature(temperature_K, TemperatureUnit.DEG_K)
        return temperature_K * 1.8 - 459.67

    @staticmethod
    def temperature_K_to_C(temperature_K: float) -> float:
        # Convert Kelvin to degrees Celsius
        if not Temperature.is_valid_temperature(temperature_K, TemperatureUnit.DEG_K):
            raise TemperatureError.invalid_temperature(temperature_K, TemperatureUnit.DEG_K)
        return temperature_K - 273.15

    @staticmethod
    def temperature_K_to_R(temperature_K: float) -> float:
        # Convert Kelvin to degrees Rankine
        if not Temperature.is_valid_temperature(temperature_K, TemperatureUnit.DEG_K):
            raise TemperatureError.invalid_temperature(temperature_K, TemperatureUnit.DEG_K)
        return temperature_K * 1.8