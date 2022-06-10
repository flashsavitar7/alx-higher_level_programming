#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    front = 0
    back = 0
    ans = 0
    length = len(roman_string)
    
    if roman_string == None:
        return 0
    else:
        for i in range(length):
            front = d[roman_string[i]]
            if front > back:
                ans = ans + front - 2 * back
            else:
                ans += front
            back = front
    return int(ans)


