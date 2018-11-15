"""Auto-generated file, do not edit by hand. IL metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IL = PhoneMetadata(id='IL', country_code=972, international_prefix='0(?:0|1[2-9])',
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{6}(?:\\d{3,5})?|[57]\\d{8}|[1-489]\\d{7}', possible_length=(7, 8, 9, 10, 11, 12), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:153\\d\\d?|[2-489])\\d{7}', example_number='21234567', possible_length=(8, 11, 12), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='5(?:(?:[0-489][2-9]|6\\d)\\d|5(?:01|2[2-5]|3[23]|4[45]|5[05689]|6[6-8]|7[0-267]|8[7-9]|9[1-9]))\\d{5}', example_number='502345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:255|80[019]\\d{3})\\d{3}', example_number='1800123456', possible_length=(7, 10)),
    premium_rate=PhoneNumberDesc(national_number_pattern='1(?:2(?:00\\d\\d|12)|9(?:0[01]|19)\\d\\d)\\d{4}', example_number='1919123456', possible_length=(8, 10)),
    shared_cost=PhoneNumberDesc(national_number_pattern='1700\\d{6}', example_number='1700123456', possible_length=(10,)),
    voip=PhoneNumberDesc(national_number_pattern='7(?:(?:18|2[23]|3[237]|47|6[58]|7\\d|9[2357-9])\\d|8(?:2\\d|33|55|77|81))\\d{5}', example_number='771234567', possible_length=(9,)),
    uan=PhoneNumberDesc(national_number_pattern='1599\\d{6}', example_number='1599123456', possible_length=(10,)),
    voicemail=PhoneNumberDesc(national_number_pattern='151\\d{8,9}', example_number='15112340000', possible_length=(11, 12)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='1700\\d{6}', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{3})', format='\\1-\\2', leading_digits_pattern=['125']),
        NumberFormat(pattern='(\\d)(\\d{3})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['[2-489]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{2})(\\d{2})', format='\\1-\\2-\\3', leading_digits_pattern=['121']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['[57]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format='\\1-\\2-\\3', leading_digits_pattern=['12']),
        NumberFormat(pattern='(\\d{4})(\\d{6})', format='\\1-\\2', leading_digits_pattern=['159']),
        NumberFormat(pattern='(\\d)(\\d{3})(\\d{3})(\\d{3})', format='\\1-\\2-\\3-\\4', leading_digits_pattern=['1[7-9]']),
        NumberFormat(pattern='(\\d{3})(\\d{1,2})(\\d{3})(\\d{4})', format='\\1-\\2 \\3-\\4', leading_digits_pattern=['1'])],
    mobile_number_portable_region=True)
