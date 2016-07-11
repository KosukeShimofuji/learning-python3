#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib2(n):
        """Retrun a list containg the Fibonacci series up to n """
        result = []
        a, b = 0, 1 
        while a < n:
            result.append(a)
            a,b = b, a+b
        return result

print (fib2(100))

