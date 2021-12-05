import random
import copy
# import math


class Strategy:
    def minimax(self, board, depth, alpha, beta, player):
        """
        Function that implements the minimax algorithm on a board for the AI
        :param board: game board
        :param depth: the depth of the graph (how many future moves does the algorithm analyze
        :param alpha: score used for the computer moves in order to optimise the algorithm with alfa-beta pruning
        :param beta: score used for the human moves in order to optimise the algorithm with alfa-beta pruning
        :param player: AI/HUMAN move value (2/1)
        :return: the best column choice for the next move and the score achieved with that move
        """
        HUMAN = 1
        AI = 2
        valid_moves = board.get_valid_locations()
        is_terminal = board.is_terminal_node()
        if depth == 3 and board.winning_move(AI):
            return None, 1000000000000000000
        # if depth == 2 and board.winning_move(HUMAN):
        #    return None, -100000000000
        if depth == 1 and board.winning_move(AI):
            return None, 1000000
        if depth == 0 or board.is_terminal_node():
            if board.is_terminal_node():
                if board.winning_move(HUMAN):
                    return None, -float("inf")
                else:
                    return None, 0
            else:
                return None, board.score_position()
        if player == AI:
            value = -float("inf")
            result_column = random.choice(valid_moves)
            for column in valid_moves:
                auxiliary_board = copy.deepcopy(board)
                row = auxiliary_board.get_next_open_row(column)
                auxiliary_board.set_value(row, column, AI)
                new_score = self.minimax(auxiliary_board, depth - 1, alpha, beta, HUMAN)[1]
                if new_score > value:
                    value = new_score
                    result_column = column
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return result_column, value
        else:
            value = float("inf")
            result_column = random.choice(valid_moves)
            for column in valid_moves:
                auxiliary_board = copy.deepcopy(board)
                row = auxiliary_board.get_next_open_row(column)
                auxiliary_board.set_value(row, column, HUMAN)
                new_score = self.minimax(auxiliary_board, depth - 1, alpha, beta, AI)[1]
                if new_score < value:
                    value = new_score
                    result_column = column
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return result_column, value
