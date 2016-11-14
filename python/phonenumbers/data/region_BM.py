"""Auto-generated file, do not edit by hand. BM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BM = PhoneMetadata(id='BM', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern='[4589]\\d{9}', possible_number_pattern='\\d{7}(?:\\d{3})?', possible_length=(10,), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='441(?:2(?:02|23|61|[3479]\\d)|[46]\\d{2}|5(?:4\\d|60|89)|824)\\d{4}', example_number='4412345678', possible_length=(10,), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='441(?:[37]\\d|5[0-39])\\d{5}', example_number='4413701234', possible_length=(10,), possible_length_local_only=(7,)),
    toll_free=PhoneNumberDesc(national_number_pattern='8(?:00|44|55|66|77|88)[2-9]\\d{6}', possible_number_pattern='\\d{10}', example_number='8002123456', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900[2-9]\\d{6}', possible_number_pattern='\\d{10}', example_number='9002123456', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(national_number_pattern='5(?:00|22|33|44|66|77|88)[2-9]\\d{6}', possible_number_pattern='\\d{10}', example_number='5002345678', possible_length=(10,)),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    national_prefix='1',
    national_prefix_for_parsing='1',
    leading_digits='441')
