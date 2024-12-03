from time import sleep
import pygame
import sys
import sprite
from typing import List
import random
from random import randint



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
        self.rowm: int = ()
        self.colm: int = ()
        self.corvar: List = ()
        self.rows:int = 9
        self.cols: int = 9
        self.rectcent = ()
        self.rect_ID = {}
        self.grid: int = 9
        self.board_background:List[str] = [[""]*self.grid for i in range(self.grid)]
        #self.permlist:List[str] = {}#creates issue in diff module
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
    
    
    def difficult(self):# module to create random numbers throughout. ideally quantity is selectable by user.
        takenlist = ["1","2","3","4","5","6","7"] #random numbers put into the grid
        self.templist = {}
        temp = []
        self.permlist = dict()
        ylist =[randint(0,8) for i in range(0,7)]#random y locations
        xlist = [randint(0,8) for i in range(0,7)]#random x locations  

        for i,j in zip(xlist,ylist): #incriment x,y direction simultanously
                k = random.choice(takenlist)
                takenlist.remove(k)
                self.board_background[i][j] = k #may be pointless
                self.templist.update({k : (i,j)})
                for n,m in self.templist.items():
                    if m not in temp:
                        temp.append(m)
                        self.permlist[n] = m

        #print(self.permlist)      
        #print(self.board_background)
    def ID_cord(self): #Works
        """Create ID's for all cells"""
        colw = 77
        rowh = 77
        mx, my = pygame.mouse.get_pos()
        self.colm = my // rowh
        self.rowm = mx // colw
        self.corvar = (self.colm,self.rowm)
        print(self.corvar)
        print(mx,my)
        
        

    def list_loop(self):
        if self.flag1 == False:
            pass
        '''Creating a single list for center points, b/c the grid is a square, x&y values incriments uniformly'''
        self.grid_center:List[int] =[]
        '''creating overall list up to boundry of grid by half of each square size'''
        if self.rowm > 8:
            return
        for i in range(0,700,38):
            self.grid_center.append(i)
        '''Slicing the overall list by incriments of 2 get only the centers.'''
        self.grid_center= self.grid_center[1:18:2]
        #print(self.grid_center[self.rowm],self.grid_center[self.colm])
        self.gridcentvalue = (self.grid_center[self.rowm],self.grid_center[self.colm])
        self.gridcentvaluex = self.grid_center[self.colm]
        self.gridcentervaluey = self.grid_center[self.rowm]
        #self.permgridcentvalue = (self.grid_center[],self.grid_center[])
        #premade selected grid locations
        self.pkeys = list(self.permlist.keys())
        self.pvalue = list(self.permlist.values())
        
        
        
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
                #j = int(i)
                #self.board_background[self.colm][self.rowm] = j
            #else:
                #print("please enter a single number")
        #for i in (self.colm,self.rowm):
            #if i in self.permlist.values():
                #break
            #else:
                #self.board_background[self.colm][self.rowm] = self.user_text
    
        
    def render(self):
        if self.rowm > 8:
            return
        #Creating submit button to check if game is complete

        
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
        
               
        
        
        cord = (self.colm,self.rowm)
        for i,j in self.permlist.items():
            if j == cord:
                return
               
        self.board_background[self.colm][self.rowm] = self.user_text#Stores the value in its proper place
        #Below is original def render()
        #'''Generating input onto the screen.'''
        #'''Creating text color, font'''
        textcolor = (255, 0, 0)
        base_font = pygame.font.Font(None,35)  
        text_typed = base_font.render(self.user_text,True,textcolor)
        self.text_box = pygame.Rect(50,50,77,77)#not needed
        self.input_rect = pygame.Rect((50,50),(50,25))#not needed
        #white box overrights background zone with white space prior writing new number into background.
        whitebox = pygame.Surface((25,25))
        whitebox.fill((255,255,255))
        self.screen.blit(whitebox,self.gridcentvalue)
        self.screen.blit(text_typed,self.gridcentvalue)
        #printing the premade pieces by looping through the list.
        l = 0
        for i,j in self.pvalue:
            k = self.pkeys[l]
            l = l + 1 
            self.screen.blit(whitebox,(self.grid_center[j],self.grid_center[i]))
            permlistkey = base_font.render(k,True,textcolor)
            self.screen.blit(permlistkey,(self.grid_center[j],self.grid_center[i]))
        
        #print(self.board_background)
        return

    def Button(self):
        #event button that triggers win_logic by user.
        rect = pygame.rect.Rect(750, 0, 77, 77)
        text = "check"
        textcolor = (0,0,0)
        boxcolor = (128,128,128)
        font = pygame.font.Font(None,30)
        buttonrender = font.render(text, True, textcolor)
        pygame.draw.rect(self.screen, boxcolor,rect,0,5)
        pygame.draw.rect(self.screen,textcolor,rect,5,0)
        self.screen.blit(buttonrender,(750+10,10+15))
        if self.rowm == 9 or 10:
            if self.colm == 0:
                self.win_logic()

    def win_logic(self):
        ytest = False
        xtest = False
        #taking y column of final user list and turning it into it's own 2D array.
        t = 0
        ylist = []
        twoDylist = []
        for i in range(0,9,1): #ranging 0-9 exclusive
            for row in self.board_background:
                x = row[t] #iteraties through entire 2D picking only y placement in row
                ylist.append[x]
            t = t + 1
        for w in range(0,len(ylist),9): #Have to break the 1D list of all Y's into 2D
            twoDylist.append(ylist[w:w + 9])
        #check for duplicates in Y 2D array.
        for o in twoDylist:
            ychecklist = []
            for p in o:
                if p not in ychecklist:
                    ychecklist.append(p)
            if len(ychecklist) != 8:
                ytest = False
                return print("Inputs incorrect")
        if len(ychecklist) == 8:
            ytest = True
        #Checking for duplicates in X direction only.
        #Don't need to break the 2d array as it is already set for x direction
        for v in self.board_background:
            xchecktest = []
            for n in v:
                if n not in xchecktest:
                    xchecktest.append(n)
            if len(xchecktest) != 8:
                return print("Inputs incorrect")
        if len(xchecktest) == 8:
            xtest = True
        if xtest and ytest == True:
            print("you've won")
            exit()


    def run_game(self):
        #"""Loop for running the game"""
        clock = pygame.time.Clock()
        self.screen.fill(self.bg_color)
        self.render_board()
        self.difficult()
        self.Button()
        while True:
            #flag1 to initialize modules based on input after screen is rendered.
            self.flag1 = False
            for event in pygame.event.get():
                #"""Determine mouse click until moved into its own code to be called in"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.flag1 = True
                        self.ID_cord()
                        #self.user_input()
                        self.list_loop()
                        self.render()
                        self.Button()
            #note: this works when in the click loop but doesn't show like I want.
            #Also if typing and clicking again, it overwrites. Need module that has below code initated on click.
                if event.type == pygame.KEYDOWN:
                    self.user_text = ''
                    #"""Adding user text"""
                    if event.key == pygame.K_BACKSPACE:
                            self.user_text = self.user_text[:-1]
                    else:   
                        self.user_text += event.unicode
                        #only takes first number, only works for number input
                        self.user_text = self.user_text[0]
                   
                #'''trying to draw the input rectangle on the screen'''
                #pygame.draw.rect(self.screen,self.color,self.input_rect,2)
             
            if self.flag1 == True:
                self.render()

            #"""Quiting Pygame"""
            if event.type == pygame.QUIT:
                exit()
            clock.tick(60)
    
            pygame.display.flip()
        
if __name__ == '__main__':
    ai: Sudoku = None
    ai = Sudoku(size=(77,77),squares=(9,9))
    ai.run_game()