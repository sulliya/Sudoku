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
        self.colm:[int] = ()
        self.rowm:[int] = ()
        self.corvar:[list] = ()
        self.rows:[int] = 9
        self.cols:[int] = 9
        self.rectcent = ()
        self.rect_ID = {}
        self.grid:[int] = 9
        self.board_background:[str] = [[""]*self.grid for i in range(self.grid)]
        


    def render_board(self):
        '''creating the grid space moving in x & y direction'''
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
        """Create ID's for all cells"""
        colw = 77
        rowh = 77
        mx, my = pygame.mouse.get_pos()
        self.rowm = my // colw
        self.colm = mx // rowh
        self.corvar = (self.colm,self.rowm)
        print(self.corvar)
        print(mx,my)


        '''testing grid center with coordinate location'''
        grid_center:[int] =[]
        for i in range(0,700,38):
            grid_center.append(i)
        grid_center= grid_center[1:18:2]
        print(grid_center[self.colm],grid_center[self.rowm])

        '''testing code'''
        userlist = []
        userlist = self.board_background[j:j + 3] for j in range(0,9,3)
      
    def list_loop(self):
        '''Creating a single list for center points, b/c the grid is a square, x&y values incriments uniformly'''
        grid_center:[int] =[]
        for i in range(0,700,38):
            grid_center.append(i)
        grid_centers= grid_center[1:18:2]
        print(grid_centers)
        
        
    def user_input(self):
        '''Taking typed in string value and placing it into the open 2d array holding all values'''
        textcolor = (255, 0, 0)
        font = pygame.font.Font(None, 50)
        self.text_box = pygame.Rect(50,50,77,77)
        user_ip =''
        '''code to store coordinates in the empty 2d array'''
        self.board_background[self.rowm][self.colm] = user_ip


    def win_logic(self):
        '''code when button selecting submit is hit'''
        #to be created
        '''Winning logic for the game'''
        checklist1:[list] = ['1','2','3','4','5','6','7','8','9']
        checklist2:[list] = [['1','2','3'],['4','5','6'],['7','8','9']]
        userlist:[list] = []
        for i in self.board_background:
            '''checking that each layer has numbers 1-9 and no duplicates in the x & y'''
            if self.board_background[set(i) == checklist1][set(i) == checklist1]:
                check1 = True
            '''check 3x3 arrays have numbers 1-9 and no duplicates'''
            '''Slicing the 2D 9x9 array into 3's to then stack and check'''
            userlist = self.board_background[j:j + 3] for j in range(0,9,3)


            
        

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
                        self.ID_cord()
                        self.user_input()
                        #self.list_loop()
                        #self.win_logic()
                    if self.text_box.collidepoint(event.pos):
                        active: True
                    else:
                        active = False
                if event.type == pygame.KEYDOWN:
                    """Creating text block input"""
                    if active:
                        if event.key == pygame.K_BACKSPACE:
                            user_ip = user_ip[:-1]
                        else:
                            user_ip += event.unicode



                """Quiting Pygame"""
                if event.type == pygame.QUIT:
                    exit()
            clock.tick(60)
    
            pygame.display.flip()
        
if __name__ == '__main__':
    ai: Sudoku = None
    ai = Sudoku(size=(77,77),squares=(9,9))
    ai.run_game()