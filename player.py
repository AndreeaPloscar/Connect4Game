
class Player:
    def __init__(self, value):
        self.value = value

    def move(self, board, line, column):
        """
        Function for performing the move of the player on the board at given coordinates
        :param board: given board to place the player's piece on
        :param line: the line where the piece will be placed
        :param column: the column where the piece will be placed
        :return: -
        """
        board.set_value(line, column, self.value)
