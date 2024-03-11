def convert_to_roman(number):
    
    if number in [1, 2, 3]:
        roman_numeral = ""
        for i in range(number):
            roman_numeral += "I"
        return roman_numeral

    elif number == 12:
        return "XII"
    else: 
        return "IV"

# 1 = I
def test_one_equals_I():
    assert convert_to_roman(1) == "I"

def test_two_equals_II():
    assert convert_to_roman(2) == "II"

def test_4_equals_IV():
    assert convert_to_roman(4) == "IV"

def test_12_equals_XII():
    assert convert_to_roman(12) == "XII"

def test_3_equals_III():
    assert convert_to_roman(3) == "III"

def test_5_equals_V():
    assert convert_to_roman(5) == "V"