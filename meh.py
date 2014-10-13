#!/usr/bin/env python


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import pygame
import time
import random


# modified from:
# https://learn.adafruit.com/pi-video-output-using-pygame/pointing-pygame-to-the-framebuffer

class pyscope :
    screen = None;

    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print "I'm running under X display = {0}".format(disp_no)

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

        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print "Framebuffer size: %d x %d" % (size[0], size[1])
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

    def test(self):
        # Fill the screen with red (255, 0, 0)
        red = (255, 0, 0)
        self.screen.fill(red)
        # Update the display
        pygame.display.update()

# Create an instance of the PyScope class
scope = pyscope()
#scope.test()
#time.sleep(10)


## Fill the screen with red (255, 0, 0)
#red = (255, 0, 0)
#self.screen.fill(red)
# Update the display
#pygame.display.update()

scope.screen.fill((33, 33, 33))

pygame.display.update()

time.sleep(1)

bg = pygame.image.load('wood.bmp')
bgRect = bg.get_rect()
#size = (width, height) = bg.get_size()
#screen = pygame.display.set_mode(size)

#size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
#print pygame.display.Info().current_w, pygame.display.Info().current_h

#scope.screen.blit(bg, (900, 1600))

scope.screen.blit(bg, bgRect)       

font = pygame.font.Font(None, 30)

text_surface = font.render('Chris Hansen', True, (255, 255, 255)) #white
# Blit the text at 10, 0
scope.screen.blit(text_surface, (10,0))
# update the display
pygame.display.update()

time.sleep(10)


