import pygame
import time
import random
pygame.init()

display_width = 700
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

ship_width = 85
ship_height = 110

asteroid_width = 87
asteroid_height = 87

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Legends of Space')
clock = pygame.time.Clock()
screen= pygame.display.set_mode((display_width,display_height))
shipImg = pygame.image.load('rocket2.png')
asteroidImg =pygame.image.load('asteroid.png')
backgroundImg = pygame.image.load('spacer.png').convert()

def ship(x,y):
    gameDisplay.blit(shipImg,(x,y))


def asteroid(asteroid_x,asteroid_y):
        gameDisplay.blit(asteroidImg,(asteroid_x,asteroid_y))


def crash(dodge):
    message_display(f'''You Crashed! Your Score : {dodge}''')


def text_objects(text,font):
    textSurface= font.render(text,True,red)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def asteroids_dodged(count):
    font = pygame.font.Font('freesansbold.ttf',15)
    text = font.render("Asteroids Dodged >> " +str(count),True,green)
    gameDisplay.blit(text,((400,0)))


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
            if score%5 == 0:
                asteroid_speed += 1
                x_change +=1
                y_change +=1
        if y + ship_height > asteroid_starty and y <asteroid_starty+asteroid_height:
            if x > asteroid_startx and x <asteroid_startx + asteroid_width or x + ship_width > asteroid_startx and x +ship_width < asteroid_startx + asteroid_width:
                crash(score)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
