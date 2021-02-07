import pygame, sys
clock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Pong!')

WIN_SIZE = (640, 480)
screen = pygame.display.set_mode(WIN_SIZE)

def main():
    ball_rect = pygame.Rect(WIN_SIZE[0] // 2, WIN_SIZE[1] // 2, 10, 10)

    right_paddle_rect = pygame.Rect(50, WIN_SIZE[1]//2 - 25, 10, 50)
    left_paddle_rect = pygame.Rect(580, WIN_SIZE[1]//2 - 25, 10, 50)
    paddles_list = [right_paddle_rect, left_paddle_rect]

    ballX_velocity = 5
    ballY_velocity = 5
    left_paddle_aceleration = 0
    right_paddle_aceleration = 0

    font = pygame.font.Font('./fonts/FreePixel.ttf', 24)
    # font_surface = font.render(text, True, (255,255,255))
    right_score = 0
    left_score = 0
    
    for i in range(1,5):
        screen.fill((0,0,0))
        pygame.time.delay(1000)
        font_surface = font.render(str(i), True, (255,255,255))
        screen.blit(font_surface, (WIN_SIZE[0]//2 - font_surface.get_width()/2, WIN_SIZE[1]//2))
        pygame.display.update()

    while True:

        screen.fill((0,0,0))

        ball = pygame.draw.rect(screen, (255,255,255), ball_rect)
        right_paddle = pygame.draw.rect(screen, (255,255,255), right_paddle_rect)
        left_paddle = pygame.draw.rect(screen, (255,255,255), left_paddle_rect)

        ball_rect.x += ballX_velocity
        ball_rect.y += ballY_velocity
    
        if ball_rect.x > left_paddle_rect.x + 20:
            right_score += 1
            pygame.time.delay(500)
            ballX_velocity = - ballX_velocity
            ballY_velocity = - ballY_velocity
            ball_rect.x, ball_rect.y = WIN_SIZE[0]//2, WIN_SIZE[1]//2
            
        if ball_rect.x < right_paddle_rect.x - 20:
            left_score += 1
            pygame.time.delay(500)
            ballX_velocity = - ballX_velocity
            ballY_velocity = - ballY_velocity
            ball_rect.x, ball_rect.y = WIN_SIZE[0]//2, WIN_SIZE[1]//2

        if ball_rect.y > 470 or ball_rect.y < 10:
            ballY_velocity = - ballY_velocity

        for paddle in paddles_list:
            if ball_rect.colliderect(paddle):
                ballX_velocity = - ballX_velocity
                ballY_velocity = - ballY_velocity

        font_surfaceLEFT = font.render(f'Score: {left_score}', True, (255,255,255))
        font_surfaceRIGHT = font.render(f'Score: {right_score}', True, (255,255,255))

        screen.blit(font_surfaceLEFT, ((WIN_SIZE[0] - font_surfaceLEFT.get_width()) - 10, 20))
        screen.blit(font_surfaceRIGHT, ((0 + 10), 20))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_f:
                    pygame.display.set_mode(WIN_SIZE, FULLSCREEN)
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
            
        left_paddle_rect.y += left_paddle_aceleration
        right_paddle_rect.y += right_paddle_aceleration

        for i in range(0, 480, 10):
            middle_line = pygame.draw.line(screen, (255,255,255), (WIN_SIZE[0]//2, i), (WIN_SIZE[0]//2, i))

        clock.tick(30)
        pygame.display.update()
    
def menu():
    font = pygame.font.Font('./fonts/FreePixel.ttf', 24)
    text = 'Press SPACE to play!'
    font_surface = font.render(text, True, (255,255,255))
    while True:
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
        
        screen.blit(font_surface, (WIN_SIZE[0]//2 - font_surface.get_width()/2, WIN_SIZE[1]//2))
        pygame.display.update()

if __name__ == '__main__':
    menu()