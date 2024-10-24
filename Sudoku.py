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
        self.screen = pygame.display.set_mode((900,700))#surface for interfacing
        self.bg_color = (255,255,255)
        pygame.display.set_caption("Sudoku")
        self.squares = squares
        self.size = size
        self.colm: int = ()
        self.rowm: int = ()
        self.corvar: List = ()
        self.rows:int = 9
        self.cols: int = 9
        self.rectcent = ()
        self.rect_ID = {}
        self.grid: int = 9
        self.board_background:List[str] = [[""]*self.grid for i in range(self.grid)]
        #test code
        self.testboard:List[str] = [['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],
                                    ['1','2','3','4','5','6','7','8','9']]
        self.color = pygame.Color('firebrick')
        #temp note: input_rect is working not on location of click but hard code, having a scope issue
        self.input_rect = pygame.Rect(0,0,50,25)
        self.user_text =''
        self.gridcentvaluex:int = () #equals the value center ID based off clicking a square
        self.gridcentervaluey:int = ()
        self.flag1 = False

    def render_board(self): #Note: This code is fine and doesn't need editing
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
        
        #Creating second storage 
        storage2 = []
        squares2 = (3,3)
        size2 = (233,233)

        x = int((700 - (size2[0] * squares2 [0]))/2)
        y = int((700 - (size2[1] * squares2[1]))/2)

        for a in range(squares2[0]):
            for b in range(squares2[1]):
                i0 =(x + (a * size2[0]))
                i1= (y + (b * size2[1]))

                pygame.draw.rect(self.screen, (0,0,0), (i0, i1, size2[0], size2[1]), 5)
                storage.append((i0, i1, size2[0], size2[0]))

        return storage,storage2
    
    def ID_cord(self): #Works
        """Create ID's for all cells"""
        colw = 77
        rowh = 77
        mx, my = pygame.mouse.get_pos()
        self.rowm = my // colw
        self.colm = mx // rowh
        self.corvar = (self.colm,self.rowm)
        print(self.corvar)
        

    def list_loop(self):
        if self.flag1 == False:
            pass
        '''Creating a single list for center points, b/c the grid is a square, x&y values incriments uniformly'''
        grid_center:list[int] =[]
        '''creating overall list up to boundry of grid by half of each square size'''
        for i in range(0,700,38):
            grid_center.append(i)
        '''Slicing the overall list by incriments of 2 get only the centers.'''
        grid_center= grid_center[1:18:2]
        #print(grid_center[self.colm],grid_center[self.rowm])
        self.gridcentvalue = (grid_center[self.colm],grid_center[self.rowm])
        self.gridcentvaluex = grid_center[self.rowm]
        self.gridcentervaluey = grid_center[self.colm]
      
        
        
    def user_input(self): #break into another function for rendering only
        '''checking if user input is a single integer'''
        for i in self.user_text:
            '''Boleon test on int value type and length, if true modify list'''
            numbertype = False
            numbercount = False
            if int(i) == int:
                numbertype = True
            if len(self.user_text) == 1:
                numbercount = True
            if numbertype == True:
                numbercount == True
                '''Taking typed in string value and placing it into the open 2d array holding all values'''
                j = int(i)
                self.board_background[self.colm][self.rowm] = j
            else:
                print("please enter a single number")
        self.board_background[self.colm][self.rowm] = self.user_text
        print(self.board_background[self.colm][self.rowm])# replacing works. but not re-rendering
        
    def render(self):#ask, why .render changes to white when changed name on all occurances?
        '''Generating input onto the screen.'''
        '''Creating text color, font'''
        textcolor = (255, 0, 0)
        base_font = pygame.font.Font(None,35)  
        text_typed = base_font.render(self.user_text,True,textcolor)
        self.text_box = pygame.Rect(50,50,77,77)
        self.input_rect = pygame.Rect((50,50),(50,25))
        #white box overrights background zone with white space prior writing new number into background.
        whitebox = pygame.Surface((25,25))
        whitebox.fill((255,255,255))
        self.screen.blit(whitebox,self.gridcentvalue)
        self.screen.blit(text_typed,self.gridcentvalue)
        

    def win_logic(self):
        '''code when button selecting submit is hit'''
        #to be created
        '''Winning logic for the game'''
        checklist1: List[str] = ['1','2','3','4','5','6','7','8','9']
        checklist2: List[int] = [[1,2,3],[4,5,6],[7,8,9]]
        userlist: List[int] = []
        
        for i in self.board_background:
            '''checking that each layer has numbers 1-9 and no duplicates in the x & y'''
            if self.board_background[set(i) == checklist1][set(i) == checklist1]:
                check1 = True
            '''Break lists of 9 into 3, then check to see if they conatain numbers 1-9'''
            '''Slicing the 2D 9x9 array into 3's to then stack and check'''
            '''converting string to int'''
            listconv = []
            cs = [int(y) for x in self.board_background for y in x]
            listconv = [cs[j:j + 3] for j in range(0,9,3)]


    def run_game(self):
        """Loop for running the game"""
        clock = pygame.time.Clock()
        self.screen.fill(self.bg_color)
        self.render_board()
        while True:
            #flag1 to initialize modules based on input after screen is rendered.
            self.flag1 = False
            for event in pygame.event.get():
                """Determine mouse click until moved into its own code to be called in"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.flag1 = True
                        self.ID_cord()
                        self.user_input()
                        self.list_loop()
                        self.render()
                        #self.win_logic()
            #note: this works when in the click loop but doesn't show like I want.
            #Also if typing and clicking again, it overwrites. Need module that has below code initated on click.
                if event.type == pygame.KEYDOWN:
                    self.user_text = ''
                    """Adding user text"""
                    if event.key == pygame.K_BACKSPACE:
                            self.user_text = self.user_text[:-1]
                    else:   
                        self.user_text += event.unicode
                        #only takes first number, only works for number input
                        self.user_text = self.user_text[0]
                   
                '''trying to draw the input rectangle on the screen'''
                #pygame.draw.rect(self.screen,self.color,self.input_rect,2)
             
            if self.flag1 == True:
                self.render()

            """Quiting Pygame"""
            if event.type == pygame.QUIT:
                exit()
            clock.tick(60)
    
            pygame.display.flip()
        
if __name__ == '__main__':
    ai: Sudoku = None
    ai = Sudoku(size=(77,77),squares=(9,9))
    ai.run_game()