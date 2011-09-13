"""Auto-generated file, do not edit by hand. CL metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CL = PhoneMetadata(id='CL', country_code=56, international_prefix='(?:0|1(?:1[0-69]|2[0-57]|5[13-58]|69|7[0167]|8[018]))0',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:[2-9]|600|123)\\d{7,8}', possible_number_pattern='\\d{6,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2|32|41)\\d{7}|(?:3[3-5]|4[235]|5[1-3578]|6[13-57]|7[1-35])\\d{6,7}', possible_number_pattern='\\d{6,9}', example_number='21234567'),
    mobile=PhoneNumberDesc(national_number_pattern='9[6-9]\\d{7}', possible_number_pattern='\\d{8,9}', example_number='961234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}|1230\\d{7}', possible_number_pattern='\\d{9,11}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='600\\d{7,8}', possible_number_pattern='\\d{10,11}', example_number='6001234567'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='44\\d{7}', possible_number_pattern='\\d{9}', example_number='441234567'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='600\\d{7,8}', possible_number_pattern='\\d{10,11}', example_number='6001234567'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0|(1(?:1[0-69]|2[0-57]|5[13-58]|69|7[0167]|8[018]))',
    number_format=[NumberFormat(pattern='(2)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['2'], national_prefix_formatting_rule=u'(\\1)', domestic_carrier_code_formatting_rule=u'$CC (\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{2,3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[357]|4[1-35]|6[13-57]'], national_prefix_formatting_rule=u'(\\1)', domestic_carrier_code_formatting_rule=u'$CC (\\1)'),
        NumberFormat(pattern='(9)([6-9]\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['9'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(44)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['44'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([68]00)(\\d{3})(\\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['60|8'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(600)(\\d{3})(\\d{2})(\\d{3})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['60'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(1230)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule=u'\\1')])
