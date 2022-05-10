#!/usr/bin/env python3
# Julian Ogata
# CPSC 386-01
# 2022-2-26
# jogata@csu.fullerton.edu
# @jogata5
#
# Lab 02-00
#
# Header file that holds the players' infomation and player methods
#

"""Player Class File"""

import time
from .die import roll


class PigPlayer:
    """PigPlayer class: Holds player information and dice roll methods"""

    def __init__(self, name, score=0, order=0):
        self._name = name
        self._score = score
        self._order = order
        self._player_type = "Human"

    # Getter Methods
    def get_name(self):
        """Method: Gets private value of the player's name"""
        return self._name

    def get_score(self):
        """Method: Gets private value of the player's score"""
        return self._score

    def get_order(self):
        """Method: Gets private value of the player's turn order"""
        return self._order

    def get_player_type(self):
        """Method: Gets private value of the player's type"""
        return self._player_type

    # Setter Methods
    def set_name(self, name):
        """Method: Sets a value to the player's name"""
        self._name = name

    def set_score(self, score):
        """Method: Sets a value to the player's score"""
        self._score = score

    def set_order(self, order):
        """Method: Sets a value to the player's turn order"""
        self._order = order

    # Properties
    player_name = property(get_name, set_name)
    player_score = property(get_score, set_score)
    player_order = property(get_order, set_order)

    def __str__(self):
        return self._name

    def __repr__(self):
        return 'Player("{}")'.format(self._name)

    def __int__(self):
        return self._score, self._order

    def does_roll(self):
        """Method: Calls player to press ENTER to begin rolling die"""
        input(
            "{} is rolling. ".format(self.get_name())
            + "Press ENTER to roll die..."
        )
        time.sleep(1)
        return roll()

    def roll_again(self):
        """Method: Asks player for a "yes" input to roll again"""
        resp = input(
            "{}, do you want to roll again? ".format(self.get_name())
            + 'Type "yes" to roll! '
        )
        return resp.lower() == "yes"


class Computer(PigPlayer):
    """Computer class:
    Holds the Computer AI's information and dice roll methods"""

    def __init__(self):
        super().__init__("Computer")
        self._name = "CPU Tom"
        self._player_type = "CPU"

    def cpu_does_roll(self):
        """Method: Had the AI roll die"""
        print("\n{} is rolling...".format(self.get_name()))
        time.sleep(1)
        return roll()

    def cpu_roll_again(self, players, temp_score, times_rolled):
        """Method: Calls choices method to roll die again"""
        print("{} is thinking...".format(self.get_name()))
        time.sleep(2)
        return self.choices(players, temp_score, times_rolled) == "yes"

    def choices(self, players, temp_score, times_rolled):
        """Method: Chooses whether for the AI to roll or not"""
        tom_score = players[0].player_score
        other_score = players[1].player_score
        dif = (
            (temp_score + tom_score) % (other_score + times_rolled) * temp_score
        )
        if other_score >= 21:
            print("{} choose to roll again".format(self.get_name()))
            return "yes"
        if dif < 5 or tom_score > 26:
            print("{} choose to roll again".format(self.get_name()))
            return "yes"
        if 10 >= tom_score < 20 and (times_rolled < 3):
            print("{} choose to roll again".format(self.get_name()))
            return "yes"
        if tom_score < 10 and temp_score > 8:
            print("{} choose not to roll again".format(self.get_name()))
            return "no"
        if dif > 20 or temp_score > 12:
            print("{} choose not to roll again".format(self.get_name()))
            return "no"
        print("{} choose not to roll".format(self.get_name()))
        return "no"
