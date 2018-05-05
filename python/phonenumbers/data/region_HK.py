"""Auto-generated file, do not edit by hand. HK metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HK = PhoneMetadata(id='HK', country_code=852, international_prefix='00(?:[126-9]|30|5[09])?',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-7]\\d{7}|8[0-4]\\d{6,7}|9\\d{4,10}', possible_length=(5, 6, 7, 8, 9, 11)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:[13-8]\\d|2[013-9]|9[0-24-9])\\d|3(?:[1569][0-24-9]\\d|4[0-246-9]\\d|7[0-24-69]\\d|8(?:4[04]|9\\d))|58(?:0[1-8]|1[2-9]))\\d{4}', example_number='21234567', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:46(?:0[0-6]|4[0-57-9])|5(?:[1-59][0-46-9]\\d|6[0-4689]\\d|7(?:[0-2469]\\d|30))|6(?:0[1-9]\\d|[145]\\d{2}|2(?:[0-357-9]\\d|6[01])|[36][0-57-9]\\d|7[0-79]\\d|8[0-2457-9]\\d|9[0-579]\\d)|707[1-5]|8480|9(?:0[1-46-9]\\d|1[02-9]\\d|2(?:[0-8]\\d|9[03-9])|[358][0-8]\\d|[467]\\d{2}))\\d{4}', example_number='51234567', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', example_number='800123456', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900(?:[0-24-9]\\d{7}|3\\d{1,4})', example_number='90012345678', possible_length=(5, 6, 7, 8, 11)),
    personal_number=PhoneNumberDesc(national_number_pattern='8(?:1[0-4679]\\d|2(?:[0-36]\\d|7[0-4])|3(?:[034]\\d|2[09]|70))\\d{4}', example_number='81123456', possible_length=(8,)),
    pager=PhoneNumberDesc(national_number_pattern='7(?:1(?:0[0-38]|1[0-3679]|3[013]|69|9[136])|2(?:[02389]\\d|1[18]|7[27-9])|3(?:[0-38]\\d|7[0-369]|9[2357-9])|47\\d|5(?:[178]\\d|5[0-5])|6(?:0[0-7]|2[236-9]|[35]\\d)|7(?:[27]\\d|8[7-9])|8(?:[23689]\\d|7[1-9])|9(?:[025]\\d|6[0-246-8]|7[0-36-9]|8[238]))\\d{4}', example_number='71123456', possible_length=(8,)),
    uan=PhoneNumberDesc(national_number_pattern='30(?:0[1-9]|[15-7]\\d|2[047]|89)\\d{4}', example_number='30161234', possible_length=(8,)),
    preferred_international_prefix='00',
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[2-7]|[89](?:0[1-9]|[1-9])']),
        NumberFormat(pattern='(800)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['800']),
        NumberFormat(pattern='(900)(\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['900']),
        NumberFormat(pattern='(900)(\\d{2,5})', format='\\1 \\2', leading_digits_pattern=['900'])],
    mobile_number_portable_region=True)
