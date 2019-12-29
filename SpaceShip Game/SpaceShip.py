import pygame
import time
import random
pygame.init()

display_width = 700
display_height = 620

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0,0,255)
light_blue = (0,191,255)
grey = (200,200,200)


#fonts
largeText = pygame.font.Font('Fonts/coolFont.ttf',90)
smallText = pygame.font.Font("Fonts/buttonFont.ttf",20)
mediumText1 = pygame.font.Font('Fonts/text.ttf',34)
mediumText2 = pygame.font.Font('Fonts/Font2.ttf',25)
ship_width = 90
ship_height = 97
bullet_width = 20
bullet_height = 40
asteroid_width = 77
asteroid_height = 77

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Legends of Space')
clock = pygame.time.Clock()
pause = False
screen= pygame.display.set_mode((display_width,display_height))
shipImg = pygame.image.load('Images/spaceship2.png')
asteroidImg =pygame.image.load('Images/asteroid.png')
bulletImg = pygame.image.load('Images/bullet5.png')
extraImg = pygame.image.load('Images/extra.png')
backgroundImg = pygame.image.load('Images/spacer.png').convert()
menuImg = pygame.image.load('Images/space2.png').convert()
speaker3Img = pygame.image.load('Images/speaker3.png')
speaker0Img = pygame.image.load('Images/speaker0.png')
pygame.display.set_icon(shipImg)
music = pygame.mixer.music.load('Music/music1.wav')
pygame.mixer.music.play(-1)
music = True

def ship(x,y):
    gameDisplay.blit(shipImg,(x,y))


def asteroid(asteroid_x_list,asteroid_y):
        for asteroid_x in asteroid_x_list:
            gameDisplay.blit(asteroidImg,(asteroid_x,asteroid_y))


def crash(dodge):
    #message_display(f"You Crashed! Your Score : {dodge}",red)
    #game_intro()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game() 
        TextSurf, TextRect = text_objects(f"You Crashed! Your Score : {dodge}",mediumText1,red)
        TextRect.center = (350,50)
        gameDisplay.blit(TextSurf, TextRect)
        bullet_state = "Ready"
        button("Play Again",100,550,125,50,green,bright_green,game_loop)
        button("Quit",500,550,125,50,red,bright_red,quit_game)
        #asteroids_dodged(dodge)
        pygame.display.update()
        clock.tick(15)

def text_objects(text,font,colour):
    textSurface= font.render(text,True,colour)
    return textSurface, textSurface.get_rect()


def message_display(text,color):
    TextSurf, TextRect = text_objects(text,mediumText1,color)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect),
    pygame.display.update()
    time.sleep(0.5)    


def asteroids_dodged(count):
    font = mediumText2
    text = font.render("Asteroids Dodged  >> " +str(count),True,green)
    gameDisplay.blit(text,((500,0)))

def asteroids_destroyed(count2):
    font = mediumText2
    text = font.render("Asteroids Destroyed  >> " +str(count2),True,green)
    gameDisplay.blit(text,((25,0)))

def pause_music():
    global music 
    if music is True:
        music = False
        pygame.mixer.music.pause()
    else:
        music = True
        pygame.mixer.music.unpause()

def quit_game():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    
    textSurf,textRect  = text_objects(msg,smallText,white)
    textRect.center = ((x +(w/2)),(y +(h/2)))
    gameDisplay.blit(textSurf,textRect)

def shoot_bullet(x,y):
    bullet_state = "Fire"
    gameDisplay.blit(bulletImg,(x+15,y-40))

def unpause_game():
    global pause
    pause = False
def pause_game():
    global music
    screen.blit(menuImg,[0,0])
    gameDisplay.blit(extraImg,(500,150))
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause_game() 
        TextSurf, TextRect = text_objects("Pause Menu",mediumText1,white)
        TextRect.center = (350,50)
        gameDisplay.blit(TextSurf, TextRect)
        button("Continue",100,550,125,50,green,bright_green,unpause_game)
        button("Quit",500,550,125,50,red,bright_red,quit_game)
        button(" ",600,30,30,30,black,black,pause_music)
        if music is True:
            gameDisplay.blit(speaker3Img,(600,30))
        else:
            gameDisplay.blit(speaker0Img,(600,30))
        #asteroids_dodged(dodge)
        pygame.display.update()
        clock.tick(15)

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
    global pause
    bullet_state = "Ready"
    ship_x = (display_width * 0.45)
    ship_y = (display_height * 0.6)
    i = 0
    x_change = 0
    y_change = 0
    score = 0
    score2 = 0
    asteroid_count = 1
    asteroid_x_list=[random.randrange(ship_x-200,display_width-asteroid_width)]
    asteroid_y = -500
    asteroid_speed = 7

    bullet_x = 0
    bullet_y = ship_y
    bullet_xchange = 0
    bullet_ychange = 5

    gameExit = False
    j = 0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    pause_game()
                if event.key == pygame.K_SPACE:
                    if bullet_state is "Ready":
                        bullet_state = "Fire"
                        bullet_x = ship_x
                        shoot_bullet(bullet_x,bullet_y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0
                
        ship_x += x_change
        ship_y += y_change
        asteroid_y += asteroid_speed
        screen.blit(backgroundImg,[0,0])
        asteroid(asteroid_x_list,asteroid_y)
        ship(ship_x,ship_y)
        #button("Pause",25,25,100,50,blue,light_blue,pause_game)
        asteroids_dodged(score)
        asteroids_destroyed(score2)
        if ship_x > display_width - ship_width:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 0
        if ship_x < 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = 0
        if ship_y > display_height -ship_height :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change = 0
        if ship_y < 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = 0
        if asteroid_y > display_height:
            asteroid_x_list = []
            asteroid_y = 0 - asteroid_height
            for x in range(asteroid_count):
                asteroid_x_new = random.randrange(ship_x-100,display_width-asteroid_width)
                asteroid_x_list.append(asteroid_x_new)
            
            asteroid(asteroid_x_list,asteroid_y)
            score +=1
            if score > 1 and score%5 == 1:
                asteroid_speed += 1
                x_change +=1
                y_change +=1
            if score %10 == 0:
                i = int(score/10)+1
                message_display(f"Level {i}!",bright_green)
                if asteroid_count <4:
                    asteroid_count += 1
        if ship_y + ship_height > asteroid_y and ship_y + 40 < asteroid_y + asteroid_height :
            for asteroid_x in asteroid_x_list:
                if ship_x > asteroid_x and ship_x <asteroid_x + asteroid_width or ship_x + ship_width > asteroid_x and ship_x +ship_width < asteroid_x + asteroid_width:
                    crash(score)
        
        if bullet_state is "Fire":
            if bullet_y < asteroid_y + asteroid_height:
                for asteroid_x in asteroid_x_list:
                    if bullet_x > asteroid_x and bullet_x <asteroid_x + asteroid_width or bullet_x + bullet_width > asteroid_x and bullet_x +bullet_width < asteroid_x + asteroid_width:
                        #crash(score)
                        score2 += 1
                        bullet_y = ship_y
                        bullet_x = 0
                        bullet_state = "Ready"
                        asteroid_x -= 200
                        asteroid_y = 0 - asteroid_height
                        

        if bullet_y <= 0:
            bullet_y = ship_y
            bullet_state = "Ready"
        if bullet_state is "Fire":
            shoot_bullet(bullet_x,bullet_y)
            bullet_y -= bullet_ychange
        
        pygame.display.update()
        clock.tick(60)

game_intro()
quit_game()
