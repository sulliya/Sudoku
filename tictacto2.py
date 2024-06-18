import pygame
import sys
import sprite
from typing import List

class tictactoe:
    """Background screen to be called into main  tic tak toe game"""

    def __init__(self, size: List[int], squares:List[int]):
        """handling the screen"""
        pygame.init()
        self.screen = pygame.display.set_mode((300,300))
        self.bg_color = (255,255,255)
        pygame.display.set_caption("TicTacToe")

        #tiles_ID = {z1:(0,0),z2:(1,0),z3:(2,0),z4:(0,1),z5:(1,1),z6:(2,2),z7:(0,3),z8:(1,3),z9:(2,3),z10:(3,3)}
        self.squares = squares
        self.size = size
        #self.storage = self.render_board(self.squares,self.size)

        #size =(300,300)
        #cell_width = 100
        #cell_height = 100
        #grid_surface = pygame.Surface(size)
        #grid = []
       # for x in range(300):
         #   grid.append([])
         #   for y in range(600):
        #        self.new_method(grid, x, y)
         #       pygame.draw.rect(grid_surface, (200,0,0), (x*cell_width, y*cell_height))

  #  def new_method(self, grid, x, y):
   #     grid[x][y] = "x"
    
    def render_board(self):
        storage =[]
        x = int((300 - (self.size[0] * self.squares [0]))/2)
        y = int((300 - (self.size[1] * self.squares[1]))/2)

        for a in range(self.squares[0]):
            for b in range(self.squares[1]):
                i0 =(x + (a * self.size[0]))
                i1= (y + (b * self.size[1]))
                storage.append((i0,i1))
        pygame.draw.rect(self.screen, (0,0,0), storage, 1)

        return storage

    def run_game(self):
        """Loop for running the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.screen.fill(self.bg_color)


            #pygame.draw.rect(screen, (20,100,0), 1)
            storage = self.render_board()

            pygame.display.flip()

if __name__ == '__main__':
    ai = tictactoe(size=(5,5),squares=(50,50))
    ai.run_game()