import pygame
import math
import id, color


class Menu:

    def __init__(self, surface, pos=()):
        self.buttons = []
        self.surface = surface

        self.width = 0
        self.height = 30
        self.pos = (self.surface.get_width()/2, self.surface.get_height()/2) if pos == () else pos

    def add_button(self, button):
        self.buttons.append(button)

        if button.defaultSurface.get_width() + 100 > self.width:
            self.width = button.defaultSurface.get_width() + 100

        self.height += 100

    def add_buttons(self, *buttons):
        for button in buttons:
            self.add_button(button)

    def update(self, mouse_is_down):
        for i, button in enumerate(self.buttons):
            button.update(pygame.mouse.get_pos(), self, i, mouse_is_down)

    def draw(self):
        #pygame.draw.rect(self.surface, color.BACKGROUND, (self.surface.get_width()/2 - self.width/2, self.surface.get_height()/2 - self.height/2, self.width, self.height), 10, 10)
        for i, button in enumerate(self.buttons):
            button.draw(self, i)

class Button:

    def __init__(self, text, color, size=60):
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont("monospace", size)
        self.defaultSurface = pygame.Surface((self.font.size(self.text)[0] + 80, 70), pygame.SRCALPHA)
        self.hoveredSurface = pygame.Surface((self.font.size(self.text)[0] + 100, 80), pygame.SRCALPHA)
        self.clickedSurface = pygame.Surface((self.font.size(self.text)[0] + 80, 70), pygame.SRCALPHA)

        self.load()

    def load(self):
        pygame.draw.rect(self.defaultSurface, color.BACKGROUND, (0, 0, self.defaultSurface.get_width(), self.defaultSurface.get_height()), 0, 10)
        pygame.draw.rect(self.defaultSurface, self.color, (0, 0, self.defaultSurface.get_width(), self.defaultSurface.get_height()), 5, 10)
        self.defaultSurface.blit(self.font.render(self.text, True, self.color), (40, self.defaultSurface.get_height()/2 - self.font.size(self.text)[1]/2))

        pygame.draw.rect(self.clickedSurface, color.FOREGROUND, (0, 0, self.clickedSurface.get_width(), self.clickedSurface.get_height()), 0, 10)
        pygame.draw.rect(self.clickedSurface, self.color, (0, 0, self.clickedSurface.get_width(), self.clickedSurface.get_height()), 5, 10)
        self.clickedSurface.blit(self.font.render(self.text, True, self.color), (40, self.clickedSurface.get_height()/2 - self.font.size(self.text)[1]/2))

        self.font = pygame.font.SysFont("monospace", 65)
        pygame.draw.rect(self.hoveredSurface, color.CONTRAST, (0, 0, self.hoveredSurface.get_width(), self.hoveredSurface.get_height()), 0, 10)
        pygame.draw.rect(self.hoveredSurface, self.color, (0, 0, self.hoveredSurface.get_width(), self.hoveredSurface.get_height()), 8, 10)
        self.hoveredSurface.blit(self.font.render(self.text, True, self.color), (40, self.hoveredSurface.get_height()/2 - self.font.size(self.text)[1]/2))

    def update(self, mouse_pos, menu, number, mouse_is_down):
        mouseX = mouse_pos[0] - (menu.pos[0] - self.defaultSurface.get_width()/2)
        mouseY = mouse_pos[1] - (menu.pos[1] - (100*len(menu.buttons) - 30)/2 + 5/2 + 100*number)

        # If touching mouse
        if (0 < mouseX and mouseX < self.defaultSurface.get_width() and
            0 < mouseY and mouseY < self.defaultSurface.get_height()):
            if mouse_is_down:
                self.state = 2
                return
            self.state = 1
            return
        self.state = 0

    def draw(self, menu, number):
        button = [self.defaultSurface, self.hoveredSurface, self.clickedSurface][self.state]
        menu.surface.blit(button, (menu.pos[0] - button.get_width()/2, menu.pos[1] - (100*len(menu.buttons) - 30)/2 + 35 + 100*number - button.get_height()/2))
