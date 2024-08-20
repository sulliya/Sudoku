from time import sleep
import pygame
import sys
import sprite
from typing import List
import random


class Sudoku:
    """Class to setup base variables and UI"""

    def __init__(self,size:List[int],squares:List[int]):
        """Setup base vairables for screen and other definitions"""
        pygame.init()
        self.screen = pygame.display.set_mode((900,700))
        self.bg_color = (255,255,255)
        pygame.display.set_caption("Sudoku")
        self.squares = squares
        self.size = size
        self.rectcent = ()
        self.rect_ID = {}

    def render_board(self):
        storage =[]
        x = int((700 - (self.size[0] * self.squares [0]))/2)
        y = int((700 - (self.size[1] * self.squares[1]))/2)

        for a in range(self.squares[0]):
            for b in range(self.squares[1]):
                i0 =(x + (a * self.size[0]))
                i1= (y + (b * self.size[1]))
                
                pygame.draw.rect(self.screen, (0,0,0), (i0, i1, self.size[0], self.size[1]), 1)
                storage.append((i0, i1, self.size[0], self.size[0]))

        return storage
    
    def ID_cord(self):
        """Create ID's for all cells in dictionary form"""
        colw = 77
        rowh = 77
        mx, my = pygame.mouse.get_pos()
        rowm = my // colw
        colm = mx // rowh
        corvar = (colm,rowm)
        print(corvar)
        #keys1 = ()
        for i in range(0,8):
            keys1 = (z for z in range(0 + 77, 0))
        print(keys1)
         
    
    def run_game(self):
        """Loop for running the game"""
        clock = pygame.time.Clock()
        self.screen.fill(self.bg_color)
        self.render_board()
        while True:
            for event in pygame.event.get():
                """Determine mouse click until moved into its own code to be called in"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    """creating the x,y position of mouse to be used in floor division""" 
                    if event.button == 1:
                        print(event.pos)
                        self.ID_cord()
                """Quiting Pygame"""
                if event.type == pygame.QUIT:
                    exit()
            clock.tick(60)
    
            pygame.display.flip()
        
if __name__ == '__main__':
    ai: Sudoku = None
    ai = Sudoku(size=(77,77),squares=(9,9))
    ai.run_game()