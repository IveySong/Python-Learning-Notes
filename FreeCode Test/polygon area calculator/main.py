# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 23:02:01 2023

@author: Aixia
"""

import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)


# Run unit tests automatically
main(module='test_module', exit=False)