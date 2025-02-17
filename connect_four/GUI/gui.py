from connect_four.GUI.WinnerDisplay import WinnerDisplay
from connect_four.domain.board import Board, COLUMNS
from connect_four.domain.computer import Computer
from connect_four.domain.player import Player
import pygame
import sys

HUMAN = 0
PLAYER1 = 0
HUMAN_VS_COMPUTER = 1

class Ui():
    def __init__(self, human_player : Player, board : Board, second_player : Player = None, computer_player  : Computer = None):
        self.__human_player = human_player
        self.__computer_player = computer_player
        self.__board = board
        self.__second_player = second_player

        pygame.init()
        self.SQUARESIZE = 100
        self.RADIUS = self.SQUARESIZE // 2 - 5
        self.WIDTH = 7 * self.SQUARESIZE
        self.HEIGHT = 7 * self.SQUARESIZE  # Extra row for dropping pieces
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Connect Four")

    def draw_board(self):
        self.screen.fill((0, 0, 0))  # Black background

        for row in range(6):
            for col in range(7):
                pygame.draw.rect(self.screen, (0, 0, 255),
                                 (col * self.SQUARESIZE, (row + 1) * self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE))

                piece = self.__board.get_piece(row, col)

                if piece is None:
                    color = (50, 50, 50)
                elif piece == 'X':
                    color = (200, 0, 0)
                elif piece == 'O':
                    color = (255, 215, 0)
                else:
                    color = (255, 255, 255)

                pygame.draw.circle(self.screen, color,
                                   (col * self.SQUARESIZE + self.SQUARESIZE // 2,
                                    (row + 1) * self.SQUARESIZE + self.SQUARESIZE // 2), self.RADIUS)

        pygame.display.update()



    def display_board(self):
        print(self.__board)

    def check_column(self, column):
        if not isinstance(column, int):
            raise TypeError('Column must be an integer')

        if column < 0 or column > COLUMNS:
            raise ValueError("Invalid column number")

        return True

    def option_menu(self):
        self.print_menu()
        option = int(input("Enter your choice: "))
        if option == HUMAN_VS_COMPUTER:
            self.start_game_human_computer()
        else:
            self.start_game_human_human()

    def start_game_human_computer(self):
        pygame.init()
        playing = True

        while playing:
            self.__board = Board()
            self.draw_board()
            won = False
            move = 0

            while not won and self.__board.still_play():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN and move % 2 == HUMAN:
                        x = event.pos[0]
                        column = x // self.SQUARESIZE

                        try:
                            self.__board.move(column, self.__human_player.symbol)
                            self.draw_board()

                            if self.__board.game_won():
                                winner_display = WinnerDisplay(self.WIDTH, self.HEIGHT)
                                playing = winner_display.display_winner(self.screen, self.__human_player.name)
                                won = True
                                if not playing:
                                    pygame.quit()
                                    sys.exit()
                                break

                            move += 1
                        except ValueError as ve:
                            print(ve)

                if not won and move % 2 == 1:
                    pygame.time.wait(500)
                    column = self.__computer_player.make_move(self.__board)
                    self.__board.move(column, self.__computer_player.symbol)
                    self.draw_board()

                    if self.__board.game_won():
                        winner_display = WinnerDisplay(self.WIDTH, self.HEIGHT)
                        playing = winner_display.display_winner(self.screen, "AI Player")
                        won = True
                        if not playing:
                            pygame.quit()
                            sys.exit()
                        continue

                    move += 1

            if not won and self.__board.still_play() == False:
                winner_display = WinnerDisplay(self.WIDTH, self.HEIGHT)
                playing = winner_display.display_winner(self.screen, "No one")
                if not playing:
                    pygame.quit()
                    sys.exit()

    def start_game_human_human(self):
        pygame.init()
        playing = True

        while playing:
            self.__board = Board()
            self.draw_board()
            won = False
            move = 0

            while not won and self.__board.still_play():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x = event.pos[0]
                        column = x // self.SQUARESIZE

                        try:
                            current_player = self.__human_player if move % 2 == 0 else self.__second_player
                            self.__board.move(column, current_player.symbol)
                            self.draw_board()

                            if self.__board.game_won():
                                winner_display = WinnerDisplay(self.WIDTH, self.HEIGHT)
                                playing = winner_display.display_winner(self.screen, current_player.name)
                                won = True
                                if not playing:
                                    pygame.quit()
                                    sys.exit()
                                break

                            move += 1
                        except ValueError as ve:
                            print(ve)

            if not won and self.__board.still_play() == False:
                winner_display = WinnerDisplay(self.WIDTH, self.HEIGHT)
                playing = winner_display.display_winner(self.screen, "No one")
                if not playing:
                    pygame.quit()
                    sys.exit()