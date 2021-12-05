import random


class UI:
    def __init__(self, game):
        self.__game = game

    def print_board(self):
        print(self.__game.get_board_str())

    def start(self):
        AI = 2
        HUMAN = 1
        HUMAN_MOVE = 0
        turn = random.randint(0, 1)
        self.print_board()
        game_over = False
        while not game_over:
            if turn % 2 == HUMAN_MOVE:
                column = int(input("Human >>"))
                while column not in range(7):
                    column = int(input("Human >>"))
                self.__game.human_move(column)
                if self.__game.winning_move(HUMAN):
                    print("HUMAN WINS")
                    game_over = True
                elif self.__game.game_draw():
                    print("DRAW")
                    game_over = True
            else:
                self.__game.computer_move()
                self.print_board()
                if self.__game.winning_move(AI):
                    print("COMPUTER WINS")
                    game_over = True
                elif self.__game.game_draw():
                    print("DRAW")
                    game_over = True
            turn += 1
