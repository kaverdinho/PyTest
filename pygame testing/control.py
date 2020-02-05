import pygame as py
from pygame.locals import *

"LAGA" \
"AttributeError: type object 'Controlls' has no attribute 'playerx'"
class Controlls(object):
    def __init__(self):
        self.playerx = int(300)
        self.playery = int(300)

        self.movement_speed = 21
        self.movement_speed_acceleration = 2

        self.go_down = False
        self.go_up = False
        self.go_left = False
        self.go_right = False
        self.go_dl = False
        self.go_dr = False
        self.go_ul = False
        self.go_ur = False

        self.vel_down = 0
        self.vel_up = 0
        self.vel_left = 0
        self.vel_right = 0
        self.vel_ul = 0
        self.vel_ur = 0
        self.vel_dl = 0
        self.vel_dr = 0
        py.init()
        self.on = True
        while self.on:
            for event in py.event.get():
                self.keys = py.key.get_pressed()
                                                                    # KEY DOWN
                if event.type == py.KEYDOWN:
                    if self.keys[py.K_ESCAPE]:
                        self.on = False
                                                                    #DOWN   KEY DOWN
                    elif self.keys[py.K_DOWN]:
                        if self.keys[py.K_LEFT]:
                            self.go_dl = True
                        elif self.keys[py.K_RIGHT]:
                            self.go_dr = True
                        else:
                            self.go_down = True
                                                                    # UP    KEY DOWN
                    elif self.keys[py.K_UP]:
                        if self.keys[py.K_LEFT]:
                            self.go_ul = True
                        elif self.keys[py.K_RIGHT]:
                            self.go_ur = True
                        else:
                            self.go_up = True
                                                                # RIGHT KEY DOWN
                    elif self.keys[py.K_RIGHT]:
                        if self.keys[py.K_UP]:
                            self.go_ur = True
                        elif self.keys[py.K_DOWN]:
                            self.go_dr = True
                        else:
                            self.go_right = True
                                                                 # LEFT KEY DOWN
                    elif self.keys[py.K_LEFT]:
                        if self.keys[py.K_UP]:
                            self.go_ul = True
                        elif self.keys[py.K_DOWN]:
                            self.go_dl = True
                        else:
                            self.go_left = True
                                                                    # KEY UP
                elif event.type == py.KEYUP:
                                                                    # DOWN  KEY UP
                    if event.key == K_DOWN:
                        self.vel_down = 0
                        self.vel_dl = 0
                        self.vel_dr = 0
                        self.go_dl = False
                        self.go_dr = False
                        self.go_down = False
                                                                    #UP KEY UP
                    elif event.key == K_UP:
                        self.vel_up = 0
                        self.vel_ul = 0
                        self.vel_ur = 0
                        self.go_up = False
                        self.go_ul = False
                        self.go_ur = False
                                                                    #RIGHT  KEY UP
                    elif event.key == K_RIGHT:
                        self.vel_right = 0
                        self.vel_dr = 0
                        self.vel_ur = 0
                        self.go_ur = False
                        self.go_dr = False
                        self.go_right = False
                                                                    #LEFT   KEY UP
                    elif event.key == K_LEFT:
                        self.vel_left = 0
                        self.vel_ul = 0
                        self.vel_dl = 0
                        self.go_dl = False
                        self.go_ul = False
                        self.go_left = False
                                                                    # DOWN
            if self.go_down:
                if self.vel_down < self.movement_speed:
                    self.playery += self.vel_down
                    self.vel_down += self.movement_speed_acceleration
                else:
                    self.playery += self.movement_speed
                                                                      # UP
            elif self.go_up:
                if self.vel_up < self.movement_speed:
                    self.playery -= self.vel_up
                    self.vel_up += self.movement_speed_acceleration
                else:
                    self.playery -= self.movement_speed
                                                                          # RIGHT
            elif self.go_right:
                if self.vel_right < self.movement_speed:
                    self.playerx += self.vel_right
                    self.vel_right += self.movement_speed_acceleration
                else:
                    self.playerx += self.movement_speed
                                                                            # LEFT
            elif self.go_left:
                if self.vel_left < self.movement_speed:
                    self.playerx -= self.vel_left
                    self.vel_left += self.movement_speed_acceleration
                else:
                    self.playerx -= self.movement_speed
                                                                            # UP LEFT
            elif self.go_ul:
                if self.vel_ul < self.movement_speed // 2:
                    self.playery -= self.vel_ul
                    self.playerx -= self.vel_ul
                    self.vel_ul += self.movement_speed_acceleration
                else:
                    self.playery -= self.movement_speed // 2
                    self.playerx -= self.movement_speed // 2
                                                                          # UP RIGHT
            elif self.go_ur:
                if self.vel_ur < self.movement_speed // 2:
                    self.playery -= self.vel_ur
                    self.playerx += self.vel_ur
                    self.vel_ur += self.movement_speed_acceleration
                else:
                    self.playery -= self.movement_speed // 2
                    self.playerx += self.movement_speed // 2
                                                                         # DOWN LEFT
            elif self.go_dl:
                if self.vel_dl < self.movement_speed // 2:
                    self.playery += self.vel_dl
                    self.playerx -= self.vel_dl
                    self.vel_dl += self.movement_speed_acceleration
                else:
                    self.playery += self.movement_speed // 2
                    self.playerx -= self.movement_speed // 2
                                                                         # DOWN RIGHT
            elif self.go_dr:
                if self.vel_dr < self.movement_speed // 2:
                    self.playery += self.vel_dr
                    self.playerx += self.vel_dr
                    self.vel_dr += self.movement_speed_acceleration
                else:
                    self.playery += self.movement_speed // 2
                    self.playerx += self.movement_speed // 2
        if __name__ == '__main__':
            Controlls()
