import pygame


class RenderSystem:
    def __init__(self, positions):
        self.positions = positions
        myfont = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        self.paused_label = myfont.render("Paused", 1, (255,255,255))
        self.running_label = myfont.render("Running", 1, (255,255,255))

    def render(self, screen, paused):
        screen.fill((0, 0, 0))
        for i in range(len(self.positions)):
            pygame.draw.rect(screen, (0, 125, 255), (self.positions[i].x, self.positions[i].y, self.positions[i].w, self.positions[i].h))
        if paused:
            screen.blit(self.paused_label, (10, 10))
        else:
            screen.blit(self.running_label, (10, 10))
        pygame.display.update()
