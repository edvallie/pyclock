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

bg = pygame.image.load('wood.jpg')
bg = pygame.transform.scale(bg, (width, height))
screen.blit(bg, bg.get_rect())


font = pygame.font.Font(None, 30)

header_punchedIn = font.render('Punched In', True, (255, 255, 255), (0, 0, 0))
header_punchedOut = font.render('Punched Out', True, (255, 255, 255), (0, 0, 0))

#print header_punchedIn.get_size()[0]

screen.blit(header_punchedIn, (width * 0.25, height * 0.05556))
screen.blit(header_punchedOut, ((width * 0.25) + (width * 0.2875), height * 0.05556))

# dimensions of the boxes containing people punched in/out
box_width = width * 0.25
box_height = height * 0.85

# screen position of the list of people punched in
box_punchedIn_x = width * 0.21875
box_punchedIn_y = height * 0.09

# screen position of the list of people punched out
box_punchedOut_x = width * 0.50
#box_punchedOut_y = height / 11
#box_punchedOut_x = (width * 0.74) #+ (width / 4)
box_punchedOut_y = height * 0.09

# create the "surface" for punched in users, set transparent
box_punchedIn = pygame.Surface((box_width, box_height))
box_punchedIn.set_alpha(128)

# create the "surface" for punched out users, set transparent
box_punchedOut = pygame.Surface((box_width, box_height))
box_punchedOut.set_alpha(128)


# Font size for people's names
font = pygame.font.Font(None, 21)

people_punchedIn = ['Emmerson Bigguns', 'Shea Verpussi', 'Dick Gozinya', 'May Anne Naise', 'Amanda Faulk', 'Anna Bortion', 'Ben Dover', 'Berry McCaulkiner', 'Ben Wabawls', 'Buck Nekkid', 'Connie Lingus', 'Clint Toris', 'Craven Moorehead', 'Dick Cumming', 'Dee Flower', 'Drew Peacock', 'Doug McCockin', 'Dick Trickle', 'Eric Shun', 'Harry P. Ness', 'Harry Azzol', 'Haywood Jablomi', 'Hugh Janus', 'Issac Cox', 'Ivona Ryder', 'Semour Butts', 'Jack Mehoff', 'Justin Hermouth','Kimmy Hed', 'Lou Sanus', 'Martha Fokker', 'Mike Rotch', 'Mike Hunt', 'Neil Enbob', 'Ophelia Cuming', 'Penny Tration', 'Pat McRotch', 'Phil McCrackin', 'Ruben Mycock', 'Sarah Tonin', 'Wayne Kerr']


text_surface = font.render(people_punchedIn[0], True, (255, 255, 255))
font_size = text_surface.get_height()

print font_size
print len(people_punchedIn)


y = 0
i = 0
for person in people_punchedIn:
    if i % 2 == 0:
        text_surface = font.render(person, True, (255, 255, 255))
#        pygame.draw.rect(box_punchedIn, (255, 0, 0), (0, y, width / 4, font_size))
    else:
        text_surface = font.render(person, True, (0, 0, 0))
        pygame.draw.rect(box_punchedIn, (255, 255, 255), (0, y, box_width, font_size))

    box_punchedIn.blit(text_surface, (width * 0.00625, y))
    y += text_surface.get_size()[1]
    i += 1


screen.blit(box_punchedIn, (box_punchedIn_x, box_punchedIn_y))


people_punchedOut = ['Emmerson Bigguns', 'Shea Verpussi', 'Dick Gozinya', 'May Anne Naise', 'Amanda Faulk', 'Anna Bortion', 'Ben Dover', 'Berry McCaulkiner', 'Ben Wabawls', 'Buck Nekkid', 'Connie Lingus', 'Clint Toris', 'Craven Moorehead', 'Dick Cumming', 'Dee Flower', 'Drew Peacock', 'Doug McCockin', 'Dick Trickle', 'Eric Shun', 'Harry P. Ness', 'Harry Azzol', 'Haywood Jablomi', 'Hugh Janus', 'Issac Cox', 'Ivona Ryder', 'Semour Butts', 'Jack Mehoff', 'Justin Hermouth','Kimmy Hed', 'Lou Sanus', 'Martha Fokker', 'Mike Rotch', 'Mike Hunt', 'Neil Enbob', 'Ophelia Cuming', 'Penny Tration', 'Pat McRotch', 'Phil McCrackin', 'Ruben Mycock', 'Sarah Tonin', 'Wayne Kerr']


y = 0
i = 0
for person in people_punchedOut:
    if i % 2 == 0:
        text_surface = font.render(person, True, (255, 255, 255))
    else:
        text_surface = font.render(person, True, (0, 0, 0))
        pygame.draw.rect(box_punchedOut, (255, 255, 255), (0, y, width * 0.25, font_size))

    box_punchedOut.blit(text_surface, (width * 0.00625, y))
    y += text_surface.get_size()[1]
    i += 1

#text_surface = font.render('Hugh Janus', True, (255, 255, 255))
#box_punchedOut.blit(text_surface, (0, 23))

screen.blit(box_punchedOut, (box_punchedOut_x, box_punchedOut_y))

#update the display
pygame.display.update()

#time.sleep(10)
for line in sys.stdin:
	print line




