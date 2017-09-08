"""Auto-generated file, do not edit by hand. FI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FI = PhoneMetadata(id='FI', country_code=358, international_prefix='00|99(?:[02469]|5(?:11|33|5[59]|88|9[09]))',
    general_desc=PhoneNumberDesc(national_number_pattern='[16]\\d{6,9}|2\\d{4,9}|[35]\\d{5,9}|4\\d{7,10}|7\\d{7,9}|[89]\\d{6,8}', possible_length=(5, 6, 7, 8, 9, 10, 11)),
    fixed_line=PhoneNumberDesc(national_number_pattern='1[3-79][1-8]\\d{4,6}|[235689][1-8]\\d{5,7}', example_number='131234567', possible_length=(7, 8, 9)),
    mobile=PhoneNumberDesc(national_number_pattern='4(?:[0-8]\\d{6,8}|9\\d{9})|50\\d{4,8}', example_number='412345678', possible_length=(6, 7, 8, 9, 10, 11)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{5,6}', example_number='800123456', possible_length=(8, 9)),
    premium_rate=PhoneNumberDesc(national_number_pattern='[67]00\\d{5,6}', example_number='600123456', possible_length=(8, 9)),
    uan=PhoneNumberDesc(national_number_pattern='10(?:0\\d{4,6}|[1-46-9]\\d{5,7}|5\\d{4,7})|2(?:0(?:0\\d{4,6}|[1346-8]\\d{5,7}|2(?:[023]\\d{4,5}|[14-9]\\d{4,6})|5(?:\\d{3}|\\d{5,7})|9(?:[0-7]\\d{4,6}|[89]\\d{1,6}))|9\\d{5,8})|3(?:0(?:0\\d{3,7}|[1-57-9]\\d{5,7}|6(?:\\d{3}|\\d{5,7}))|44\\d{3}|93\\d{5,7})|60(?:[12]\\d{5,6}|6\\d{7})|7(?:1\\d{7}|3\\d{8}|5[03-9]\\d{5,6})', example_number='10112345', possible_length=(5, 6, 7, 8, 9, 10)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='100\\d{4,6}|20(?:0\\d{4,6}|2[023]\\d{4,5}|9[89]\\d{1,6})|300\\d{3,7}|60(?:[12]\\d{5,6}|6\\d{7})|7(?:1\\d{7}|3\\d{8}|5[03-9]\\d{5,6})', example_number='1001234', possible_length=(5, 6, 7, 8, 9, 10)),
    preferred_international_prefix='00',
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{3,7})', format='\\1 \\2', leading_digits_pattern=['(?:[1-3]0|[6-8])0'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(116\\d{3})', format='\\1', leading_digits_pattern=['116'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3,9})', format='\\1 \\2', leading_digits_pattern=['1(?:0[1-9]|[3-9])|2(?:0[1-9]|9)|30[1-9]|4|50|7(?:[13]|5[03-9])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(75\\d{3})', format='\\1', leading_digits_pattern=['75[12]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d)(\\d{5,9})', format='\\1 \\2', leading_digits_pattern=['[235689][1-8]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(39\\d)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['39'], national_prefix_formatting_rule='0\\1')],
    intl_number_format=[NumberFormat(pattern='(\\d{3})(\\d{3,7})', format='\\1 \\2', leading_digits_pattern=['(?:[1-3]0|[6-8])0']),
        NumberFormat(pattern='(116\\d{3})', format='\\1', leading_digits_pattern=['116']),
        NumberFormat(pattern='(\\d{2})(\\d{3,9})', format='\\1 \\2', leading_digits_pattern=['1(?:0[1-9]|[3-9])|2(?:0[1-9]|9)|30[1-9]|4|50|7(?:[13]|5[03-9])']),
        NumberFormat(pattern='(\\d)(\\d{5,9})', format='\\1 \\2', leading_digits_pattern=['[235689][1-8]']),
        NumberFormat(pattern='(39\\d)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['39'])],
    main_country_for_code=True,
    mobile_number_portable_region=True)
