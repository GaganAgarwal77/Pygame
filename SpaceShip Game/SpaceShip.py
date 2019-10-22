import pygame
import time
import random
pygame.init()

display_width = 700
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0,0,255)


#fonts
largeText = pygame.font.Font('coolFont.ttf',90)
smallText = pygame.font.Font("buttonFont.ttf",20)
mediumText1 = pygame.font.Font('text.ttf',34)
mediumText2 = pygame.font.Font('Font2.ttf',25)
ship_width = 97
ship_height = 97

asteroid_width = 87
asteroid_height = 87

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Legends of Space')
clock = pygame.time.Clock()
screen= pygame.display.set_mode((display_width,display_height))
shipImg = pygame.image.load('spaceship2.png')
asteroidImg =pygame.image.load('asteroid.png')
extraImg = pygame.image.load('extra.png')
backgroundImg = pygame.image.load('spacer.png').convert()
menuImg = pygame.image.load('space2.png').convert()
def ship(x,y):
    gameDisplay.blit(shipImg,(x,y))


def asteroid(asteroid_x,asteroid_y):
        gameDisplay.blit(asteroidImg,(asteroid_x,asteroid_y))


def crash(dodge):
    message_display(f"You Crashed! Your Score : {dodge}",red)
    game_intro()


def text_objects(text,font,colour):
    textSurface= font.render(text,True,colour)
    return textSurface, textSurface.get_rect()


def message_display(text,color):
    TextSurf, TextRect = text_objects(text,mediumText1,color)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect),
    pygame.display.update()
    time.sleep(2)    


def asteroids_dodged(count):
    font = mediumText2
    text = font.render("Asteroids Dodged >> " +str(count),True,green)
    gameDisplay.blit(text,((500,0)))

def quit_game():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        
        if click[0] == 1 and action !=None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    
    textSurf,textRect  = text_objects(msg,smallText,white)
    textRect.center = ((x +(w/2)),(y +(h/2)))
    gameDisplay.blit(textSurf,textRect)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        screen.blit(menuImg,[0,0])
        TextSurf, TextRect = text_objects("Welcome to Space!",largeText,white)
        TextRect.center = (350,100)
        gameDisplay.blit(TextSurf, TextRect)
        button("Play!",100,550,125,50,green,bright_green,game_loop)
        button("Quit",500,550,125,50,red,bright_red,quit_game)
        gameDisplay.blit(extraImg,(500,150))
        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.6)
    i = 0
    x_change = 0
    y_change = 0
    score = 0
    asteroid_count = 1
    asteroid_startx=random.randrange(x-10,x+ship_width+10)
    asteroid_starty = -500
    asteroid_speed = 7
    gameExit = False
    j = 0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change
        screen.blit(backgroundImg,[0,0]) 
        asteroid(asteroid_startx,asteroid_starty)
        ship(x,y)
        asteroid_starty +=asteroid_speed
        asteroids_dodged(score)
        if x > display_width - ship_width or x < 0:
            crash(score)
        if y > display_height -ship_height or y <0:
            crash(score)
        if asteroid_starty > display_height:
            asteroid_starty = 0 - asteroid_height
            asteroid_startx = random.randrange(x-10,x+ship_width+10)
            score +=1
            if score >1 and score%5 == 1:
                i = int(score/5)+1
                message_display(f"Level {i}!",bright_green)
                asteroid_speed += 1
                x_change +=1
                y_change +=1
        if y + ship_height > asteroid_starty and y <asteroid_starty+asteroid_height:
            if x > asteroid_startx and x <asteroid_startx + asteroid_width or x + ship_width > asteroid_startx and x +ship_width < asteroid_startx + asteroid_width:
                crash(score)
        pygame.display.update()
        clock.tick(60)
game_intro( )
game_loop()
quit_game()
