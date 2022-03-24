import numpy


class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.__empty_value = 0
        self.__board = self.__create_board()

    def get_row_column_value(self, row, column):
        return self.__board[row][column]

    def __create_board(self):
        return numpy.zeros((self.rows, self.columns))

    def set_value(self, row, column, value):
        self.__board[row][column] = value

    def get_next_open_row(self, column):
        """
        Function that finds the first open row on column given as parameter
        :param column: positive integer number < the numbers of columns of the board
        :return: the number of the first open row for given column as integer
        """
        for row in range(self.rows):
            if self.__board[row][column] == 0:
                return row

    def is_terminal_node(self):
        HUMAN = 1
        AI = 2
        return self.winning_move(HUMAN) or self.winning_move(AI) or (len(self.get_valid_locations()) == 0)

    def is_valid_location(self, column):
        return self.__board[self.rows - 1][column] == 0

    def get_valid_locations(self):
        """
        Function that finds all the valid locations on board (all the columns that are not full)
        :return: a list of valid locations
        """
        valid_locations = []
        for column in range(self.columns):
            if self.is_valid_location(column):
                valid_locations.append(column)
        return valid_locations

    def get_row_values(self, row):
        return [cell for cell in self.__board[row]]

    @staticmethod
    def evaluate_area(area):
        """
        Function that evaluates a given area from the board and computes the score for it for the computer pieces
        :param area: list of cells from the board
        :return: the score computed for given area
        """
        score = 0
        empty = 0
        AI = 2
        HUMAN = 1
        if area.count(AI) == 4:
            score += 1000000
        elif area.count(AI) == 3 and area.count(empty) == 1:
            score += 5
        elif area.count(AI) == 2 and area.count(empty) == 2:
            score += 2
        if area.count(HUMAN) == 3 and area.count(empty) == 1:
            score -= 1000000000000000000
        return score

    def score_position(self):
        """
        Function that evaluates the current position of the computer pieces and returns the score of the current
        position
        :return:
        """
        WINDOW_LENGTH = 4
        score = 0
        COLUMN_COUNT = 7
        HALF = 3
        ROW_COUNT = 6
        AI = 2
        center_array = [int(cell) for cell in list(self.__board[:, COLUMN_COUNT // 2])]
        center_count = center_array.count(AI)
        score += center_count * 3
        for row in range(ROW_COUNT):
            row_array = [int(cell) for cell in list(self.__board[row, :])]
            for column in range(COLUMN_COUNT - HALF):
                window = row_array[column:column + WINDOW_LENGTH]
                score += self.evaluate_area(window)
        for column in range(COLUMN_COUNT):
            column_array = [int(cell) for cell in list(self.__board[:, column])]
            for row in range(ROW_COUNT - HALF):
                window = column_array[row:row + WINDOW_LENGTH]
                score += self.evaluate_area(window)
        for row in range(ROW_COUNT - HALF):
            for column in range(COLUMN_COUNT - HALF):
                window = [self.__board[row + index][column + index] for index in range(WINDOW_LENGTH)]
                score += self.evaluate_area(window)
        for row in range(ROW_COUNT - HALF):
            for column in range(COLUMN_COUNT - HALF):
                window = [self.__board[row + HALF - index][column + index] for index in range(WINDOW_LENGTH)]
                score += self.evaluate_area(window)
        return score

    def winning_move(self, piece):
        """
        Function that checks if the piece given as parameter has a winning move on the board
        :param piece: natural number 1/2
        :return: True if there is at least one winning move on the board for the given piece, false otherwise
        """
        COLUMN_COUNT = 7
        ROW_COUNT = 6
        HALF = 3
        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT - HALF):
                if self.__board[row][column] == piece and self.__board[row + 1][column] == piece \
                        and self.__board[row + 2][column] == piece and self.__board[row + 3][column] == piece:
                    return True
        for column in range(COLUMN_COUNT - HALF):
            for row in range(ROW_COUNT):
                if self.__board[row][column] == piece and self.__board[row][column + 1] == piece\
                        and self.__board[row][column + 2] == piece and self.__board[row][column + 3] == piece:
                    return True
        for column in range(COLUMN_COUNT - HALF):
            for row in range(ROW_COUNT - HALF):
                if self.__board[row][column] == piece and self.__board[row + 1][column + 1] == piece\
                        and self.__board[row + 2][column + 2] == piece and \
                        self.__board[row + 3][column + 3] == piece:
                    return True
        for column in range(COLUMN_COUNT - HALF):
            for row in range(HALF, ROW_COUNT):
                if self.__board[row][column] == piece and self.__board[row - 1][column + 1] == piece \
                        and self.__board[row - 2][column + 2] == piece and \
                        self.__board[row - 3][column + 3] == piece:
                    return True
        return False

    def __str__(self):
        result = ""
        for line in range(self.rows-1, -1, -1):
            string = " ".join([str(int(cell)) for cell in self.__board[line]]) + "\n"
            result += string
        return result
