#!/usr/bin/env python3
# Julian Ogata
# CPSC 386-01
# 2022-2-26
# jogata@csu.fullerton.edu
# @jogata5
#
# Lab 02-00
#
# Game file that holds core elements: game rules, turns, scores, etc.
#

"""Game Class file"""

import time
from .die import Die as d
from .player import PigPlayer as p, Computer as c


class PigGame:
    """Piggame class: Holds pig game information and game rules/methods"""

    def __init__(self):
        self._turn = 1
        self._game = True
        self._player_num = 0

    def reset(self):
        """Method: Resets game"""
        self._turn = 1
        self._game = True
        self._player_num = 0

    def get_turn(self):
        """Method: returns game turn"""
        return self._turn

    def get_game(self):
        """Method: Returns game state"""
        return self._game

    def get_players(self):
        """Method: Returns number of players in the game"""
        return self._player_num

    def set_players(self, num):
        """Method: Sets number of players in the game"""
        self._player_num = num

    def set_game(self, game):
        """Method: Sets game state"""
        self._game = game

    def add_turn(self):
        """Method: Iterates turn counter"""
        self._turn += 1

    def check_win(self, player, tp_score):
        """Method: Checks if the current player has won"""
        if player.get_score() >= 30 or (player.get_score() + tp_score >= 30):
            print("{} WINS!!".format(player.get_name()))
            self.set_game(False)
            return True
        return False

    def check_game(self):
        """Method: Checks game state"""
        if self.get_game() is False:
            print("Thank you for playing!\n")
        return True

    def setup(self):
        """Method: Sets the game up"""
        counter = 0
        x_num = 1
        player_names = []
        players = []
        input_num = False
        name_loop = True
        print("___Up to 4 players___\n")

        while input_num is False:
            try:
                self.set_players(int(input("How many players: ")))
                if self.get_players() < 1 or self.get_players() > 4:
                    print("Please input a number from 1 - 4")
                else:
                    input_num = True
            except ValueError:
                print("Please input a number from 1 - 4")

        if self.get_players() == 1:
            print("You will face Tom the Computer")
            players.append(c())
            player_names.append("CPU Tom")
            counter = 1
            self.set_players(2)

        while counter < self.get_players():
            while name_loop:
                name = input("What is Player {}'s name?\n".format(str(x_num)))
                if name not in player_names:
                    name_loop = False
                else:
                    print("Duplicate name detected. Input a different name.")

            players.append(p(name))
            player_names.append(name)
            check_name(players, player_names, counter, x_num)
            counter += 1
            x_num += 1
            name_loop = True

        players = order(players)
        return players

    def turn(self, player, players):
        """Method: Runs the current player's turn"""
        print("{}'s Turn\n".format(player.player_name))
        roll = 0
        tp_score = 0
        n_rolls = 0
        while True:
            print("\n**************************")
            n_rolls += 1
            if player.get_player_type() == "CPU":
                roll = player.cpu_does_roll()
            else:
                roll = player.does_roll()
            print("\n**Times rolled: {}**".format(n_rolls))
            print("**ROLL: {}**".format(roll))
            time.sleep(1)
            if check_die(roll) is True:
                print("You rolled a 1\nYou have lost", tp_score, "points.")
                self.add_turn()
                break
            tp_score += roll
            print(
                "Current turn score: {}\n".format(tp_score),
                "Current Player score: {}\n".format(player.get_score()),
                "What-if score: {}".format(tp_score + player.get_score()),
            )
            time.sleep(1)
            if self.check_win(player, tp_score) is True:
                break
            if player.get_player_type() == "CPU":
                if player.cpu_roll_again(players, tp_score, n_rolls) is False:
                    player.set_score(player.get_score() + tp_score)
                    print(
                        "You rolled {} points! Your score is now: {}".format(
                            tp_score, player.get_score()
                        )
                    )
                    self.add_turn()
                    return player
            else:
                if player.roll_again() is False:
                    player.set_score(player.get_score() + tp_score)
                    print(
                        "You rolled {} points! Your score is now: {}".format(
                            roll, player.get_score()
                        )
                    )
                    self.add_turn()
                    return player
        return player

    def run(self):
        """Method: Runs the game"""
        players = self.setup()
        while self.get_game() is True:
            print(
                "----------------------------------------\nTurn: {}\n".format(
                    self.get_turn()
                )
            )
            self.check_game()
            self.turn(players[0], players)
            if self.get_game() is True:
                next_player(players)
            time.sleep(2)
        again = input("Do you want to play again? Yes or No? ")
        if again.lower() == "yes":
            self.reset()
            self.run()
        else:
            print("\nTHANKS FOR PLAYING!!")


def check_name(players, player_names, counter, x_num):
    """Function: Checks player names for duplicates"""
    if players[counter].get_name() == "":
        players[counter].set_name("Player {}".format(str(x_num)))
        player_names[counter] = "Player {}".format(str(x_num))


def check_die(roll):
    """Function: Checks if the die rolled a 1"""
    return roll == 1


def order(players):
    """Function: Builds the player order"""
    print("Highest roll goes first:")
    time.sleep(1)
    order_die = d()
    for player in players:
        player.set_order(order_die.roll_order())
        order_die.change_order_die(player.player_order)
        print("{} rolls a {}".format(player.get_name(), player.get_order()))
        time.sleep(1)
    players.sort(key=lambda player: player.get_order(), reverse=True)
    print("\nTurn Order:", players)
    return players


def next_player(players):
    """Method: Goes to next player in queue"""
    print("\nNext player...\n")
    players.append(players[0])
    players.remove(players[0])
    return players
