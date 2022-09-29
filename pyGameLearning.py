import math
import pygame
WIDTH = 900
HIGHt = 900
pygame.init()
screen = pygame.display.set_mode((WIDTH,HIGHt))
white = (100,100,100)
flag = True
current_x =0
current_y = 0
block_size = 20 
def grid():
    global x_coords
    x_coords = [1 for i in range(math.ceil(WIDTH/block_size)+block_size)]
    global y_coords
    y_coords = [1 for i in range(math.ceil(HIGHt/block_size)+block_size)]
    for x in range(0, WIDTH, block_size):
        for y in range(0, WIDTH, block_size):
            rect = pygame.Rect(x, y, block_size,block_size)
            pygame.draw.rect(screen,white,rect,1)
    #create lsit of all rect x and y coordinates
    for i in range(math.ceil(WIDTH/20)):
        x_coords[i] = i * block_size
    for i in range(math.ceil(HIGHt/20)):
        y_coords[i] = i* block_size

def snake(x,y):
    blockSize = 20
    snake = pygame.Rect(x_coords[current_x],y_coords[current_y], blockSize, blockSize)
    pygame.draw.rect(screen, (0,255,0),snake,1)
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                current_y +=1
            elif event.key == pygame.K_UP:
                current_y -= 1
            if event.key == pygame.K_RIGHT:
                current_x +=1
            elif event.key == pygame.K_LEFT:
                current_x -= 1
            snake(current_x, current_y)
        grid()
        snake(current_x, current_y)
    #screen.fill(white)
    pygame.display.update()
    

