def temperature_converter(temperature: float, from_unit: str, to_unit: str) -> float:
    # Convert temperature from one unit to another
    units = set(['F', 'C', 'R', 'K'])
    if from_unit not in units or to_unit not in units:
        raise ValueError('Invalid unit')
    if from_unit.upper() == to_unit.upper():
        return temperature
    if from_unit.upper() == 'F':
        if to_unit.upper() == 'C':
            return temperature_F_to_C(temperature)
        elif to_unit.upper() == 'R':
            return temperature_F_to_R(temperature)
        elif to_unit.upper() == 'K':
            return temperature_F_to_K(temperature)
    elif from_unit.upper() == 'C':
        if to_unit.upper() == 'F':
            return temperature_C_to_F(temperature)
        elif to_unit.upper() == 'R':
            return temperature_C_to_R(temperature)
        elif to_unit.upper() == 'K':
            return temperature_C_to_K(temperature)
    elif from_unit.upper() == 'R':
        if to_unit.upper() == 'F':
            return temperature_R_to_F(temperature)
        elif to_unit.upper() == 'C':
            return temperature_R_to_C(temperature)
        elif to_unit.upper() == 'K':
            return temperature_R_to_K(temperature)
    else:
        # from_unit.upper() == 'K'
        if to_unit.upper() == 'F':
            return temperature_K_to_F(temperature)
        elif to_unit.upper() == 'C':
            return temperature_K_to_C(temperature)
        elif to_unit.upper() == 'R':
            return temperature_K_to_R(temperature)


## Fahrenheit to X converters

def temperature_F_to_C(temperature_F: float) -> float:
    # Convert degrees Fahrenheit to degrees Celsius
    if temperature_F < -459.67:
        raise ValueError('Invalid temperature. Must be >= -459.67 (F)')
    return (temperature_F - 32) * (5/9)

def temperature_F_to_R(temperature_F: float) -> float:
    # Convert degrees Fahrenheit to degrees Rankine
    if temperature_F < -459.67:
        raise ValueError('Invalid temperature. Must be >= -459.67 (F)')
    return temperature_F + 459.67

def temperature_F_to_K(temperature_F: float) -> float:
    # Convert degrees Fahrenheit to degrees Kelvin
    if temperature_F < -459.67:
        raise ValueError('Invalid temperature. Must be >= -459.67 (F)')
    return (temperature_F + 459.67) / 1.8

## Celcius to X converters

def temperature_C_to_F(temperature_C: float) -> float:
    # Convert degrees Celsius to degrees Fahrenheit
    if temperature_C < -273.15:
        raise ValueError('Invalid temperature. Must be >= -273.15 (C)')
    return temperature_C * 1.8 + 32

def temperature_C_to_K(temperature_C: float) -> float:
    # Convert degrees Celsius to Kelvin
    if temperature_C < -273.15:
        raise ValueError('Invalid temperature. Must be >= -273.15 (C)')
    return temperature_C + 273.15

def temperature_C_to_R(temperature_C: float) -> float:
    # Convert degrees Celsius to degrees Rankine
    if temperature_C < -273.15:
        raise ValueError('Invalid temperature. Must be >= -273.15 (C)')
    return temperature_C + 491.67

## Rankine to X converters

def temperature_R_to_F(temperature_R: float) -> float:
    # Convert degrees Rankine to degrees Fahrenheit
    if temperature_R < 0:
        raise ValueError('Invalid temperature. Must be >= 0 (R)')
    return temperature_R - 459.67

def temperature_R_to_C(temperature_R: float) -> float:
    # Convert degrees Rankine to degrees Celsius
    if temperature_R < 0:
        raise ValueError('Invalid temperature. Must be >= 0 (R)')
    return temperature_R - 491.67

def temperature_R_to_K(temperature_R: float) -> float:
    # Convert degrees Rankine to Kelvin
    if temperature_R < 0:
        raise ValueError('Invalid temperature. Must be >= 0 (R)')
    return temperature_R / 1.8

## Kelvin to X converters

def temperature_K_to_F(temperature_K: float) -> float:
    # Convert Kelvin to degrees Fahrenheit
    if temperature_K < 0:
        raise ValueError('Invalid temperature. Must be >= 0 (K)')
    return temperature_K * 1.8 - 459.67

def temperature_K_to_C(temperature_K: float) -> float:
    # Convert Kelvin to degrees Celsius
    if temperature_K < 0:
        raise ValueError('Invalid temperature. Must be >= 0 (K)')
    return temperature_K - 273.15

def temperature_K_to_R(temperature_K: float) -> float:
    # Convert Kelvin to degrees Rankine
    if temperature_K < 0:
        raise ValueError('Invalid temperature. Must be >= 0 (K)')
    return temperature_K * 1.8
