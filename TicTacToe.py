"""
Cheng Tang's Tic Tac Toe Back end
Can play with AI with a brain / AI without a brain
"""
import random



def click(b):
    b['text'] = 'X'
    b['state'] = 'disabled'


class TicTacToe:
    def __init__(self):
        # 3x3 int array. 0 = empty, 1 = player, 2 = AI
        self.board = []
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append(0)

        # to make it easier to check empty spots and for the AI the generate random moves.
        self.choices = {"1": [0, 0], "2": [0, 1], "3": [0, 2], "4": [1, 0], "5": [1, 1], "6": [1, 2], "7": [2, 0],
                        "8": [2, 1], "9": [2, 2]}
        # keeping track of turns, 0 for player, 1 for AI
        self.turn = 0

        # True for hard mode, false for easy mode
        self.diff = True

        # keeping track of the scores
        self.player_score = 0
        self.AI_score = 0

    def print_board(self):
        # looks nicer this way, for debugging purposes since I am only working on backend.
        for i in range(3):
            print(self.board[i])

    def clear_board(self):
        """
        empty board and reset choices
        """
        # reset board to empty (0)
        for i in range(3):
            for j in range(3):
                self.board[i][j] = 0
        # reset choices
        self.choices = {"1": [0, 0], "2": [0, 1], "3": [0, 2], "4": [1, 0], "5": [1, 1], "6": [1, 2], "7": [2, 0],
                        "8": [2, 1], "9": [2, 2]}

    def player_turn(self, x):
        # when it's players' turn
        #print(self.choices)
        # debugging purposes
        #self.print_board()
        # debugging purposes
        #x = input()
        # make moves on the board based on string inputs for now
        self.board[self.choices[x][0]][self.choices[x][1]] = 1
        self.choices.pop(x)
        # swap turns
        self.turn = 1

    def AI_turn_EZ(self):
        # randomly chooses an empty spot
        y = list(self.choices)[random.randint(0, len(self.choices) - 1)]
        self.board[self.choices[str(y)][0]][self.choices[str(y)][1]] = 2
        self.choices.pop(str(y))
        # swap turns
        self.turn = 0
        return int(y)

    def check_board(self):
        # check horizontally, vertically, diagonally
        result = 0
        for i in range(0, 3):
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] != 0:
                result = self.board[0][i]
                return result
            elif self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][
                0] != 0:
                result = self.board[i][0]
                return result
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            result = self.board[0][0]
            return result
        elif self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != 0:
            result = self.board[0][2]
            return result
        else:
            # check for tie
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.board[i][j] == 0:
                        return result
            result = 3
            return result

    def easy_mode(self):
        self.clear_board()
        while True:
            # check the board state before each move
            result = self.check_board()
            if result != 0:
                # assigning scores
                if result == 1:
                    self.player_score = self.player_score + 1
                elif result == 2:
                    self.AI_score = self.AI_score + 1
                break
            else:
                if self.turn == 0:
                    self.player_turn()
                elif self.turn == 1:
                    self.AI_turn_EZ()

    def minimax(self, turn):
        # https://www.youtube.com/watch?v=fT3YWCKvuQE&t=750s
        # Borrowed idea from Kylie Ying
        temp = self.check_board()
        # check if the game is over
        # if it is, calculate the score, usually people return -1 or 1 everytime they go down the tree
        # but I thought Kylie's calculation of score using remaining spaces was amazing, so I borrowed it
        if temp != 0:
            if temp == 1:
                return {'move': None, 'score': (-1 * (len(self.choices) + 1))}
            # if the player wins, the score is negative since the player wants to minimize while we want to maximize
            elif temp == 2:
                return {'move': None, 'score': (1 * (len(self.choices) + 1))}
            # if we win, the score is positive since we want to maximize our scores and see which move gives us the
            # highest score
            else:
                # if it's a tie, score is 0
                return {'move': None, 'score': 0}

        if turn == 0:
            best = {'move': None, 'score': 99999}
            # 99999 is basically positive infinity, turn 0 is players' turn, and he wants to minimize score
        else:
            best = {'move': None, 'score': -99999}
            # -99999 is basically positive infinity, turn 1 is AI's turn, and we want to maxmize our scores

        for i in list(self.choices):
            move = self.choices[i]
            # go down the list of choices, and play there
            if turn == 0:
                # assume the player plays at this spot
                self.board[move[0]][move[1]] = 1
                self.choices.pop(i)
                temp_score = self.minimax(turn + 1)
                # minimax the AI's turn
            else:
                # assume AI plays at this spot
                self.board[move[0]][move[1]] = 2
                self.choices.pop(i)
                temp_score = self.minimax(turn - 1)
                # minimax player's turn
            self.board[move[0]][move[1]] = 0
            # after we have our score (the game is over) for that move in the list
            # put this move back and go down the for loop for next move
            self.choices[i] = move
            # keep track of this move
            temp_score['move'] = i
            if turn == 0:
                # AI wants to maximize, player wants to minimize
                if temp_score['score'] < best['score']:
                    best = temp_score
            else:
                if temp_score['score'] > best['score']:
                    best = temp_score
        # after the for loop, return the move (the iterator) with the highest score
        return best
        # additionally, I think it's very smart that Kylie implemented the return type as a set
        # that keeps track of both moves and the score. (I was struggling on how to return moves at first)

    def hard_mode(self):
        self.clear_board()
        if self.turn == 1:
            # always takes corner if AI starts first
            y = random.choice([1, 3, 7, 9])
            self.board[self.choices[str(y)][0]][self.choices[str(y)][1]] = 2
            self.choices.pop(str(y))
            # player's turn after
            self.player_turn()
            # take center after if possible
            if self.board[1][1] == 0:
                self.board[1][1] = 2
                self.choices.pop("5")
                self.player_turn()
        else:
            # if player starts first
            self.player_turn()
            # then take center if possible
            if self.board[1][1] == 0:
                self.board[1][1] = 2
                self.choices.pop("5")
            else:
                # if center is taken as the first step by the player, we have to take either 1 3 7 9
                y = random.choice([1, 3, 7, 9])
                self.board[self.choices[str(y)][0]][self.choices[str(y)][1]] = 2
                self.choices.pop(str(y))
            # player's turn next
            self.player_turn()

        # just before we go into minimax algorithm, the above steps are so that we can save some runtime (not sure by
        # how much) since there isn't any point calculating the best move when the board is near empty. Simple
        # strategy to never lose: if we are starting, take the corner first and center if possible else: just take
        # center if possible

        while True:
            # check the board state before each move
            result = self.check_board()
            if result != 0:
                # assigning scores
                if result == 1:
                    self.player_score = self.player_score + 1
                elif result == 2:
                    self.AI_score = self.AI_score + 1
                break
            else:
                if self.turn == 0:
                    self.player_turn()
                elif self.turn == 1:
                    # returns the best option
                    y = self.minimax(self.turn)['move']
                    y = str(y)
                    self.board[self.choices[y][0]][self.choices[y][1]] = 2
                    self.choices.pop(str(y))
                    # don't forget to swap players
                    self.turn = 0


# test
if __name__ == '__main__':

    TTT = TicTacToe()
    while True:
        ans = input("0 for easy, 1 for hard \n")
        if ans == "0":
            TTT.easy_mode()
            TTT.print_board()
            print("AI: " + str(TTT.AI_score) + "  Player: " + str(TTT.player_score))
        else:
            TTT.hard_mode()
            TTT.print_board()
            print("AI: " + str(TTT.AI_score) + "  Player: " + str(TTT.player_score))
