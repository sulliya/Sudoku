import sys
import pygame 
import pyautogui as py
import time


window = pygame.display.set_mode((800,800))
pygame.display.set_caption("Test")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255,255,255))
    pos = pygame.mouse.get_pos()
    pygame.draw.line(window,(0,0,255),(266,0),(266,800),width=5)
    pygame.draw.line(window,(0,0,255),(533,0),(533,800),width=5)
    pygame.draw.line(window,(0,0,255),(0,266),(800,266),width=5)
    pygame.draw.line(window,(0,0,255),(0,533),(800,533),width=5)
    pygame.draw.circle(window,(255,0,0),(150,200),50)
    pygame.draw.circle(window,(255,255,255),(150,200),35)


    
    pygame.display.flip()
pygame.quit()