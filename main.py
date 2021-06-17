# main.py
import pygame
from pygame.locals import *
from pygame.version import PygameVersion
from constants import *

from ball import Ball
from paddle import Paddle
from inputs import handle_events
from inputs import handle_input

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONG")
image = pygame.image.load("image.jpg")
image_lost = pygame.image.load("image_game_over.jpg")

# ajout d'une musique

background_music = pygame.mixer.Sound("Chocobo_s-Theme.ogg")
background_music.play()


# creating a object

clock = pygame.time.Clock()

done = [False]
is_game_over = [False]

ball = None
left_paddle = None
right_paddle = None
stop_son = [True]



def setup_game():
    global ball
    global left_paddle
    global right_paddle
    ball = Ball()
    left_paddle = Paddle()
    right_paddle = Paddle()
    right_paddle.rect.x = SCREEN_WIDTH - right_paddle.rect.width



def draw_game_over():
    global stop_son
    global background_music
    global image_lost
    font = pygame.font.Font("freesansbold.ttf", 32)
    game_over = font.render("GAME OVER", True, RED)
    game_over_rect = game_over.get_rect()
    game_over_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen.blit(image_lost, (0, 0))
    screen.blit(game_over, game_over_rect)
    
    if stop_son[0] == True:
        background_music.stop()
        game_over_sound = pygame.mixer.Sound("Sounds_effect/game_over.ogg")
        game_over_sound.play()
        stop_son[0] = False

def draw_game():
    left_paddle.draw(screen)
    right_paddle.draw(screen)
    ball.draw(screen)
    


def draw():
    screen.fill(WHITE)
    screen.blit(image, (0, 0))
    if is_game_over[0]:
        draw_game_over()
    else:
        draw_game()

    pygame.display.flip()


def update():
    handle_events(done)
    if not is_game_over[0]:
        handle_input(left_paddle, right_paddle)
        ball.update(left_paddle, right_paddle, is_game_over)


setup_game()

while not done[0]:
    
    clock.tick(30)
    update()
    draw()

pygame.quit()
