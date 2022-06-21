from .base import BaseEnum

from enum import unique

@unique
class AreaUnit(BaseEnum):
    SQ_FT = 'ft^2'
    SQ_M = 'm^2'
    SQ_KM = 'km^2'
    SQ_MI = 'mi^2'
    SQ_IN = 'in^2'
    SQ_CM = 'cm^2'
    SQ_MM = 'mm^2'
    ACRE = 'acre'
    HECTARE = 'ha'
    ACRE_FT = 'acre-ft'