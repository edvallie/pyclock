#!/usr/bin/env python


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import pygame
import time
import random

screen = None;

# FB init stuff taken from:
# https://web.archive.org/web/20130601053413/http://www.karoltomala.com/blog/?p=679
drivers = ['fbcon', 'directfb', 'svgalib']

found = False
for driver in drivers:
    if not os.getenv('SDL_VIDEODRIVER'):
        os.putenv('SDL_VIDEODRIVER', driver)
    try:
        pygame.display.init()
    except pygame.error:
        print 'Driver: {0} failed.'.format(driver)
        continue
    found = True
    break

    if not found:
        raise Exception('No suitable video driver found!')


screen = pygame.display.set_mode((1600, 900))
pygame.font.init()

bg = pygame.image.load('wood.bmp')
bg = pygame.transform.scale(bg, (1600, 900))
screen.blit(bg, bg.get_rect())


font = pygame.font.Font(None, 30)

text_surface = font.render('Ben Dover', True, (255, 255, 255)) #white
# Blit the text at 10, 0
screen.blit(text_surface, (10,0))
#update the display
pygame.display.update()

time.sleep(10)


