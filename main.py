from board import Board
from game import Game
from gui import GUI
from player import Player
from strategy import Strategy
from ui import UI

with open("settings.properties", "r") as settings_file:
    for line in settings_file:
        line = line.split("=")
        if line[0].strip() == "ui":
            ui = line[1].strip()

board = Board(6, 7)
human_player = Player(1)
strategy = Strategy()
computer = Player(2)
game = Game(board, human_player, computer, strategy)

if ui == "ui":
    ui = UI(game)
else:
    ui = GUI(game)

ui.start()
