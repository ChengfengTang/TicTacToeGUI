#Lynn & Cheng
import tkinter as tk
import tkinter.messagebox
from TicTacToe import TicTacToe
import random


class main_app(tk.Frame):
    def __init__(self, root):
        self.root = root
        self._game = TicTacToe()
        self.var = tk.IntVar()
        self.b1 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(1))
        self.b1.grid(row=0, column=0)
        self.b2 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(2))
        self.b2.grid(row=0, column=1)
        self.b3 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(3))
        self.b3.grid(row=0, column=2)
        self.b4 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(4))
        self.b4.grid(row=1, column=0)
        self.b5 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(5))
        self.b5.grid(row=1, column=1)
        self.b6 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(6))
        self.b6.grid(row=1, column=2)
        self.b7 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(7))
        self.b7.grid(row=2, column=0)
        self.b8 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(8))
        self.b8.grid(row=2, column=1)
        self.b9 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(9))
        self.b9.grid(row=2, column=2)
        self.play_label = tk.Label(text='Play:', height=1, width=8, font=('Comic Sans MS', 18, 'bold'))
        self.play_label.grid(row=3, column=0, pady=2, columnspan=1, sticky='e')
        self.score_label = tk.Label(text='Score: ', height=1, width=8, font=('Comic Sans MS', 18, 'bold'))
        self.score_label.grid(row=4, column=0, pady=2, columnspan=1, sticky='e')
        self.easy_button = tk.Button(text='Easy', height=1, width=9, font=('Comic Sans MS', 16, 'bold'),
                                     command=lambda: self.mode_click(self.easy_button))
        self.easy_button.grid(row=3, column=1, padx=5, columnspan=1, sticky='e')
        self.hard_button = tk.Button(text='Hard', height=1, width=9, font=('Comic Sans MS', 16, 'bold'),
                                     command=lambda: self.mode_click(self.hard_button))
        self.hard_button.grid(row=3, column=2, padx=5, columnspan=1, sticky='w')
        self.x_score = tk.Label(text='Player: ' + str(self._game.player_score), height=1, width=9,
                                font=('Comic Sans MS', 16, 'bold'))
        self.x_score.grid(row=4, column=1)
        self.o_score = tk.Label(text='AI: ' + str(self._game.AI_score), height=1, width=9,
                                font=('Comic Sans MS', 16, 'bold'))
        self.o_score.grid(row=4, column=2, padx=5, columnspan=1, sticky='w')

    def enable_buttons(self):
        self.b1['state'] = 'active'
        self.b2['state'] = 'active'
        self.b3['state'] = 'active'
        self.b4['state'] = 'active'
        self.b5['state'] = 'active'
        self.b6['state'] = 'active'
        self.b7['state'] = 'active'
        self.b8['state'] = 'active'
        self.b9['state'] = 'active'

    def update_score(self):
        self.x_score = tk.Label(text='Player: ' + str(self._game.player_score), height=1, width=9,
                                font=('Comic Sans MS', 16, 'bold'))
        self.x_score.grid(row=4, column=1)
        self.o_score = tk.Label(text='AI: ' + str(self._game.AI_score), height=1, width=9,
                                font=('Comic Sans MS', 16, 'bold'))
        self.o_score.grid(row=4, column=2, padx=5, columnspan=1, sticky='w')

    def player_turn(self):
        print(self._game.choices)
        self._game.print_board()
        print("waiting...")
        self.b1.wait_variable(self.var)
        x = str(self.var.get())
        self.disable_button(x)
        print(x)
        self._game.player_turn(x)

    def mode_click(self, mode_button):
        self._game.clear_board()
        self.reset()
        if self._game.turn == 0:
            tkinter.messagebox.showerror('Tic Tac Toe', 'You are starting.')

        if mode_button['text'] == 'Easy':
            while True:
                result = self._game.check_board()
                if result != 0:
                    # assigning scores
                    if result == 1:
                        tkinter.messagebox.showerror('Tic Tac Toe', 'Congratulation, you won!.')
                        self._game.player_score = self._game.player_score + 1
                        self.update_score()
                    elif result == 2:
                        tkinter.messagebox.showerror('Tic Tac Toe', 'You lost :( .')
                        self._game.AI_score = self._game.AI_score + 1
                        self.update_score()
                    elif result == 3:
                        tkinter.messagebox.showerror('Tic Tac Toe', 'It was a tie! .')
                    self.disable_all_button()
                    break
                else:
                    if self._game.turn == 0:
                        self.player_turn()
                    elif self._game.turn == 1:
                        y = str(self._game.AI_turn_EZ())
                        print(y)
                        self.draw_AI_move(y)
                        self._game.print_board()

        elif mode_button['text'] == 'Hard':
            if self._game.turn == 1:
                # always takes corner if AI starts first
                y = random.choice([1, 3, 7, 9])
                self._game.board[self._game.choices[str(y)][0]][self._game.choices[str(y)][1]] = 2
                self._game.choices.pop(str(y))
                self.draw_AI_move(str(y))
                # player's turn after
                self.player_turn()
                # take center after if possible
                if self._game.board[1][1] == 0:
                    self._game.board[1][1] = 2
                    self._game.choices.pop("5")
                    self.b5['text'] = 'O'
                    self.b5['state'] = 'disabled'
                    self.player_turn()
                    self._game.print_board()
            else:
                # if player starts first
                self.player_turn()
                # then take center if possible
                if self._game.board[1][1] == 0:
                    self._game.board[1][1] = 2
                    self._game.choices.pop("5")
                    self.draw_AI_move("5")
                else:
                    # if center is taken as the first step by the player, we have to take either 1 3 7 9
                    y = random.choice([1, 3, 7, 9])
                    self._game.board[self._game.choices[str(y)][0]][self._game.choices[str(y)][1]] = 2
                    self._game.choices.pop(str(y))
                    self.draw_AI_move(str(y))
                # player's turn next
                self.player_turn()

            # just before we go into minimax algorithm, the above steps are so that we can save some runtime (not sure by
            # how much) since there isn't any point calculating the best move when the board is near empty. Simple
            # strategy to never lose: if we are starting, take the corner first and center if possible else: just take
            # center if possible

            while True:
                # check the board state before each move
                result = self._game.check_board()
                if result != 0:
                    # assigning scores
                    if result == 1:
                        tkinter.messagebox.showerror('Tic Tac Toe', 'Congratulation, you won!.')
                        self._game.player_score = self._game.player_score + 1
                        self.update_score()
                    elif result == 2:
                        tkinter.messagebox.showerror('Tic Tac Toe', 'You lost :( .')
                        self._game.AI_score = self._game.AI_score + 1
                        self.update_score()
                    elif result == 3:
                        tkinter.messagebox.showerror('Tic Tac Toe', 'It was a tie! .')
                    self.disable_all_button()
                    break
                else:
                    if self._game.turn == 0:
                        self.player_turn()
                    elif self._game.turn == 1:
                        # returns the best option
                        y = self._game.minimax(self._game.turn)['move']
                        y = str(y)
                        self._game.board[self._game.choices[y][0]][self._game.choices[y][1]] = 2
                        self._game.choices.pop(str(y))
                        self.draw_AI_move(str(y))
                        # don't forget to swap players
                        self._game.turn = 0

    def draw_AI_move(self, y):
        if y == '1':
            self.b1['text'] = 'O'
            self.b1['state'] = 'disabled'
        elif y == '2':
            self.b2['text'] = 'O'
            self.b2['state'] = 'disabled'
        elif y == '3':
            self.b3['text'] = 'O'
            self.b3['state'] = 'disabled'
        elif y == '4':
            self.b4['text'] = 'O'
            self.b4['state'] = 'disabled'
        elif y == '5':
            self.b5['text'] = 'O'
            self.b5['state'] = 'disabled'
        elif y == '6':
            self.b6['text'] = 'O'
            self.b6['state'] = 'disabled'
        elif y == '7':
            self.b7['text'] = 'O'
            self.b7['state'] = 'disabled'
        elif y == '8':
            self.b8['text'] = 'O'
            self.b8['state'] = 'disabled'
        elif y == '9':
            self.b9['text'] = 'O'
            self.b9['state'] = 'disabled'

    def disable_button(self, x):
        if x == '1':
            self.b1['text'] = 'X'
            self.b1['state'] = 'disabled'
        elif x == '2':
            self.b2['text'] = 'X'
            self.b2['state'] = 'disabled'
        elif x == '3':
            self.b3['text'] = 'X'
            self.b3['state'] = 'disabled'
        elif x == '4':
            self.b4['text'] = 'X'
            self.b4['state'] = 'disabled'
        elif x == '5':
            self.b5['text'] = 'X'
            self.b5['state'] = 'disabled'
        elif x == '6':
            self.b6['text'] = 'X'
            self.b6['state'] = 'disabled'
        elif x == '7':
            self.b7['text'] = 'X'
            self.b7['state'] = 'disabled'
        elif x == '8':
            self.b8['text'] = 'X'
            self.b8['state'] = 'disabled'
        elif x == '9':
            self.b9['text'] = 'X'
            self.b9['state'] = 'disabled'

    def reset(self):
        self.b1 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(1))
        self.b1.grid(row=0, column=0)
        self.b2 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(2))
        self.b2.grid(row=0, column=1)
        self.b3 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(3))
        self.b3.grid(row=0, column=2)
        self.b4 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(4))
        self.b4.grid(row=1, column=0)
        self.b5 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(5))
        self.b5.grid(row=1, column=1)
        self.b6 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(6))
        self.b6.grid(row=1, column=2)
        self.b7 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(7))
        self.b7.grid(row=2, column=0)
        self.b8 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(8))
        self.b8.grid(row=2, column=1)
        self.b9 = tk.Button(self.root, text=' ', height=3, width=8, font=('Comic Sans MS', 24, 'bold'),
                            command=lambda: self.var.set(9))
        self.b9.grid(row=2, column=2)

    def disable_all_button(self):
        self.b1['state'] = 'disabled'
        self.b2['state'] = 'disabled'
        self.b3['state'] = 'disabled'
        self.b4['state'] = 'disabled'
        self.b5['state'] = 'disabled'
        self.b6['state'] = 'disabled'
        self.b7['state'] = 'disabled'
        self.b8['state'] = 'disabled'
        self.b9['state'] = 'disabled'


if __name__ == '__main__':
    main = tk.Tk()
    main.title('Tic Tac Toe')
    main.geometry('510x600')
    main_app(main)
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    main.mainloop()
