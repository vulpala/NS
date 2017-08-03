__author__ = 'Harishiva'
import math
import sys
import decimal

class Expo: # constructor class
    def __init__(self, m, d, n):
        self.num = m
        self.exp = d
        self.power = n

    def large_integer_exponent(self, m, d, n):

        # perfoming m^d mod n and returning the result

        result = m**d % n

        return result

    def exponent(self, m, d, n):
        print(self.large_integer_exponent(m, d, n))




