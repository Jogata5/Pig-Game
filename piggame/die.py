#!/usr/bin/env python3
# Julian Ogata
# CPSC 386-01
# 2022-2-26
# jogata@csu.fullerton.edu
# @jogata5
#
# Lab 02-00
#
# Holds the dice class and roll methods
#

"""Die Class file"""

from pickle import NONE
import random


class Die:
    """Die class: Holds die information and roll methods"""

    def __init__(self):
        self._die_range = [1, 2, 3, 4, 5, 6]

    def roll_order(self):
        """Method: Rolls 6-sided order die"""
        return random.choice(self._die_range)

    def change_order_die(self, num=NONE):
        """Method: Removes die numbers that have been rolled"""
        if num != NONE:
            self._die_range.remove(num)


def roll():
    """Function: Rolls 6-sided die"""
    return random.randrange(1, 7)
