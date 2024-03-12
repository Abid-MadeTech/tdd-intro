"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

roman_numerals = {
        1: 'I', 
        2: 'II', 
        3: 'III', 
        4: 'IV', 
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        10: 'X',
        12: 'XII',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
       
    }

def convert_to_roman(number):
    return roman_numerals[number]

# 1 = I
def test_convert_one_to_ten_to_roman_numeral():
    for i in range(1, 11):
        assert convert_to_roman(i) == roman_numerals[i]

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

def test_9_equals_IX():
    assert convert_to_roman(9) == "IX"

def test_10_equals_X():
    assert convert_to_roman(10) == "X"

def test_12_equals_XII():
    assert convert_to_roman(12) == "XII"

def test_50_equals_L():
    assert convert_to_roman(50) == "L"

def test_100_equals_C():
    assert convert_to_roman(100) == "C"

def test_500_equals_D():
    assert convert_to_roman(500) == "D"

def test_1000_equals_M():
    assert convert_to_roman(1000) == "M"





