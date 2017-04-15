"""Auto-generated file, do not edit by hand. FI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FI = PhoneMetadata(id='FI', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2,5}', possible_length=(3, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='116111', example_number='116111', possible_length=(6,)),
    emergency=PhoneNumberDesc(national_number_pattern='112', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11(?:2|6111)', example_number='112', possible_length=(3, 6)),
    short_data=True)
