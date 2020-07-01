import math
import random
import re
import sys

def factorial(n):
    if (n>1):
        
        return n*factorial(n-1)    
        
    elif(n==1):
        return n
        


if __name__ == '__main__':
        n = int(input())
        print('n is ',n)
        result = factorial(n)
        print('factorial of ',n,'is ',result)
