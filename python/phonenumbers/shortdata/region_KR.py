"""Auto-generated file, do not edit by hand. KR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KR = PhoneMetadata(id='KR', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2,4}', possible_length=(3, 4, 5)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:1[78]|28|330|82)', example_number='118', possible_length=(3, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='11[29]', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:[01]|114)|1(?:[0247-9]|114)|2[01389]|3(?:2|3[039]|45|66|88|9[18])|[679]114|8(?:114|2))', example_number='112', possible_length=(3, 4, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1(?:0(?:[01]|114)|1(?:114|4)|[6-9]114)', example_number='100', possible_length=(3, 5)),
    short_data=True)
