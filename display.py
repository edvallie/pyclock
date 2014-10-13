#!/usr/bin/env python


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import pygame
import time
import random
import sys

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



width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

#width = 640
#height = 480

screen = pygame.display.set_mode((width, height))
pygame.font.init()
pygame.mouse.set_visible(False)

bg = pygame.image.load('wood.bmp')
bg = pygame.transform.scale(bg, (width, height))
screen.blit(bg, bg.get_rect())

font = pygame.font.Font(None, 30)

header_punchedIn = font.render('Punched In', True, (255, 255, 255), (0, 0, 0))
header_punchedOut = font.render('Punched Out', True, (255, 255, 255), (0, 0, 0))

print header_punchedIn.get_size()[0]

screen.blit(header_punchedIn, (width / 4, 50))
screen.blit(header_punchedOut, ((width / 4) + (width / 3.48), 50))

print width

#text_surface = font.render('Ben Dover', True, (255, 255, 255)) #white
# Blit the text at 10, 0
#screen.blit(text_surface, (10,0))

box_punchedIn = pygame.Surface((width / 4, height - 200))
box_punchedIn.set_alpha(128)
box_punchedIn.fill((0, 0, 0))
screen.blit(box_punchedIn, (width / 4 - 50, 80))
#pygame.draw.rect(screen, (33, 33, 33, 128), (0, 0, 100, 100))

box_punchedOut = pygame.Surface((width / 4, height - 200))
box_punchedOut.set_alpha(128)
box_punchedOut.fill((0, 0, 0))


y = 0
people_punchedOut = ['Emmerson Bigguns', 'Shea Verpussi', 'Dick Gozinya', 'May Anne Naise', 'Amanda Faulk', 'Anna Bortion', 'Ben Dover', 'Berry McCaulkiner', 'Ben Wabawls', 'Buck Nekkid', 'Connie Lingus', 'Clint Toris', 'Craven Moorehead', 'Dick Cumming', 'Dee Flower', 'Drew Peacock', 'Doug McCockin', 'Dick Trickle', 'Eric Shun', 'Harry P. Ness', 'Harry Azzol', 'Haywood Jablomi', 'Hugh Janus', 'Issac Cox', 'Ivona Ryder', 'Semour Butts', 'Jack Mehoff', 'Justin Hermouth','Kimmy Hed', 'Lou Sanus', 'Martha Fokker', 'Mike Rotch', 'Mike Hunt', 'Neil Enbob', 'Ophelia Cuming', 'Penny Tration', 'Pat McRotch', 'Phil McCrackin', 'Ruben Mycock', 'Sarah Tonin', 'Wayne Kerr']

for person in people_punchedOut:
	text_surface = font.render(person, True, (255, 255, 255))
	box_punchedOut.blit(text_surface, (10, y))
	y += 23


#text_surface = font.render('Hugh Janus', True, (255, 255, 255))
#box_punchedOut.blit(text_surface, (0, 23))

screen.blit(box_punchedOut, ((width / 4) + (width / 4), 80))

#update the display
pygame.display.update()

#time.sleep(10)
for line in sys.stdin:
	print line




