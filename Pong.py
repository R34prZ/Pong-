# import essencial modules
import pygame, sys
clock = pygame.time.Clock()
from pygame.locals import *

# init pygame and mixer(for sounds), and set game caption name
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Pong!')

# setting screen size and screen variable
WIN_SIZE = (720, 480)
screen = pygame.display.set_mode(WIN_SIZE)

# function that blits text in the screen in a easier way
def blit_text(text, x, y, font ='./fonts/FreePixel.ttf', font_size=24, color=(255,255,255), center=False):
    screen_font = pygame.font.Font(font, font_size)
    text_surface = screen_font.render(text, True, color)
    if center:
        x = (WIN_SIZE[0]//2 - text_surface.get_width()/2)
        screen.blit(text_surface, (x, y))
    else:
        screen.blit(text_surface, (x, y))

# function that play sounds in a easier way
def play_sound(sound):
    sound_file = pygame.mixer.Sound(sound)
    pygame.mixer.Sound.play(sound_file)

# main function
def main():
    # game objects rects
    ball_rect = pygame.Rect(WIN_SIZE[0] // 2, WIN_SIZE[1] // 2, 10, 10)
    right_paddle_rect = pygame.Rect(WIN_SIZE[0] *0 + 50, WIN_SIZE[1]//2 - 25, 10, 50)
    left_paddle_rect = pygame.Rect(WIN_SIZE[0] - 50, WIN_SIZE[1]//2 - 25, 10, 50)
    paddles_list = [right_paddle_rect, left_paddle_rect]

    # variable to set ball's velocity and aceleartion of the paddles(used to move them)
    ball_velocity = [7,7]
    left_paddle_aceleration = 0
    right_paddle_aceleration = 0

    # score
    right_score = 0
    left_score = 0
    
    # variables to toggle fullscreen and show fps
    fullscreen = False
    show_fps = False

    # this part puts the '3,2,1' counter in teh beggining
    for i in range(1,5):
        screen.fill((0,0,0))
        blit_text('tip: press F to fullscreen', WIN_SIZE[0]//2, WIN_SIZE[1] -50, center=True)
        pygame.time.delay(1000)
        blit_text(str(i),0 ,WIN_SIZE[1]//2, center=True) # the x value in here is just because it's mandatory, but it's
        pygame.display.update()                                         # totally being defined by the "center" parameter

    # mainloop
    while True:

        screen.fill((0,0,0))

        # drawing objects on screen
        ball = pygame.draw.rect(screen, (255,255,255), ball_rect)
        right_paddle = pygame.draw.rect(screen, (255,255,255), right_paddle_rect)
        left_paddle = pygame.draw.rect(screen, (255,255,255), left_paddle_rect)

        # making the ball move
        ball_rect.x += ball_velocity[0]
        ball_rect.y += ball_velocity[1]
        
        # defining score 
        if ball_rect.x > left_paddle_rect.x + 20:
            right_score += 1
            play_sound('./snd/score.wav')
            pygame.time.delay(500)
            ball_velocity[0] = - ball_velocity[0]
            ball_velocity[1] = - ball_velocity[1]
            ball_rect.x, ball_rect.y = WIN_SIZE[0]//2, WIN_SIZE[1]//2
            
        if ball_rect.x < right_paddle_rect.x - 20:
            left_score += 1
            play_sound('./snd/score.wav')
            pygame.time.delay(500)
            ball_velocity[0] = - ball_velocity[0]
            ball_velocity[1] = - ball_velocity[1]
            ball_rect.x, ball_rect.y = WIN_SIZE[0]//2, WIN_SIZE[1]//2

        # makes ball collide in the Y vertex(?)
        if ball_rect.y > 470 or ball_rect.y < 10:
            ball_velocity[1] = - ball_velocity[1]

        # makes ball collide with paddle and set effects for that
        for paddle in paddles_list:
            if ball_rect.colliderect(paddle):
                ball_velocity[0] = - ball_velocity[0]
                ball_velocity[1] = - ball_velocity[1]
                play_sound('./snd/hit.wav')
            if paddle.bottom < WIN_SIZE[1] * 0:
                paddle.bottom = WIN_SIZE[1]
            elif paddle.top > WIN_SIZE[1]:
                paddle.top = WIN_SIZE[1] * 0

        # score text on each side of the screen for the 2 players
        blit_text(f'Score: {left_score}', WIN_SIZE[0] - 110, 20)
        blit_text(f'Score: {right_score}', (WIN_SIZE[0]*0)+10, 20)

        fps = clock.get_fps()
        # for loop to handle keys and exit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        pygame.display.set_mode(WIN_SIZE, FULLSCREEN)
                    else:
                        pygame.display.set_mode(WIN_SIZE)
                if event.key == K_TAB:
                    show_fps = not show_fps
                if event.key == K_UP:
                    left_paddle_aceleration -= 10
                if event.key == K_DOWN:
                    left_paddle_aceleration += 10
                if event.key == K_w:
                    right_paddle_aceleration -= 10
                if event.key == K_s:
                    right_paddle_aceleration += 10
            if event.type == KEYUP:
                left_paddle_aceleration = 0
                right_paddle_aceleration = 0
        
        # makes paddles move!
        left_paddle_rect.y += left_paddle_aceleration
        right_paddle_rect.y += right_paddle_aceleration

        # shows fps if True
        if show_fps:
            blit_text(f'FPS: {int(fps)}', 0, WIN_SIZE[1]-50,color=(255,0,255), center=True)

        # draw the middle screen line
        for i in range(0, WIN_SIZE[1], 10):
            middle_line = pygame.draw.line(screen, (255,255,255), (WIN_SIZE[0]//2, i), (WIN_SIZE[0]//2, i))

        # game tick(fps(?)) and display update
        clock.tick(30)
        pygame.display.update()
    
# menu, the first thing i'll see
def menu():
    # main menu loop
    while True:
        # for loop to handle keys
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    main()
        blit_text('Press SPACE to play!', 0, WIN_SIZE[1]//2, center=True)
        pygame.display.update()

if __name__ == '__main__':
    menu()