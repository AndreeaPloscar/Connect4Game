import pygame
import math
import sys
import random


class GUI:

    def __init__(self, game):
        self.__game = game
        pygame.init()
        self.square_size = 100
        self.radius = int(self.square_size / 2 - 5)
        self.rows, self.columns = self.__game.get_board_dimensions()
        self.width = self.columns * self.square_size
        self.height = (self.rows + 1) * self.square_size
        self.size = (self.width, self.height)
        self._screen = pygame.display.set_mode(self.size)
        pygame.display.update()
        self.draw_board()

    def draw_board(self):
        BLUE = (29, 145, 251)
        BLACK = (0, 0, 0)
        RED = (208, 3, 47)
        WHITE = (255, 255, 255)
        PLAYER = 0
        AI = 1
        pygame.display.update()

        for column in range(self.columns):
            for row in range(self.rows):
                pygame.draw.rect(self._screen, BLUE,
                                 (column * self.square_size, (row + 1) * self.square_size, self.square_size,
                                  self.square_size))
                pygame.draw.circle(self._screen, BLACK, (column * self.square_size + self.square_size / 2, (row + 3 / 2)
                                                         * self.square_size), self.radius)

        for column in range(self.columns):
            for row in range(self.rows):
                if self.__game.get_cell_value(row, column) == 1:
                    pygame.draw.circle(self._screen, RED, (column * self.square_size + self.square_size / 2, self.height -
                                                           (row + 1 / 2) * self.square_size), self.radius)
                elif self.__game.get_cell_value(row, column) == 2:
                    pygame.draw.circle(self._screen, WHITE,
                                       (column * self.square_size + self.square_size / 2, self.height - (row + 1 / 2) *
                                        self.square_size), self.radius)
        pygame.display.update()

    def start(self):
        BLUE = (29, 145, 251)
        BLACK = (0, 0, 0)
        RED = (208, 3, 47)
        WHITE = (255, 255, 255)
        HUMAN_MOVE = 0
        AI = 1
        AI_PIECE = 2
        HUMAN_PIECE = 1
        game_over = False
        turn = random.randint(0, 1)
        font = pygame.font.SysFont("comicsansms", 65)
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self._screen, BLACK, (0, 0, self.width, self.square_size))
                    position_x = event.pos[0]
                    if turn == HUMAN_MOVE:
                        pygame.draw.circle(self._screen, RED, (position_x, int(self.square_size / 2)), self.radius)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self._screen, BLACK, (0, 0, self.width, self.square_size))
                    if turn == HUMAN_MOVE:
                        position_x = event.pos[0]
                        column = int(math.floor(position_x / self.square_size))
                        self.__game.human_move(column)
                        if self.__game.winning_move(HUMAN_PIECE):
                            pygame.draw.rect(self._screen, BLACK, (0, 0, self.width, self.square_size))
                            label = font.render("HUMAN WINS!", True, RED)
                            self._screen.blit(label, (50, 10))
                            game_over = True
                        elif self.__game.game_draw():
                            pygame.draw.rect(self._screen, BLACK, (0, 0, self.width, self.square_size))
                            label = font.render("DRAW!", True, BLUE)
                            self._screen.blit(label, (50, 10))
                            game_over = True
                        self.draw_board()
                        pygame.display.update()
                        turn += 1
                        turn = turn % 2

            if turn == AI and not game_over:
                self.__game.computer_move()
                if self.__game.winning_move(AI_PIECE):
                    pygame.draw.rect(self._screen, BLACK, (0, 0, self.width, self.square_size))
                    label = font.render("COMPUTER WINS!", True, WHITE)
                    self._screen.blit(label, (50, 10))
                    game_over = True
                elif self.__game.game_draw():
                    pygame.draw.rect(self._screen, BLACK, (0, 0, self.width, self.square_size))
                    label = font.render("DRAW!", True, BLUE)
                    self._screen.blit(label, (50, 10))
                    game_over = True
                self.draw_board()
                pygame.display.update()
                turn += 1
                turn = turn % 2

        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()
