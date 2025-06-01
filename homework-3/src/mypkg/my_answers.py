#!/usr/bin/python

"""
Python Statements
"""


def add_binary(a, b):
    """
    This is to review binary operations
    ============================================================
    Given two binary strings, return their sum (also a binary string).
    Return None if one of the input strings are empty or contains characters different than 1 or 0.
    Example 1:
                Input: a = "11", b = "1"
                Output: result = "100"
    Example 2:
                Input: a = "1010", b = "1011"
                Output: result = "10101"
    """
a_len = len(a)
b_len = len(b)
a_sum = 0
b_sum = 0
if(a == ''):
    return None
if(b == ''):
     return None
for i in range(a_len):
    if (a[i] == '1' or a[i] == '0'):
        a_sum += int(a[i])*(2**(a_len-i-1))
    else:
         return None
         break
for i in range(b_len):
    if (b[i] == '0' or b[i] == '1'):
        b_sum += int(b[i])*(2**(b_len-i-1))
     else:
          return None
          break
    m = bin(a_sum + b_sum)
    result = str(m)[2:]
return result
print(add_binary('1 1', '0 0001'))
    
  

def plus_one(digits):
    """
    This is to review loops and if statements
    ============================================================
    Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
    You can do this in-place!
    The digits are stored such that the most significant digit is at the head of the list, and each
    element in the array contain a single digit.
    You may assume the integer does not contain any leading zero, except the number 0 itself.
    Example 1:
            Input: digits = [1, 2, 3]
            Output: digits = [1, 2, 4]
            Explanation: The array represents the integer 123.
    Example 2:
            Input: digits = [1, 0, 9, 9]
            Output: digits = [1, 1, 0, 0]
    """
    n = len(digits)

   
    #Add one to last digit
    digits[n-1] += 1
    carry = digits[n-1] / 10
    digits[n-1] = digits[n-1] % 10
   
    for i in range(n-2,-1,-1):
        if (carry == 1):
           digits[i] += 1
           carry = digits[i]/10
           digits[i] = digits[i] % 10
          
    if (carry == 1):
      digits.insert(0, 1)
  
digits=[1, 0,9,9]
  
plus_one(digits)
for i in range(0, len(digits)):
     
     print(digits[i] ,end= " ")
     

    return digits



def roman_to_integers(roman_string):
    
    """
    This is to review loops, if statements and dictionaries
    ============================================================
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, two is written as II in Roman numeral, just two one's added together.
    Twelve is written as, XII, which is simply X + II. The number twenty seven is written
    as XXVII, which is XX + V + II.
    Roman numerals are usually written largest to smallest from left to right. However,
    the numeral for four is not IIII. Instead, the number four is written as IV. Because
    the one is before the five we subtract it making four. The same principle applies to
    the number nine, which is written as IX. There are six instances where subtraction is used:
    - I can be placed before V (5) and X (10) to make 4 and 9.
    - X can be placed before L (50) and C (100) to make 40 and 90.
    - C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
    Example 1:
        Input: "III"
        Output: 3
    Example 2:
        Input: "IV"
        Output: 4
    Example 3:
        Input: "IX"
        Output: 9
    Example 4:
        Input: "LVIII"
        Output: 58
        Explanation: C = 100, L = 50, XXX = 30 and III = 3.
    Example 5:
        Input: "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    
    Roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

p = 0
res = 0
n = len(roman_string)
        
for i in range(n-1, -1, -1):

            if Roman_number[roman_string[i]] >= p:
             res += Roman_number[roman_string[i]]
            else:
                res -= Roman_number[roman_string[i]]
            p = Roman_number[roman_string[i]]
print (res)
roman_to_integers
print(roman_to_integers('MCMIV'))

    return integer


#Second way

def roman_to_integers(roman_string):
        Roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        for i in range(len(roman_string)):
            if i > 0 and Roman_number[roman_string[i]] > Roman_number[roman_string[i - 1]]:
                integer += Roman_number[roman_string[i]] - 2 * Roman_number[roman_string[i - 1]]
            else:
                integer += Roman_number[roman_string[i]]
                            
        return integer

print(roman_to_integers('III'))
print(roman_to_integers('IV'))
print(roman_to_integers('IX'))
print(roman_to_integers('LVIII'))
print(roman_to_integers('MCMXCIV'))
