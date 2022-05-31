#!/usr/bin/python3
for i in range(0,100,+1):
    if i % 15 == 0:
        print("FizzBuzz ", end= "")
    elif i % 3 == 0:
        print("Fizz ", end = "")
    elif i % 5 == 0:
        print("Buzz ", end = "")
    else:
        print(f"{i:d} ", end = "")