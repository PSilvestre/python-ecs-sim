import sys

import pygame

from Game import Game


def main():
    #icon = pygame.image.load("icon.png")
    #pygame.display.set_icon(icon)
    game = Game(20)
    game.game_loop()


if __name__ == '__main__': main()
