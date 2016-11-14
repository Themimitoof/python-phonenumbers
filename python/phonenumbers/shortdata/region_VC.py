"""Auto-generated file, do not edit by hand. VC metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VC = PhoneMetadata(id='VC', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='9\\d{2}', possible_number_pattern='\\d{3}', possible_length=(3,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='9(?:11|99)', possible_number_pattern='\\d{3}', example_number='911', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='9(?:11|99)', possible_number_pattern='\\d{3}', example_number='911', possible_length=(3,)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
