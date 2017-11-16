"""Auto-generated file, do not edit by hand. AU metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AU = PhoneMetadata(id='AU', country_code=61, international_prefix='(?:14(?:1[14]|34|4[17]|[56]6|7[47]|88)0011)|001[14-689]',
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{4,9}|[2-578]\\d{8}', possible_length=(5, 6, 7, 8, 9, 10), possible_length_local_only=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[237]\\d{8}|8(?:51(?:0(?:0[03-9]|[1247]\\d|3[2-9]|5[0-8]|6[1-9]|8[0-6])|1(?:1[69]|[23]\\d|4[0-4]))|[6-8]\\d{4}|9(?:[02-9]\\d{3}|1(?:[0-57-9]\\d{2}|6[0135-9]\\d)))\\d{3}', example_number='212345678', possible_length=(9,), possible_length_local_only=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='14(?:5\\d|71)\\d{5}|4(?:[0-3]\\d|4[047-9]|5[0-25-9]|6[6-9]|7[02-9]|8[12457-9]|9[017-9])\\d{6}', example_number='412345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='180(?:0\\d{3}|2)\\d{3}', example_number='1800123456', possible_length=(7, 10)),
    premium_rate=PhoneNumberDesc(national_number_pattern='19(?:0[0126]\\d|[679])\\d{5}', example_number='1900123456', possible_length=(8, 10)),
    shared_cost=PhoneNumberDesc(national_number_pattern='13(?:00\\d{3}|45[0-4]|\\d)\\d{3}', example_number='1300123456', possible_length=(6, 8, 10)),
    personal_number=PhoneNumberDesc(national_number_pattern='500\\d{6}', example_number='500123456', possible_length=(9,)),
    voip=PhoneNumberDesc(national_number_pattern='550\\d{6}', example_number='550123456', possible_length=(9,)),
    pager=PhoneNumberDesc(national_number_pattern='16\\d{3,7}', example_number='1612345', possible_length=(5, 6, 7, 8, 9)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='1(?:3(?:00\\d{3}|45[0-4]|\\d)\\d{3}|80(?:0\\d{6}|2\\d{3}))', example_number='1300123456', possible_length=(6, 7, 8, 10)),
    preferred_international_prefix='0011',
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([2378])(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[2378]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['14|[45]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(16)(\\d{3,4})', format='\\1 \\2', leading_digits_pattern=['16'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(16)(\\d{3})(\\d{2,4})', format='\\1 \\2 \\3', leading_digits_pattern=['16'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(1[389]\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1[389]0', '1(?:[38]0|9)0']),
        NumberFormat(pattern='(180)(2\\d{3})', format='\\1 \\2', leading_digits_pattern=['180', '1802']),
        NumberFormat(pattern='(19\\d)(\\d{3})', format='\\1 \\2', leading_digits_pattern=['19[13]']),
        NumberFormat(pattern='(19\\d{2})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['19[679]']),
        NumberFormat(pattern='(13)(\\d{2})(\\d{2})', format='\\1 \\2 \\3', leading_digits_pattern=['13[1-9]'])],
    main_country_for_code=True,
    mobile_number_portable_region=True)
