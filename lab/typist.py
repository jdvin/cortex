import pygame, sys
from pygame.locals import *

k_pressed = False
lm_pressed = False
rm_pressed = False


def check_press(k):
    global k_pressed
    pressed = pygame.key.get_pressed()
    if not k_pressed and pressed[k]:
        k_pressed = True
    elif k_pressed and (not pressed[k]):
        k_pressed = False
        return True
    return False

def check_left_click(obj):
    global lm_pressed
    if not lm_pressed and pygame.mouse.get_pressed()[0]:
        if obj.collidepoint(pygame.mouse.get_pos()):
            lm_pressed = True
            return True
    elif lm_pressed and (not pygame.mouse.get_pressed()[0]):
        lm_pressed = False
    return False

def check_right_click(obj):
    global rm_pressed
    if not rm_pressed and pygame.mouse.get_pressed()[1]:
        if obj.collidepoint(pygame.mouse.get_pos()):
            rm_pressed = True
            return True
    elif rm_pressed and (not pygame.mouse.get_pressed()[1]):
        rm_pressed = False
    return False
