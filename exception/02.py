#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

try:
    raise NameError('Hello Error')
except NameError as err:
    print(err) 

