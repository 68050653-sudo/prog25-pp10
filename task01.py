"""
PROG 2025/1
Pair Programming Assignment #10
Task #1
"""

# Do not remove this line!
from poomdt import is_leap_year

# Test 1 - Test whether is_leap_year can handle 0 correctly
def test_year_is_zero():
    if is_leap_year(0) == True:
        return True
    else:
        return False

# Test 2 - Test normal leap year (divisible by 4 but not by 100)
# Reason to fail: is_leap_year fails to detect normal leap year
def test_2():
    year = 2024
    if is_leap_year(year) == True:
        return True
    else:
        return False

# Test 3 - Test century non-leap year (divisible by 100 but not by 400)
# Reason to fail: is_leap_year fails to exclude century non-leap year
def test_3():
    year = 1900
    if is_leap_year(year) == False:
        return True
    else:
        return False

# Test 4 - Test century leap year (divisible by 400)
# Reason to fail: is_leap_year fails to include 400-year leap year
def test_4():
    year = 2000
    if is_leap_year(year) == True:
        return True
    else:
        return False

# Test 5 - Test non-leap year (not divisible by 4)
# Reason to fail: is_leap_year incorrectly marks normal year as leap
def test_5():
    year = 2023
    if is_leap_year(year) == False:
        return True
    else:
        return False
