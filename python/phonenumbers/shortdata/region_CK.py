"""Auto-generated file, do not edit by hand. CK metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CK = PhoneMetadata(id='CK', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='9\\d{2}', possible_number_pattern='\\d{3}', possible_length=(3,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='99[689]', possible_number_pattern='\\d{3}', example_number='998', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='99[689]', possible_number_pattern='\\d{3}', example_number='998', possible_length=(3,)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
