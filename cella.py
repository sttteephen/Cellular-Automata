import pygame
import sys
import os
from time import sleep
from math import floor

WIN_WIDTH = 1000
WIN_HEIGHT = 500
CELL_WIDTH = 1
CELL_HEIGHT = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ARRAY_SIZE = floor(WIN_WIDTH/CELL_WIDTH)

# calculate the state of cells in the next generation 
def new_genaration(array, ruleset):

    next_generation = [0] * ARRAY_SIZE

    # lope over the array
    for i in range(ARRAY_SIZE):
        if i > 0 and i < ARRAY_SIZE-1:

            # get current state of cells 
            left_cell = array[i-1]
            center_cell = array[i]
            right_cell = array[i+1]

            # use binary value of states as index into ruleset
            binary = str(left_cell) + str(center_cell) + str(right_cell)
            rule_index = int(binary, 2)
            next_generation[i] = ruleset[rule_index]
            
    return next_generation


# draw the next generation on a newline on screen
def draw_next_gen(array, genaration):
    y = genaration*CELL_HEIGHT  # y cordinate of next line
    for i in range(len(array)):
        if array[i] == 1:
                x = i*CELL_WIDTH    # x cordinate of current cell
                screen.fill(BLACK, rect=[x, y, CELL_WIDTH, CELL_HEIGHT])


# initialize array and set middle element to 1
array = [0] * ARRAY_SIZE
array[floor(ARRAY_SIZE/2)] = 1

# try 90, 182, 30, 165, 57, 45, 110, 73
ruleint = -1
while ruleint < 0 or ruleint > 255:
    ruleint = int(input('What rule would you like to generate? '))

rulebin = bin(ruleint)
rulestr = str(rulebin)[2:].zfill(8)[::-1]
ruleset = list(map(int, rulestr))
#print(ruleset)

pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Cellular Automata')
screen.fill(WHITE)

genaration = 0

#  main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # print new genarations until the end of the screen is reached
    if genaration < WIN_HEIGHT/CELL_HEIGHT:
        array = new_genaration(array, ruleset)
        draw_next_gen(array, genaration)
        genaration += 1

    pygame.display.update()
