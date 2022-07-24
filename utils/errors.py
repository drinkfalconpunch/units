class UnitsError(Exception):
    pass

class TemperatureError(UnitsError):
    def invalid_temperature(self, value, unit):
        raise TemperatureError(f"Invalid temperature. Must be >= {unit.absolute_zero} {unit.symbol}: {value}")

    def invalid_unit(self, unit):
        raise TemperatureError(f"Invalid temperature unit: {unit}")