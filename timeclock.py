#!/usr/bin/env python


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import pygame
from pygame.locals import *
import time
import random
import sys

from database_functions import *

screen = None;

os.putenv('SDL_VIDEODRIVER', 'fbcon')
pygame.display.init()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

screen = pygame.display.set_mode((width, height))
pygame.font.init()
pygame.mouse.set_visible(False)

bg = pygame.image.load('wood.jpg')
bg = pygame.transform.scale(bg, (width, height))

# dimensions of the boxes containing people punched in/out
box_width = width * 0.25
box_height = height * 0.85

punch_id = ''
punch_history = ''

while True:
    screen.blit(bg, bg.get_rect())

    # black box on left side
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width * 0.35, height))

    # Display time/date
    now = time.strftime('%l:%M%p').lstrip(' ')

    # time
    font = pygame.font.Font(None, 172)
    text_surface = font.render(now, True, (255, 255, 255))
    screen.blit(text_surface, ((width * 0.35 / 2) - (text_surface.get_width() / 2), height * 0.25))
    time_height = text_surface.get_height()

    # date
    font = pygame.font.Font(None, 40)
    text_surface = font.render(time.strftime('%A, %B ') + time.strftime('%d').lstrip('0') +  time.strftime(', %Y'), True, (255, 255, 255))
    screen.blit(text_surface, ((width * 0.35 / 2) - (text_surface.get_width() / 2), height * 0.25 + time_height))

    # update last punch info on screen
    if punch_history:
        font = pygame.font.Font(None, 24)
        text_surface = font.render(punch_history, True, (255, 255, 255))
        screen.blit(text_surface, ((width * 0.35 / 2) - (text_surface.get_width() / 2), height - text_surface.get_height()))
 
    # screen position of the list of people punched in
    box_punchedIn_x = width * 0.41875
    box_punchedIn_y = height * 0.09

    # screen position of the list of people punched out
    box_punchedOut_x = width * 0.70
    box_punchedOut_y = height * 0.09

    # create the "surface" for punched in users, set transparent
    box_punchedIn = pygame.Surface((box_width, box_height))
    box_punchedIn.set_alpha(128)

    # create the "surface" for punched out users, set transparent
    box_punchedOut = pygame.Surface((box_width, box_height))
    box_punchedOut.set_alpha(128)

    # Display column headers and add a black background
    font = pygame.font.Font(None, 30)

    header_punchedIn = font.render('Employees In', True, (255, 255, 255))
    header_punchedOut = font.render('Employees Out', True, (255, 255, 255))
    font_size = header_punchedIn.get_height()

    pygame.draw.rect(screen, (0, 0, 0), (box_punchedIn_x, height * 0.05556, box_width, font_size))
    pygame.draw.rect(screen, (0, 0, 0), (box_punchedOut_x, height * 0.05556, box_width, font_size))

    screen.blit(header_punchedIn, (width * 0.41875, height * 0.05556))
    screen.blit(header_punchedOut, (width * 0.70, height * 0.05556))

    # Font size for people's names
    font = pygame.font.Font(None, 21)

    punches = getPunches()
    people_punchedIn = punches[0]
    people_punchedOut = punches[1]

    text_surface = font.render(people_punchedIn[0], True, (255, 255, 255))
    font_size = text_surface.get_height()

    y = 0
    i = 0
    for person in people_punchedIn:
        if i % 2 == 0:
            text_surface = font.render(person, True, (255, 255, 255))
        else:
            text_surface = font.render(person, True, (0, 0, 0))
            pygame.draw.rect(box_punchedIn, (255, 255, 255), (0, y, box_width, font_size))

        box_punchedIn.blit(text_surface, (width * 0.00625, y))
        y += text_surface.get_size()[1]
        i += 1

    screen.blit(box_punchedIn, (box_punchedIn_x, box_punchedIn_y))

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

    screen.blit(box_punchedOut, (box_punchedOut_x, box_punchedOut_y))

    #update the display
    pygame.display.update()

    while now == time.strftime('%l:%M%p').lstrip(' '):
        time.sleep(1)
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isnumeric():
                    punch_id += evt.unicode
                elif evt.key == K_RETURN:
                    punch_name = str(getName(punch_id))
                    if punch_name:
                        insertPunch(punch_id)
                        punch_history = 'Last punch collected for ' + str(getName(punch_id)) + ' at ' + time.strftime('%T %D')
                    else:
                        punch_history = 'Error: Punch not read!'
                    punch_id = ''
                    now = ''
                    break
