"""Auto-generated file, do not edit by hand. FR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FR = PhoneMetadata(id='FR', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[1-8]\\d{1,5}', possible_length=(2, 3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:0(?:07|13)|1(?:[0459]|[68]\\d{3})|9[167])|224|3(?:[01]\\d{2}|3700)|740', example_number='3010', possible_length=(3, 4, 5, 6)),
    premium_rate=PhoneNumberDesc(national_number_pattern='36665|[4-8]\\d{4}', example_number='42000', possible_length=(5,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:[578]|12)', example_number='112', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0\\d{2}|1(?:[02459]|6(?:000|111)|8\\d{3})|9[167]|[578])|2(?:0(?:000|20)|24)|3\\d{3,4}|6(?:1[14]|34|\\d{4})|7(?:0[06]|22|40|\\d{4})|[458]\\d{4}', example_number='1010', possible_length=(2, 3, 4, 5, 6)),
    standard_rate=PhoneNumberDesc(national_number_pattern='10(?:14|2[23]|34|6[14]|99)|2020|3(?:646|9[07]0)|6(?:1[14]|34)|70[06]', example_number='1023', possible_length=(3, 4)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='118777|2(?:0(?:000|20)|24)|6(?:1[14]|34)|7\\d{2}', example_number='118777', possible_length=(3, 4, 5, 6)),
    sms_services=PhoneNumberDesc(national_number_pattern='(?:114|[3-8]\\d{4})', example_number='33700', possible_length=(3, 5)),
    short_data=True)
