import math
import pygame
import random
blockSize = 20
l_direction = 0
r_direction = 0
u_direction = 0 
d_direction = 0
pX = 0
pY = 0
score = 0
pScore =0
WIDTH = 900
HIGHt = 900
pygame.init()
screen = pygame.display.set_mode((WIDTH,HIGHt))
black = (0,0,0)
flag = True
current_x =5
current_y = 5
block_size = 20
snakeTail = [] 
snakeTail.append([current_x, current_y])
def grid():
    global x_coords
    x_coords = [1 for i in range(math.ceil(WIDTH/block_size)+block_size)]
    global y_coords
    y_coords = [1 for i in range(math.ceil(HIGHt/block_size)+block_size)]
    for x in range(0, WIDTH, block_size):
        for y in range(0, WIDTH, block_size):
            rect = pygame.Rect(x, y, block_size,block_size)
            #pygame.draw.rect(screen,white,rect,1)
    #create lsit of all rect x and y coordinates
    for i in range(math.ceil(WIDTH/20)):
        x_coords[i] = i * block_size
    for i in range(math.ceil(HIGHt/20)):
        y_coords[i] = i* block_size
def snake(x,y):
    snakeTailTransition = snakeTail
    snake = pygame.Rect(x_coords[current_x],y_coords[current_y], blockSize, blockSize)
    
    if score == pScore +1:
        for i in range(score+1):
            pygame.draw.rect(screen, (0,255,0),snake,1)
        print(snakeTail)
    for i in range(len(snakeTail)-1):
        snakeTail[i] = snakeTailTransition[i+1]
    snakeTail[0] = [[current_x, current_y]]
    snakeTail.append([pX, pY])
    pygame.draw.rect(screen, (0,255,0),snake,1)
def make_apple_position():
    appleX = random.randrange(0, math.floor(WIDTH/block_size)-1)
    appleY = random.randrange(0, math.floor(HIGHt/block_size)-1)
    return appleX, appleY
def apple(list):
    apple = pygame.Rect(x_coords[list[0]],y_coords[list[1]], blockSize, blockSize)
    pygame.draw.rect(screen, (250,0,0),apple,1)
clock = pygame.time.Clock()
grid()
apple_position = make_apple_position()
while flag:
    clock.tick(30)
    screen.fill(black)
    grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                l_direction,r_direction, u_direction = 0, 0,0
                d_direction = 1
            elif event.key == pygame.K_UP:
                l_direction,r_direction, d_direction = 0,0,0
                u_direction = 1
            elif event.key == pygame.K_RIGHT:
                l_direction,d_direction, u_direction = 0,0,0
                r_direction = 1
            elif event.key == pygame.K_LEFT:
                d_direction,r_direction, u_direction = 0,0,0
                l_direction = 1
    snake(current_x, current_y)
    apple(apple_position)
    if current_x == apple_position[0] and current_y == apple_position[1]:
        apple_position = make_apple_position()
        score += 1
    if r_direction == 1 and current_x < WIDTH:
        pX = current_x
        pY = current_y
        current_x += 1
    if l_direction == 1 and current_x > 0:
        pX = current_x
        pY = current_y
        current_x -= 1
    if u_direction == 1 and current_y >0:
        pY = current_y
        pX = current_x
        current_y -= 1
    if d_direction == 1 and current_y < HIGHt:
        pY = current_y
        pX = current_x
        current_y += 1
    pygame.time.delay(50)    
    #screen.fill(white)
    pygame.display.update()
    
    

