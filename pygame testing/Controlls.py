import pygame as py
import sys
from pygame.locals import *

playerx = int(300)
playery = int(300)

movement_speed = 21
movement_speed_acceleration = 2

go_down = False
go_up = False
go_left = False
go_right = False
go_dl = False
go_dr = False
go_ul = False
go_ur = False

vel_down = 0
vel_up = 0
vel_left = 0
vel_right = 0
vel_ul = 0
vel_ur = 0
vel_dl = 0
vel_dr = 0

py.init()
width, height = 600, 600 #-*/-input('>> ').split(' ')
size = int(width), int(height)
screen = py.display.set_mode(size)
on = True
while on:
    py.time.delay(100)
    for event in py.event.get():
        if event.type == py.QUIT:
            on = False
        keys = py.key.get_pressed()
        if event.type == py.KEYDOWN:
            if keys[py.K_ESCAPE]:
                # on = False
                width, height = input('>> ').split(' ')
                size = int(width), int(height)
                screen = py.display.set_mode(size)

                                                            #KEY DOWN
            elif keys[py.K_DOWN]:
                if keys[py.K_LEFT]:
                    go_dl = True
                elif keys[py.K_RIGHT]:
                    go_dr = True
                else:
                    go_down = True

            elif keys[py.K_UP]:
                if keys[py.K_LEFT]:
                    go_ul = True
                elif keys[py.K_RIGHT]:
                    go_ur = True
                else:
                    go_up = True

            elif keys[py.K_RIGHT]:
                if keys[py.K_UP]:
                    go_ur = True
                elif keys[py.K_DOWN]:
                    go_dr = True
                else:
                    go_right = True

            elif keys[py.K_LEFT]:
                if keys[py.K_UP]:
                    go_ul = True
                elif keys[py.K_DOWN]:
                    go_dl = True
                else:
                    go_left = True
                                                            # KEY UP
        elif event.type == py.KEYUP:
            if event.key == K_DOWN:
                vel_down = 0
                vel_dl = 0
                vel_dr = 0
                go_dl = False
                go_dr = False
                go_down = False

            elif event.key == K_UP:
                vel_up = 0
                vel_ul = 0
                vel_ur = 0
                go_up = False
                go_ul = False
                go_ur = False

            elif event.key == K_RIGHT:
                vel_right = 0
                vel_dr = 0
                vel_ur = 0
                go_ur = False
                go_dr = False
                go_right = False

            elif event.key == K_LEFT:
                vel_left = 0
                vel_ul = 0
                vel_dl = 0
                go_dl = False
                go_ul = False
                go_left = False

    if go_down:
        if vel_down < movement_speed:
            playery += vel_down
            vel_down += movement_speed_acceleration
        else:
            playery += movement_speed

    elif go_up:
        if vel_up < movement_speed:
            playery -= vel_up
            vel_up += movement_speed_acceleration
        else:
            playery -= movement_speed

    elif go_right:
        if vel_right < movement_speed:
            playerx += vel_right
            vel_right += movement_speed_acceleration
        else:
            playerx += movement_speed

    elif go_left:
        if vel_left < movement_speed:
            playerx -= vel_left
            vel_left += movement_speed_acceleration
        else:
            playerx -= movement_speed

    elif go_ul:
        if vel_ul < movement_speed // 2:
            playery -= vel_ul
            playerx -= vel_ul
            vel_ul += movement_speed_acceleration
        else:
            playery -= movement_speed // 2
            playerx -= movement_speed // 2

    elif go_ur:
        if vel_ur < movement_speed // 2:
            playery -= vel_ur
            playerx += vel_ur
            vel_ur += movement_speed_acceleration
        else:
            playery -= movement_speed // 2
            playerx += movement_speed // 2

    elif go_dl:
        if vel_dl < movement_speed // 2:
            playery += vel_dl
            playerx -= vel_dl
            vel_dl += movement_speed_acceleration
        else:
            playery += movement_speed // 2
            playerx -= movement_speed // 2

    elif go_dr:
        if vel_dr < movement_speed // 2:
            playery += vel_dr
            playerx += vel_dr
            vel_dr += movement_speed_acceleration
        else:
            playery += movement_speed // 2
            playerx += movement_speed // 2

    screen.fill(0)
    py.draw.rect(screen, (255, 0, 0), [playerx, playery, 20, 20])

    py.display.update()
    py.display.flip()

sys.exit()
