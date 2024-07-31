
import pygame
import random as rand
import id, color
from Game import Game
from Board import Board

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
    #pygame.mixer.music.play(-1)

    homeFont = pygame.font.SysFont("monospace", 60)
    gameFont = pygame.font.SysFont("monospace", 40)

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
            
            if game.gameover:
                scene = id.END
            
            ## Drawing ##
            
            screen.fill(color.FOREGROUND)
            game.draw()

            pygame.draw.rect(screen, color.COLORS[game.player],
                             (Board.SQUARE_SIZE, Board.SQUARE_SIZE, Board.SQUARE_SIZE, Board.SQUARE_SIZE), 2)
            text = str(game.playerScore)
            screen.blit(gameFont.render(text, True, color.COLORS[game.player]),
                        (1.5*Board.SQUARE_SIZE - gameFont.size(text)[0]/2, 1.5*Board.SQUARE_SIZE - gameFont.size(text)[1]/2, Board.SQUARE_SIZE, Board.SQUARE_SIZE))

            pygame.draw.rect(screen, color.COLORS[game.opponent],
                             (WIDTH - 2*Board.SQUARE_SIZE, Board.SQUARE_SIZE, Board.SQUARE_SIZE, Board.SQUARE_SIZE), 1)
            text = str(game.opponentScore)
            screen.blit(gameFont.render(text, True, color.COLORS[game.opponent]),
                        (WIDTH - 1.5*Board.SQUARE_SIZE - gameFont.size(text)[0]/2, 1.5*Board.SQUARE_SIZE - gameFont.size(text)[1]/2, Board.SQUARE_SIZE, Board.SQUARE_SIZE))
        
        elif scene == id.END:
            # Handle events
            for event in pygame.event.get():
                # Close the game
                if event.type == pygame.QUIT:
                    running = False
        
            pygame.draw.rect(screen, (70, 70, 70), (WIDTH/2 - 120, HEIGHT/2 - 40, 240, 80))
            pygame.draw.rect(screen, (240, 70, 70), (WIDTH/2 - 120, HEIGHT/2 - 40, 240, 80), 5)
            text = ["YOU WIN!", "YOU LOSE!"][game.playerScore < game.opponentScore]
            screen.blit(gameFont.render(text, True, color.GAMEOVER[game.playerScore < game.opponentScore]),
                        (WIDTH/2 - gameFont.size(text)[0]/2, HEIGHT/2 - gameFont.size(text)[1]/2, *gameFont.size(text)))
        
        # Refresh the screen
        clock.tick(30)
        pygame.display.update()


if __name__ == "__main__":
    init()
    pygame.quit()


