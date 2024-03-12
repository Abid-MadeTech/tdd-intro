roman_numerals = {
        1: 'I', 
        2: 'II', 
        3: 'III', 
        4: 'IV', 
        5: 'V',
        6: 'VI',
        10: ''
        12: 'XII'
    }

def convert_to_roman(number):
    return roman_numerals[number]

# 1 = I
def test_one_equals_I():
    assert convert_to_roman(1) == "I"

def test_two_equals_II():
    assert convert_to_roman(2) == "II"
    
def test_3_equals_III():
    assert convert_to_roman(3) == "III"

def test_4_equals_IV():
    assert convert_to_roman(4) == "IV"

def test_5_equals_V():
    assert convert_to_roman(5) == "V"

def test_6_equals_VI():
    assert convert_to_roman(6) == "VI"

def test_10_equals_X():
    assert convert_to_roman(10) == "X"

def test_12_equals_XII():
    assert convert_to_roman(12) == "XII"





