import pygame
import random
pygame.init()
#Colours
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

screen_width=1200;
screen_height=600;
#Creating Window
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game by Ashzad")
pygame.display.update()

#Creating Game Variables
exit_game=False
game_over=False
snake_x=45
snake_y=55
snake_size=10
snake_size_x=10
snake_size_y=10
velocity_x=0
velocity_y=0
food_x=random.randint(0,screen_width)
food_y=random.randint(0,screen_height)
score=0
fps=30
clock=pygame.time.Clock()
#Event Handling
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        #Code for right movement of snake
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x+=10
                velocity_y = 0
        # Code for left movement of snake
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity_x-=10
                velocity_y = 0
        # Code for down movement of snake
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                velocity_y+=10
                velocity_x= 0
        # Code for up movement of snake
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocity_y-=10
                velocity_x= 0

    snake_x+=velocity_x
    snake_y+=velocity_y
    if(abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6):
        score+=1
        snake_size_x += 10
        snake_size_y += 10
        food_x = random.randint(0, screen_width)
        food_y = random.randint(0, screen_height)

    gameWindow.fill(white)
    #Snake head creation
    pygame.draw.rect(gameWindow , black , [snake_x,snake_y,snake_size_x,snake_size_y] )
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()
