import pygame , random

#Initialize Pygame
pygame.init()

#Define Display
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Catch The Clown')

#FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Game Attributes
PLAYER_STARTING_SCORE = 0
PLAYER_STARTING_LIVES = 5
PLAYER_STARTING_VELOCITY = 3
PLAYER_ACCELERATION = .5

score = PLAYER_STARTING_SCORE
lives = PLAYER_STARTING_LIVES

clown_velocity = PLAYER_STARTING_VELOCITY
clown_dx = random.choice([-1,1])
clown_dy = random.choice([-1,1])

#Set Colors
BLUE = (1,175,209)
YELLOW = (248,231,28)

#Set fonts
font = pygame.font.Font('Franxurter.ttf',32)

#Set Text
title_text = font.render("Catch The Clown", True , BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50,10)

score_text = font.render("Score: "+str(score), True , YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH-50 , 10)

lives_text = font.render("Lives: "+str(lives),True,YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH-65 , 40)

game_over_text = font.render("Game Over", True ,  BLUE , YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

continue_text = font.render("Click anywhere to continue",True , BLUE , YELLOW)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2 + 64)


#Set sounds and music
click_sound = pygame.mixer.Sound('click_sound.wav')
miss_sound = pygame.mixer.Sound('miss_sound.wav')
pygame.mixer.music.load('ctc_background_music.wav')

#Load Images
background_image = pygame.image.load('background.png')
background_rect = background_image.get_rect()
background_rect.topleft = (0,0)

clown_image = pygame.image.load('clown.png')
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)


#Game loop
pygame.mixer.music.play(-1,0.0)
running =  True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Get click Coordinate
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            #The clown was clicked
            if clown_rect.collidepoint(mouse_x , mouse_y):
                click_sound.play()
                score+=1
                clown_velocity += PLAYER_ACCELERATION


                #Move the clown in new direction
                previous_dx = clown_dx
                previous_dy = clown_dy
                while(previous_dx == clown_dx and previous_dy == clown_dy):
                    clown_dx = random.choice([-1,1])
                    clown_dy = random.choice([-1,1])
            else:
                miss_sound.play()
                lives-=1
            

    #Move the clown
    clown_rect.x += clown_dx * clown_velocity
    clown_rect.y += clown_dy * clown_velocity

    if clown_rect.left < 0 or clown_rect.right > WINDOW_WIDTH:
        clown_dx = -1*clown_dx
    if clown_rect.top < 0 or clown_rect.bottom >  WINDOW_HEIGHT:
        clown_dy = -1*clown_dy
    

    score_text = font.render("Score: "+str(score), True , YELLOW)
    lives_text = font.render("Lives: "+str(lives),True,YELLOW)

    if(lives==0):
        display.blit(game_over_text,game_over_rect)
        display.blit(continue_text,continue_rect)
        pygame.display.update()

        #Pause the game
        pygame.mixer.music.pause()
        ispause = True
        while ispause:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = PLAYER_STARTING_SCORE
                    lives = PLAYER_STARTING_LIVES
                    clown_rect.center = (WINDOW_WIDTH//2 , WINDOW_HEIGHT//2)
                    clown_dx = random.choice([-1,1])
                    clown_dy = random.choice([-1,1])
                    clown_velocity = PLAYER_STARTING_VELOCITY
                    pygame.mixer.music.play()

                    ispause=False

                elif event.type == pygame.QUIT:
                    ispause = False
                    running = False

    #Blit background
    display.blit(background_image, background_rect)

    #Blit Text
    display.blit(title_text,title_rect)
    display.blit(score_text,score_rect)
    display.blit(lives_text,lives_rect)

    #Blit Clown
    display.blit(clown_image,clown_rect)
    
    
    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)


#ENG OF GAMEM
pygame.quit()