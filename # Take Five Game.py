import random

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
            print("\nPlayer #{}'s hand = {}" .format(pl[0], list(pl[1].hand)))
    def round_start_deal(self, board):
        for table_rows in board.board.items():
            table_rows[1].append(random.sample(list(self.deck), 1)[0])

class Player():
    def __init__(self):
        self.hand = []
        self.bull_pile = {}            # {turn number : [ (card_num, card_val), ... ]}, ... }
        self.game_points = {}          # {round number: self.bull_pile} 
        self.rounds_won = 0
        self.games_won = 0
    def show_round_scores(self):   # sum of score from self.bull_pile
        rpoint_total = 0
        for rounds in self.bull_pile.items():
            for cards in rounds[1]:
                rpoint_total += cards[1]
        return rpoint_total
    def show_game_points(self):
        gpoints_total = 0
        for games in self.game_points.items():
            for rounds in games[1].items():
                for cards in rounds[1]:
                    gpoints_total += cards[1]
        return gpoints_total
    def add_to_game_points(self, round_counter):
        self.game_points[round_counter] = self.bull_pile
        self.bull_pile = {}

class Board():
    def __init__(self):
        self.turn_rec = {}      # Dictionary log of {turn number : {player : (card_num, card_val)}, ...}
        self.board = {1:[], 2:[], 3:[], 4:[]}
    def show_board(self):
        print('\n Current game board ')
        for row, spaces in sorted(self.board.items()): print('row {}' .format(row), spaces)
        print('\n')
    def place_cards(self, players, round_counter): 
        self.turn_rec[len(self.turn_rec.items())+1] = {}                            # every turn adds new turn entry into self.turn_rec
        for pl in players.items():                                                  # iterate players and add chosen cards to the above line as key pairs
            print("\n Player #{}'s hand = {}" .format(pl[0], list(pl[1].hand)))
            c_card_indx = int(input('Enter the index location of the card to play \n'))
            self.turn_rec[len(self.turn_rec.items())][pl[0]] = (pl[1].hand[c_card_indx][0], pl[1].hand[c_card_indx][1])
            del pl[1].hand[c_card_indx]
        staged_cards = sorted(s_c for s_c in [p_c[1] for p_c in dict.items(self.turn_rec[len(self.turn_rec.items())])])     #list sorted by key of chosen cards as tuples [(card_num, card_val), ...]
        for card in staged_cards:
            target_row = (0,[0])        # (board row number, [list of cards in row])
            for rowlead_card in self.board.items():             # Searches for appropriate row to place card
                if rowlead_card[1][-1][0] > target_row[0] and card[0] > rowlead_card[1][-1][0]:
                    if target_row == (0,[0]):
                        target_row = rowlead_card
                    if abs(target_row[1][-1][0] - rowlead_card[1][-1][0]) > abs(card[0] - rowlead_card[1][-1][0]):
                        target_row = rowlead_card
            if target_row == (0,[0]):                                # if no appropriate row, choose to take a row and add it to player.bull_pile
                for player_of, pcard in self.turn_rec[len(self.turn_rec.items())].items():
                    if card == pcard:
                        print('\n Current game board ')
                        for row, spaces in sorted(self.board.items()): print(row, spaces)
                        print('\n')
                        row_to_take = int(input('Player {} Enter the row number to take ' .format(player_of)))
                        players[player_of].bull_pile[len(self.turn_rec.items())] = self.board.pop(row_to_take)
                        self.board[row_to_take] = [card]
                        print(players[player_of].bull_pile)
            else:                                               # if row full add to player.bull_pile then place card, if not full just place card 
                if len(self.board[target_row[0]]) == 5:
                    for player_of1, pcard1 in self.turn_rec[len(self.turn_rec.items())].items():
                        if card == pcard1:
                            players[player_of1].bull_pile[len(self.turn_rec.items())] = self.board.pop(target_row[0])
                            self.board[target_row[0]] = []
                self.board[target_row[0]].append(card)                      

class Monitor():
    def __init__(self):
        self.game_record = {}
        self.deck_after_round = {}
    def log_deck(self, deck):
        print('deck to be logged') # logs deck at end of round

session = True
game_on = True
session_monitor = Monitor()
round_counter = 0
game_counter = 0
players = {pl: Player() for pl in range(1,int(input('\n☆☆☆☆☆☆☆☆☆☆ Welcome to Take5 ☆☆☆☆☆☆☆☆☆☆\nhow many players? '))+1)}        #Dictionary of (2-10)players {player numbers : player objects}
while True:
    while game_on == True:
        deck = Deck()
        board = Board()
        round_counter += 1
        deck.deal_cards(deck, players)
        deck.round_start_deal(board)
        board.show_board()
        while len(board.turn_rec) < 10:
            board.place_cards(players, round_counter)
            board.show_board()
            continue
        for player in players.items():
            player[1].add_to_game_points(round_counter)
            print('\nplayer {} score is {}' .format(player[0], player[1].show_game_points()))
        for end_player in players.items():
            if end_player[1].show_game_points() >= 66:
                game_counter += 1
                game_on = False
    win_points = 99999
    winner = []
    for g_end_pl in players.items():
        if g_end_pl[1].show_game_points() < win_points:
            winner = g_end_pl
    winner[1].games_won += 1
    print('player {} wins with {} points!! 🎉' .format(winner[0], winner[1].show_game_points()))
    if input('Play again? (y/n) ') == 'y':
        game_on = True
    else:
        print('---Session Ended---')
        break