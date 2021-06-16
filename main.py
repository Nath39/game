# main.py
import os
import sys
import pygame
from pygame import image
from pygame.draw import line
from pygame.locals import *
from constants import *

from ball import Ball
from paddle import Paddle
from inputs import handle_events
from inputs import handle_input

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONG")
image = pygame.image.load("image.jpg")

<<<<<<< Updated upstream
=======

# ajout d'une musique
music = pygame.mixer.Sound("Chocobo_s-Theme.ogg")
music.play()

>>>>>>> Stashed changes
# creating a object

clock = pygame.time.Clock()

done = [False]
is_game_over = [False]

ball = None
left_paddle = None
right_paddle = None


def setup_game():
    global ball
    global left_paddle
    global right_paddle
    ball = Ball()
    left_paddle = Paddle(PADDLE_TALLE)
    right_paddle = Paddle(PADDLE_TALLE)
    right_paddle.rect.x = SCREEN_WIDTH - right_paddle.rect.width


def draw_game_over():
    font = pygame.font.Font("freesansbold.ttf", 32)
    game_over = font.render("GAME OVER", True, RED)
    game_over_rect = game_over.get_rect()
    #placer musique
    game_over_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen.blit(game_over, game_over_rect)


def draw_game():
    left_paddle.draw(screen)
    right_paddle.draw(screen)
    ball.draw(screen)


def draw():
    screen.fill(WHITE)
    screen.blit(image, (0, 0))
    pygame.draw.line(screen, RED, (0, 0), (0, SCREEN_HEIGHT),4)# ligne de gauche
    pygame.draw.line(screen, RED, (SCREEN_WIDTH, 0), (0,0 ),4)# ligne de haut
    pygame.draw.line(screen, RED, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT),4) # ligne du milieu
    pygame.draw.line(screen, RED, (0,SCREEN_HEIGHT), (SCREEN_WIDTH,SCREEN_HEIGHT),8)# ligne bas
    pygame.draw.line(screen, RED, (SCREEN_WIDTH, 0), (SCREEN_WIDTH,SCREEN_HEIGHT),8)# ligne de droite
    

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
