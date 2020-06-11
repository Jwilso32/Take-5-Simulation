# Take Five Simulation
import random

# Objects
class Deck():
    def __init__(self):
        self.deck = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1, 10: 3, 11: 5, 12: 1, 13: 1, 14: 1, 15: 2, 16: 1, 17: 1, 18: 1, 19: 1, 20: 3, 21: 1, 22: 5, 23: 1, 24: 1, 25: 2, 26: 1, 27: 1, 28: 1, 29: 1, 30: 3, 31: 1, 32: 1, 33: 5, 34: 1, 35: 2, 36: 1, 37: 1, 38: 1, 39: 1, 40: 3, 41: 1, 42: 1, 43: 1, 44: 5, 45: 3, 46: 1, 47: 1, 48: 1, 49: 1, 50: 3, 51: 1, 52: 1, 53: 1, 54: 1, 55: 7, 56: 1, 57: 1, 58: 1, 59: 1, 60: 3, 61: 1, 62: 1, 63: 1, 64: 1, 65: 2, 66: 5, 67: 1, 68: 1, 69: 1, 70: 3, 71: 1, 72: 1, 73: 1, 74: 1, 75: 2, 76: 1, 77: 5, 78: 1, 79: 1, 80: 3, 81: 1, 82: 1, 83: 1, 84: 1, 85: 2, 86: 1, 87: 1, 88: 5, 89: 1, 90: 3, 91: 1, 92: 1, 93: 1, 94: 1, 95: 2, 96: 1, 97: 1, 98: 1, 99: 5, 100: 3, 101: 1, 102: 1, 103: 1, 104: 1}
    def __str__(self):
        return str(self.deck)
    def deal_cards(self, deck, players):
        for pl in players.items():
            for c in random.sample(list(self.deck), 10):
                    pl[1].hand[c] = self.deck[c]
                    del self.deck[c]
            print("Player #{}'s hand = {}" .format(pl[0], list(pl[1].hand.items())))
             
class Player():
    def __init__(self):
        self.hand = {}
        self.points = 0
        self.rounds_won = 0
        self.games_won = 0
    def add_points(self, round_end_points):
        self.points += round_end_points

class Board():
    def __init__(self):
        self.turn_rec = {}                                      # Dictionary log of {turn number : {player : card played}}
        self.board_row1 = ['   ','   ','   ','   ','   ']
        self.board_row2 = ['   ','   ','   ','   ','   ']
        self.board_row3 = ['   ','   ','   ','   ','   ']
        self.board_row4 = ['   ','   ','   ','   ','   ']
    def show(self):
        print(self.board_row1[1] + ' | ' + self.board_row1[2] + ' | ' + self.board_row1[3] + ' | ' + self.board_row1[4] + '\n--------------------\n' + self.board_row2[1] + ' | ' + self.board_row2[2] + ' | ' + self.board_row2[3] + ' | ' + self.board_row2[4] + '\n--------------------\n' + self.board_row3[1] + ' | ' + self.board_row3[2] + ' | ' + self.board_row3[3] + ' | ' + self.board_row3[4] + '\n--------------------\n' + self.board_row4[1] + ' | ' + self.board_row4[2] + ' | ' + self.board_row4[3] + ' | ' + self.board_row4[4])
    def place_cards(self, players): 
        self.turn_rec[len(self.turn_rec.items())+1] = {}
        for pl in players.items():                                                          # cycle through players and add choices to the above line as key pairs
            print("Player #{}'s hand = {}" .format(pl[0], list(pl[1].hand.items())))
            ch_card_key = input('Enter the number of the card to play ')
            self.turn_rec[len(self.turn_rec.items())][pl[0]] = ch_card_key
        print(list(self.turn_rec.items()))

class Game():
    def __init__(self):
        self.round_count = 0

deck = Deck()
players = {pl: Player() for pl in range(1,int(input('how many people are playing?'))+1)}    #Dictionary of 2 - 10 {player numbers : player objects}
board = Board()
deck.deal_cards(deck, players)
board.show()
board.place_cards(players)