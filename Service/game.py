class Game:
    def __init__(self, board, human, computer, strategy):
        self.__board = board
        self._computer = computer
        self._human = human
        self.strategy = strategy

    def get_board_dimensions(self):
        return self.__board.rows, self.__board.columns

    def get_cell_value(self, row, column):
        return self.__board.get_row_column_value(row, column)

    def winning_move(self, value):
        return self.__board.winning_move(value)

    def game_draw(self):
        return not len(self.__board.get_valid_locations())

    def get_board_str(self):
        return str(self.__board)

    def computer_move(self):
        """
        Function for computer move. It calls the minimax function from strategy to get the best column choice for
        the move and it calls self._computer.move to perform the move
        :return: -
        """
        AI = 2
        COLUMN_POSITION = 0
        DEPTH = 4
        column = self.strategy.minimax(self.__board, DEPTH, float("-inf"), float("inf"), AI)[COLUMN_POSITION]
        row = self.__board.get_next_open_row(column)
        self._computer.move(self.__board, row, column)

    def human_move(self, column):
        """
        Function that calls self._human.move for the column received as parameter and the first open row on that column
        :param column: integer number < the number of columns on the board of the game
        :return:-
        """
        row = self.__board.get_next_open_row(column)
        self._human.move(self.__board, row, column)
