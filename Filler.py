
import pygame
import random as rand
import id, color
from Game import Game

WIDTH = 1000
HEIGHT = 800

def init():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF, 32)
    pygame.display.set_caption("Filler")
    #pygame.display.set_icon(pygame.image.load("icon.png").convert())
    clock = pygame.time.Clock()

    game = Game(screen, (WIDTH, HEIGHT))

    music = pygame.mixer.music.load("ambient.mp3")
    pygame.mixer.music.play(-1)

    homeFont = pygame.font.SysFont("monospace", 60)

    scene = id.GAME
    game.start()

    running = True
    while running:
        keys = pygame.key.get_pressed()
        
        if scene == id.HOME:
            for event in pygame.event.get():
                # Close the game
                if event.type == pygame.QUIT:
                    running = False
                    
            
            ## Drawing ##
            
            screen.fill(color.FOREGROUND)
            
            rect = screen.get_width()/2 - 200, screen.get_height()*0.1, 400, screen.get_height()*0.8
            
            pygame.draw.rect(screen, color.CONTRAST, rect, border_radius=5)
            pygame.draw.rect(screen, color.HIGHLIGHT, rect, border_radius=10, width = 12)
            pygame.draw.rect(screen, (255, 255, 255), (rect[0] + 3, rect[1] + 3, rect[2] - 6, rect[3] - 6), width = 5, border_radius=10)
            
            for i in (("PLAY", 0, id.GAME), ("SETTINGS", 100, id.SETTINGS), ("EXIT", 200, None)):
                text = i[0]
                dy = i[1]
                destination = i[2]
                if homeFont.render(text, False, (0, 0, 0)).get_rect().collidepoint(pygame.mouse.get_pos()[0] - (screen.get_width()/2 - homeFont.size(text)[0]/2), pygame.mouse.get_pos()[1] - (screen.get_height()/2 - homeFont.size(text)[1]/2 + dy)):
                    homeFont = pygame.font.SysFont("monospace", 70)
                    if pygame.mouse.get_pressed()[0]:
                        if destination == None:
                            running = False
                        scene = destination
                        if destination == id.GAME:
                            game.start()
                        continue
                homeFont.set_bold(True)
                screen.blit(homeFont.render(text, True, color.HIGHLIGHT), (screen.get_width()/2 - homeFont.size(text)[0]/2, screen.get_height()/2 - homeFont.size(text)[1]/2 + dy))
                homeFont.set_bold(False)
                screen.blit(homeFont.render(text, True, color.GLOW), (screen.get_width()/2 - homeFont.size(text)[0]/2, screen.get_height()/2 - homeFont.size(text)[1]/2 + dy))
        
        elif scene == id.SETTINGS:
            for event in pygame.event.get():
                # Close the game
                if event.type == pygame.QUIT:
                    running = False
                    
            screen.fill(color.FOREGROUND)
                    
        elif scene == id.GAME:
            # Handle events
            for event in pygame.event.get():
                # Close the game
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    game.panel.click(pygame.mouse.get_pos())

            game.update()
            
            ## Drawing ##
            
            screen.fill(color.FOREGROUND)
            game.draw()
        
        # Refresh the screen
        clock.tick(30)
        pygame.display.update()


if __name__ == "__main__":
    init()
    pygame.quit()


