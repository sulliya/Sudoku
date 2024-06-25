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

        self.tiles_ID = {'z1':(0,0),'z2':(1,0),'z3':(2,0),'z4':(0,1),'z5':(1,1),'z6':(2,2),
                         'z7':(0,3),'z8':(1,3),'z9':(2,3),'z10':(3,3)}
        self.squares = squares
        self.size = size
        self.clicking = False
        
    
    def render_board(self):
        storage =[]
        x = int((300 - (self.size[0] * self.squares [0]))/2)
        y = int((300 - (self.size[1] * self.squares[1]))/2)

        for a in range(self.squares[0]):
            for b in range(self.squares[1]):
                i0 =(x + (a * self.size[0]))
                i1= (y + (b * self.size[1]))
                
                pygame.draw.rect(self.screen, (0,0,0), (i0, i1, self.size[0], self.size[1]), 1)
                storage.append((i0, i1, self.size[0], self.size[0]))

        return storage

    def clicking(self):
        """mouse button action. Pinpointing tile ID with a dictionary callout"""
        while self.clicking = True:
            colw = 100
            rowh = 100
            mx, my = pygame.mouse.get_pos()
            
            mloc = [mx, my]
            rowm = my // colw
            colm = mx // rowh

            print(rowm)


    def run_game(self):
        """Loop for running the game"""
        while True:
            for event in pygame.event.get():
                """Determine mouse click until moved into its own code to be called in"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    """creating the x,y position of mouse to be used in floor division""" 
                    if event.button == 1:
                        self.clicking = True
                        mx, my = pygame.mouse.get_pos()
                        #print(mx, my)
                """Quiting Pygame"""
                if event.type == pygame.QUIT:
                    exit()
                    
            self.screen.fill(self.bg_color)

            storage = self.render_board()

            pygame.display.flip()

if __name__ == '__main__':
    ai: tictactoe = None
    ai = tictactoe(size=(100,100),squares=(3,3))
    ai.run_game()