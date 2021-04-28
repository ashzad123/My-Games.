import pygame
import random
import os
pygame.mixer.init()

pygame.init()

#Colours
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

#Creating Window
screen_width=1200;
screen_height=600;
gameWindow=pygame.display.set_mode((screen_width,screen_height))

#Background Images
welimage= pygame.image.load("welcome.jpeg")
bgimage= pygame.image.load("back1.jpg")
welimage= pygame.transform.scale(welimage,(screen_width , screen_height)).convert_alpha()
bgimage= pygame.transform.scale(bgimage,(screen_width , screen_height)).convert_alpha()

#Game Title
pygame.display.set_caption("Snake Game by Ashzad")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


#Function to print score in the screen
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

#Funtion to create head of the snake along with its incrementation
def plot_head(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])
#Welcome Page
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(black)
        gameWindow.blit(welimage,(0,0))
        text_screen("Welcome to Snakes Game.",red,340,250)
        text_screen("Press Space to Start The Game.",red,300,320)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("mixkit-player-recharging-in-video-game-2041.wav")
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()
        clock.tick(30)

#Game Loop
def game_loop():
    # Creating Game Variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    score = 0
    fps = 60
    snk_list = []
    snk_length = 1
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt","r") as f:
        hiscore=f.read()
    #Event Handling


    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter to Continue", red, 250, 250)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                    #Code for right movement of snake
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x+=5
                        velocity_y = 0
                    # Code for left movement of snake
                    if event.type==pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            velocity_x-=5
                            velocity_y = 0
                    # Code for down movement of snake
                    if event.type==pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            velocity_y+=5
                            velocity_x= 0
                    # Code for up movement of snake
                    if event.type==pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            velocity_y-=5
                            velocity_x= 0

            snake_x+=velocity_x
            snake_y+=velocity_y
                #Calculating Score
            if(abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8):
                pygame.mixer.music.load("feed.mp3")
                pygame.mixer.music.play()
                score+=10
                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                snk_length+=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimage, (0 ,0))
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if(len(snk_list)>snk_length):
               del snk_list[0]
                #Printing Score
            text_screen("Score :"+str(score)+"  High-Score: "+str(hiscore),red,5,5)
                #Snake food creation
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            if head in snk_list[:-1]:
                game_over=True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load("mixkit-fairytale-game-over-1945.wav")
                pygame.mixer.music.play()
                game_over=True
                # Snake head creation
                # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_head(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
