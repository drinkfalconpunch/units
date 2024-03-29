from enum import Enum, auto

from attrs import define, field, validators

class LengthUnit(Enum):
    MILE = auto()
    FOOT = auto()
    INCH = auto()
    YARD = auto()
    KM = auto()
    M = auto()
    NM = auto()
    MICRON = auto()
    MM = auto()
    CM = auto()

# Give the engine some unit systems, like mks or fps, and a way to convert one to the other,
# like feet to meter. Memoize values for future use.

unit_mile = {
    'enum': LengthUnit.MILE,
    'string': ['mi', 'mile', 'miles'],
    'conversions': {
        LengthUnit.YARD: 1760,
        LengthUnit.FOOT: 5280,
        LengthUnit.INCH: 63360,
        LengthUnit.KM: 1.609344,
        LengthUnit.M: 1609.344,
        LengthUnit.CM: 160934.4,
        LengthUnit.MM: 1609344,
        LengthUnit.MICRON: 1609344000,
        LengthUnit.NM: 1609344000000,
    }
}

unit_foot = {
    'enum': LengthUnit.FOOT,
    'string': ['ft', 'foot', 'feet'],
    'conversions': {
        LengthUnit.MILE: 1,
        LengthUnit.YARD: 1760,
        LengthUnit.FOOT: 5280,
        LengthUnit.INCH: 63360,
        LengthUnit.KM: 1.609344,
        LengthUnit.M: 1609.344,
        LengthUnit.CM: 160934.4,
        LengthUnit.MM: 1609344,
        LengthUnit.MICRON: 1609344000,
        LengthUnit.NM: 1609344000000,
    }
}

@define
class Length:
    value: float = field()
    unit: LengthUnit = field(validator=validators.instance_of(LengthUnit))

    @property
    def unit_string(self):
        return self.unit # FIX

    def convert_unit(self, from_unit: LengthUnit):
        pass


# in, ft, yd, mi
conversion_table = [[1,     0.08333333, 0.02777778, 0.00001578],
                    [12,    1,          0.3333333,  0.00018939],
                    [36,    3,          1,          0.00056818],
                    [63360, 5280,       1760,       1]]

# mm, cm, m, km, in, ft, yd, mi
conversion_table_field_units = [
    [1, 	0.1, 	0.001, 	0.000001, 	0.039370078740157, 	0.0032808398950131, 	0.0010936132983377, 	0.00000062137119223733],
    [10, 	1, 	0.01, 	0.00001, 	0.39370078740157, 	0.032808398950131, 	0.010936132983377, 	0.0000062137119223733],
    [1000, 	100, 	1, 	0.001, 	39.370078740157, 	3.2808398950131, 	1.0936132983377, 	0.00062137119223733],
    [1000000, 	100000, 	1000, 	1, 	39370.078740157, 	3280.8398950131, 	1093.6132983377, 	0.62137119223733],
    [25.4, 	2.54, 	0.0254, 	0.0000254, 	1, 	0.083333333333333, 	0.027777777777778, 	0.000015782828282828],
    [304.8, 	30.48, 	0.3048, 	0.0003048, 	12, 	1, 	0.33333333333333, 	0.00018939393939394],
    [914.4, 	91.44, 	0.9144, 	0.0009144, 	36, 	3, 	1, 	0.00056818181818182],
    [1609344, 	160934.4, 	1609.344, 	1.609344, 	63360, 	5280, 	1760, 	1]
]

def feet_to_yards(feet: float) -> float:
    return feet / 3

def yards_to_feet(yards: float) -> float:
    return yards * 3

def feet_to_inches(feet: float) -> float:
    return feet * 12

def inches_to_feet(inches: float) -> float:
    return inches / 12

def feet_to_meters(feet: float) -> float:
    return feet * 0.3048

def meters_to_feet(meters: float) -> float:
    return meters / 0.3048

def feet_to_miles(feet: float) -> float:
    return feet / 5280

def miles_to_feet(miles: float) -> float:
    return miles * 5280

# def feet_to
