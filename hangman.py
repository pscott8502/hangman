#!/usr/bin/python3

class Board:
    def __init__(self, word_to_guess):
        self.boardlist = ["_" for x in word_to_guess]
        self.word_to_guess = " ".join(word_to_guess)
        self.boardlist = list(" ".join(self.boardlist))

    def display_board(self):
        print("".join(self.boardlist))

    def update_board(self, update_letter):
        for index, letter in enumerate(self.word_to_guess):
            if update_letter == letter:
                self.boardlist[index] = update_letter
        board.display_board()

    def guess_tracker(self, update_letter):
        
                

secret_word = input("What is Your Secret Word? ")
board = Board(secret_word)
board.display_board()
while True:
    players_guess = input("What is Your Guess? ")
    board.update_board(players_guess)
