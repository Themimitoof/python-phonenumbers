"""Auto-generated file, do not edit by hand. NL metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NL = PhoneMetadata(id='NL', country_code=31, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:[124-7]\\d\\d|3(?:[02-9]\\d|1[0-8])|[89]\\d{0,3})\\d{6}|1\\d{4,5}', possible_length=(5, 6, 7, 8, 9, 10)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1(?:[035]\\d|1[13-578]|6[124-8]|7[24]|8[0-467])|2(?:[0346]\\d|2[2-46-9]|5[125]|9[479])|3(?:[03568]\\d|1[3-8]|2[01]|4[1-8])|4(?:[0356]\\d|1[1-368]|7[58]|8[15-8]|9[23579])|5(?:[0358]\\d|[19][1-9]|2[1-57-9]|4[13-8]|6[126]|7[0-3578])|7\\d{2})\\d{6}', example_number='101234567', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='6[1-58]\\d{7}', example_number='612345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{4,7}', example_number='8001234', possible_length=(7, 8, 9, 10)),
    premium_rate=PhoneNumberDesc(national_number_pattern='90[069]\\d{4,7}', example_number='9061234', possible_length=(7, 8, 9, 10)),
    voip=PhoneNumberDesc(national_number_pattern='(?:85|91)\\d{7}', example_number='851234567', possible_length=(9,)),
    pager=PhoneNumberDesc(national_number_pattern='66\\d{7}', example_number='662345678', possible_length=(9,)),
    uan=PhoneNumberDesc(national_number_pattern='140(?:1(?:[035]|[16-8]\\d)|2(?:[0346]|[259]\\d)|3(?:[03568]|[124]\\d)|4(?:[0356]|[17-9]\\d)|5(?:[0358]|[124679]\\d)|7\\d|8[458])|8[478]\\d{7}', example_number='14020', possible_length=(5, 6, 9)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='140(?:1(?:[035]|[16-8]\\d)|2(?:[0346]|[259]\\d)|3(?:[03568]|[124]\\d)|4(?:[0356]|[17-9]\\d)|5(?:[0358]|[124679]\\d)|7\\d|8[458])', possible_length=(5, 6)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([1-57-9]\\d)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['1[035]|2[0346]|3[03568]|4[0356]|5[0358]|7|8[4578]|91'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([1-5]\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1[16-8]|2[259]|3[124]|4[17-9]|5[124679]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(6)(\\d{8})', format='\\1 \\2', leading_digits_pattern=['6[0-57-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(66)(\\d{7})', format='\\1 \\2', leading_digits_pattern=['66'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(14)(\\d{3,4})', format='\\1 \\2', leading_digits_pattern=['14'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='([89]0\\d)(\\d{4,7})', format='\\1 \\2', leading_digits_pattern=['[89]0'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
