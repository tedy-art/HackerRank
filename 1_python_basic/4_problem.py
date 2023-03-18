"""
https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
"""
def is_leap(year):
    leap = False

    # write your logic here
    if year % 400 == 0:
        leap = True

    elif year % 100 == 0:
        leap = False

    elif year % 4 == 0:
        leap = True

    return leap

year = int(input("Enter year : "))
print(is_leap(year))