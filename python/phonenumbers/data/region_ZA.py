"""Auto-generated file, do not edit by hand. ZA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZA = PhoneMetadata(id='ZA', country_code=27, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-79]\\d{8}|8(?:[05-7]\\d{7}|[1-4]\\d{3,7})', possible_number_pattern='\\d{5,9}', possible_length=(5, 6, 7, 8, 9)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1[0-8]|2[0-378]|3[1-69]|4\\d|5[1346-8])\\d{7}', possible_number_pattern='\\d{9}', example_number='101234567', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:6[0-5]|7[0-46-9])\\d{7}|8(?:[1-4]\\d{1,5}|5\\d{5})\\d{2}', example_number='711234567', possible_length=(5, 6, 7, 8, 9)),
    toll_free=PhoneNumberDesc(national_number_pattern='80\\d{7}', possible_number_pattern='\\d{9}', example_number='801234567', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='86[2-9]\\d{6}|90\\d{7}', possible_number_pattern='\\d{9}', example_number='862345678', possible_length=(9,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='860\\d{6}', possible_number_pattern='\\d{9}', example_number='860123456', possible_length=(9,)),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(national_number_pattern='87\\d{7}', possible_number_pattern='\\d{9}', example_number='871234567', possible_length=(9,)),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(national_number_pattern='861\\d{6}', possible_number_pattern='\\d{9}', example_number='861123456', possible_length=(9,)),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(860)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['860'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[1-79]|8(?:[0-57]|6[1-9])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3,4})', format='\\1 \\2', leading_digits_pattern=['8[1-4]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2,3})', format='\\1 \\2 \\3', leading_digits_pattern=['8[1-4]'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
