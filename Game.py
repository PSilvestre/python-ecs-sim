import pygame

import time

from Entity.WaterDropletEntity import WaterDropletEntity
from System.PhysicsSystem import PhysicsSystem
from System.RenderSystem import RenderSystem

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class Game:

    def __init__(self, fps):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Playground")

        self.fps = fps
        self.ms_per_update = 1000/fps

        self.paused = True
        self.running = True

        self.entities = []
        self.position_components = []
        self.physics_components = []

        self.render_system = RenderSystem(self.position_components)
        self.physics_system = PhysicsSystem(self.position_components, self.physics_components, SCREEN_WIDTH, SCREEN_HEIGHT)

    def read_input(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused

#            if event.type == pygame.MOUSEBUTTONDOWN:
#                if event.button == 1:
#                    pos = event.pos
#                    self.add_water(pos)
        left, right, middle = pygame.mouse.get_pressed()
        if  left:
            self.add_water(pygame.mouse.get_pos())





    def game_loop(self):
        lag = 0

        while self.running:
            elapsed = pygame.time.get_ticks()
            lag += elapsed

            # process input
            self.read_input()

            #update
            while (lag >= self.ms_per_update):
                if(not self.paused):
                    self.physics_system.step(elapsed)
                lag -= self.ms_per_update

            self.render_system.render(self.screen, self.paused)

           # time.sleep(self.ms_per_update / 1000 / 2)


    def add_water(self, pos):
        x, y =  pos
        droplet = WaterDropletEntity(x,y, 10)
        self.entities.append(droplet)
        self.position_components.append(droplet.position_component)
        self.physics_components.append(droplet.physics_component)

