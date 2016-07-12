#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
except IOError:
    print("can not open file")
else:
    f.close

