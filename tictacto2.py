from time import sleep
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

        self.tiles_ID = {'z1':(0,0),'z2':(1,0),'z3':(2,0),'z4':(0,1),'z5':(1,1),'z6':(1,2),
                         'z7':(0,3),'z8':(1,3),'z9':(2,3)}
        self.tiles_Cent = {'z1':(50,50),'z2':(150,50),'z3':(250,50),'z4':(50,150),'z5':(150,150),'z6':(250,150),
                           'z7':(50,250),'z8':(150,250),'z9':(250,250)}
        self.squares = squares
        self.size = size
        
        #self.mx = mx

    
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

    def click(self):
        """mouse button action. Pinpointing tile ID with a dictionary callout"""
        colw = 100
        rowh = 100
        mx, my = pygame.mouse.get_pos()
        mouse_list=[]
        mloc = (mx, my)
        rowm = my // colw
        colm = mx // rowh
        
    def letters(self):
        """Defition for the X, placement"""
        textcolor = (255, 0, 0)
        font = pygame.font.Font(None, 50)
        text = font.render('X', True, textcolor)
        """Correlating the Key values to place text in the center of the square"""
        xdict = self.tiles_Cent.get('z1')
        #ydict = self.tiles_Cent.keys('z1')
        textRect = text.get_rect()
        #textRect.center = (xdict)
        self.screen.blit(text, xdict)
        pygame.display.flip()

    def run_game(self):
        """Loop for running the game"""
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                """Determine mouse click until moved into its own code to be called in"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    """creating the x,y position of mouse to be used in floor division""" 
                    if event.button == 1:
                        self.click()
                    if event.button == 1:
                        self.letters()
                    
                """Quiting Pygame"""
                if event.type == pygame.QUIT:
                    exit()
            clock.tick(60)
            
            #self.screen.blit(text, xdict)
            #storage = self.render_board()
            self.screen.fill(self.bg_color)
            storage = self.render_board()
            pygame.display.flip()
           
            

    #def _update_sreen(self):
        """Update the Screen"""
        
        self.screen.fill(self.bg_color)
        #storage = self.render_board()
        pygame.display.flip()

if __name__ == '__main__':
    ai: tictactoe = None
    ai = tictactoe(size=(100,100),squares=(3,3))
    ai.run_game()