import pygame
import math
import id, color


class Menu:

    def __init__(self, surface):
        self.buttons = []
        self.surface = surface

        self.width = 0
        self.height = 30

    def add_button(self, button):
        self.buttons.append(button)

        if button.defaultSurface.get_width() + 100 > self.width:
            self.width = button.defaultSurface.get_width() + 100

        self.height += 100

    def add_buttons(self, *buttons):
        for button in buttons:
            self.add_button(button)

    def update(self, mouse_pos, mouse_is_down):
        for i, button in enumerate(self.buttons):
            button.update(mouse_pos, self.surface, i, len(self.buttons), mouse_is_down)

    def draw(self):
        for i, button in enumerate(self.buttons):
            button.draw(self.surface, i, len(self.buttons))

class Button:

    def __init__(self, text):
        self.text = text
        self.font = pygame.font.SysFont("monospace", 60)
        self.defaultSurface = pygame.Surface((self.font.size(self.text)[0] + 80, 70), pygame.SRCALPHA)
        self.hoveredSurface = pygame.Surface((self.font.size(self.text)[0] + 100, 80), pygame.SRCALPHA)
        self.clickedSurface = pygame.Surface((self.font.size(self.text)[0] + 80, 70), pygame.SRCALPHA)

        self.load()

    def load(self):
        pygame.draw.rect(self.defaultSurface, color.BACKGROUND, (0, 0, self.defaultSurface.get_width(), self.defaultSurface.get_height()), 0, 10)
        pygame.draw.rect(self.defaultSurface, color.HIGHLIGHT, (0, 0, self.defaultSurface.get_width(), self.defaultSurface.get_height()), 5, 10)
        self.defaultSurface.blit(self.font.render(self.text, True, color.HIGHLIGHT), (40, self.defaultSurface.get_height()/2 - self.font.size(self.text)[1]/2))

        pygame.draw.rect(self.clickedSurface, color.FOREGROUND, (0, 0, self.clickedSurface.get_width(), self.clickedSurface.get_height()), 0, 10)
        pygame.draw.rect(self.clickedSurface, color.BACKGROUND, (0, 0, self.clickedSurface.get_width(), self.clickedSurface.get_height()), 5, 10)
        self.clickedSurface.blit(self.font.render(self.text, True, color.BACKGROUND), (40, self.clickedSurface.get_height()/2 - self.font.size(self.text)[1]/2))

        self.font = pygame.font.SysFont("monospace", 65)
        pygame.draw.rect(self.hoveredSurface, color.FOREGROUND, (0, 0, self.hoveredSurface.get_width(), self.hoveredSurface.get_height()), 0, 10)
        pygame.draw.rect(self.hoveredSurface, color.CONTRAST, (0, 0, self.hoveredSurface.get_width(), self.hoveredSurface.get_height()), 8, 10)
        self.hoveredSurface.blit(self.font.render(self.text, True, color.CONTRAST), (40, self.hoveredSurface.get_height()/2 - self.font.size(self.text)[1]/2))

    def update(self, mouse_pos, surface, number, total, mouse_is_down):
        mouseX = mouse_pos[0] - (surface.get_width()/2 - self.defaultSurface.get_width()/2)
        mouseY = mouse_pos[1] - (surface.get_height()/2 - (100*total - 30)/2 + 30 + 100*number)

        # If touching mouse
        if (0 < mouseX and mouseX < self.defaultSurface.get_width() and
            0 < mouseY and mouseY < self.defaultSurface.get_height()):
            if mouse_is_down:
                self.state = 2
                return
            self.state = 1
            return
        self.state = 0

    def draw(self, surface, number, total):
        button = [self.defaultSurface, self.hoveredSurface, self.clickedSurface][self.state]
        surface.blit(button, (surface.get_width()/2 - button.get_width()/2, surface.get_height()/2 - (100*total - 30)/2 + 65 + 100*number - button.get_height()/2))
