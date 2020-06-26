# Take Five Simulation
import random

# Objects
class Deck(): 
    def __init__(self): 
        self.deck = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 2), (6, 1), (7, 1), (8, 1), (9, 1), (10, 3), (11, 5), (12, 1), (13, 1), (14, 1), (15, 2), (16, 1), (17, 1), (18, 1), (19, 1), (20, 3), (21, 1), (22, 5), (23, 1), (24, 1), (25, 2), (26, 1), (27, 1), (28, 1), (29, 1), (30, 3), (31, 1), (32, 1), (33, 5), (34, 1), (35, 2), (36, 1), (37, 1), (38, 1), (39, 1), (40, 3), (41, 1), (42, 1), (43, 1), (44, 5), (45, 3), (46, 1), (47, 1), (48, 1), (49, 1), (50, 3), (51, 1), (52, 1), (53, 1), (54, 1), (55, 7), (56, 1), (57, 1), (58, 1), (59, 1), (60, 3), (61, 1), (62, 1), (63, 1), (64, 1), (65, 2), (66, 5), (67, 1), (68, 1), (69, 1), (70, 3), (71, 1), (72, 1), (73, 1), (74, 1), (75, 2), (76, 1), (77, 5), (78, 1), (79, 1), (80, 3), (81, 1), (82, 1), (83, 1), (84, 1), (85, 2), (86, 1), (87, 1), (88, 5), (89, 1), (90, 3), (91, 1), (92, 1), (93, 1), (94, 1), (95, 2), (96, 1), (97, 1), (98, 1), (99, 5), (100, 3), (101, 1), (102, 1), (103, 1), (104, 1)]
    def __str__(self):
        return str(self.deck)
    def deal_cards(self, deck, players):
        for pl in players.items():
            for c in random.sample(list(self.deck), 10):
                    pl[1].hand.insert(0,c)
                    self.deck.remove(c)
            print("Player #{}'s hand = {}" .format(pl[0], list(pl[1].hand)))
    def round_start_deal(self, board):
        for table_rows in board.board.items():
            table_rows[1].append(random.sample(list(self.deck), 1)[0])

class Player():
    def __init__(self):
        self.hand = []
        self.points = {}            # {Round number : cards, ...}
        self.rounds_won = 0
        self.games_won = 0
    def add_points(self, round_end_points):
        self.points += round_end_points
    def ret_scores(self):   # sum of score from self.points
        point_total = 0
        for rounds in self.points.items():
            for cards in rounds[1]:
                point_total += cards[1]
        return point_total

class Board():
    def __init__(self):
        self.turn_rec = {}      # Dictionary log of {turn number : {player : (card_num, card_val)}, ...}
        self.board = {1:[], 2:[], 3:[], 4:[]}
    def show(self):
        print('\n Current game board ')
        for row, spaces in sorted(self.board.items()): print(row, spaces)
        print('\n')
    def place_cards(self, players): 
        self.turn_rec[len(self.turn_rec.items())+1] = {}                            # every turn adds new turn entry into self.turn_rec
        for pl in players.items():                                                  # iterate players and add chosen cards to the above line as key pairs
            print("\n Player #{}'s hand = {}" .format(pl[0], list(pl[1].hand)))
            c_card_indx = int(input('Enter the index location of the card to play \n'))
            self.turn_rec[len(self.turn_rec.items())][pl[0]] = (pl[1].hand[c_card_indx][0], pl[1].hand[c_card_indx][1])
            del pl[1].hand[c_card_indx]
        staged_cards = sorted(s_c for s_c in [p_c[1] for p_c in dict.items(self.turn_rec[len(self.turn_rec.items())])]) #list sorted by key of chosen cards as tuples [(card_num, card_val), ...]
        print('\n{} staged cards' .format(staged_cards))
        print('\n{} turn_rec ' .format(self.turn_rec))
        for card in staged_cards:
            target_row = (0,[0]) # (board row number, [list of cards in row])
            for rowlead_card in self.board.items():             # Searches for appropriate row to place card
                print('\n{} rowlead_card[1][-1]' .format(rowlead_card[1][-1]))
                print('\n{} target_row[1][-1]' .format(target_row[1][-1]))
                print('\n{} card[0]' .format(card[0]))
                if rowlead_card[1][-1][0] > target_row[0] and card[0] > rowlead_card[1][-1][0]:
                    if target_row == (0,[0]):
                        target_row = rowlead_card
                    if abs(target_row[1][-1][0] - rowlead_card[1][-1][0]) > abs(card[0] - rowlead_card[1][-1][0]):
                        target_row = rowlead_card
            if target_row == (0,[0]):                                # if no appropriate row, choose to take a row and add it to player.points
                for player_of, pcard in self.turn_rec[len(self.turn_rec.items())].items():
                    if card == pcard:
                        print('\n Current game board ')
                        for row, spaces in sorted(self.board.items()): print(row, spaces)
                        print('\n')
                        row_to_take = int(input('Player {} Enter the row number to take ' .format(player_of)))
                        players[player_of].points[len(self.turn_rec.items())] = self.board.pop(row_to_take)
                        self.board[row_to_take] = [card]
                        print(players[player_of].points)
            else:                                               # if row full add to player.points then place card, if not full just place card 
                print('\n{} target_row[0]' .format(target_row[0]))
                if len(self.board[target_row[0]]) == 5:
                    for player_of1, pcard1 in self.turn_rec[len(self.turn_rec.items())].items():
                        if card == pcard1:
                            players[player_of1].points[len(self.turn_rec.items())] = self.board.pop(target_row[0])
                            self.board[target_row[0]] = []
                self.board[target_row[0]].append(card)
    def                         

class Monitor():
    def __init__(self):
        self.game_count = 1
        self.deck_after_round = {}


deck = Deck()
players = {pl: Player() for pl in range(1,int(input('how many people are playing?'))+1)}        #Dictionary of (2-10)players {player numbers : player objects}
board = Board()
deck.deal_cards(deck, players)
deck.round_start_deal(board)
board.show()
while len(board.turn_rec) < 10:
    board.place_cards(players)
    board.show()
    continue
for player in players.items():
    if player[1].ret_scores() => 66:
        for end_player in in players.items():
            winner = 0
            if end_player[1].ret_scores() > winner:
                winner = end_player[1].ret_scores()
        # add to game count
        # add to player win count
        print('player {} wins!!' .format(end_player[0]))
        break
if player[1].ret_scores() < 66:
    print('ok')
        # add to player round wins
        #  
