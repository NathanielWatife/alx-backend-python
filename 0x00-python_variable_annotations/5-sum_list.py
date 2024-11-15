#!/usr/bin/env python3
"""typed annotation of function sum_list"""

from typing import List, Union

def sum_list(input_list: List[float]) -> float:
    """Return the sum of all numbers in the list"""
    return sum(input_list)