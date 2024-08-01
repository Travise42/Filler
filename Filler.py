
import pygame
import random as rand
import id, color
from Game import Game
from Board import Board
from Menu import Menu, Button

WIDTH = 1000
HEIGHT = 800

def init():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF, 32)
    pygame.display.set_caption("Filler")
    #pygame.display.set_icon(pygame.image.load("icon.png").convert())
    clock = pygame.time.Clock()

    homeFont = pygame.font.SysFont("monospace", 60)
    gameFont = pygame.font.SysFont("monospace", 40)

    home = Menu(screen)
    play = Button("Play")
    settings = Button("Settings")
    quit = Button("Quit")
    home.add_buttons(play, settings, quit)

    music = pygame.mixer.music.load("ambient.mp3")
    #pygame.mixer.music.play(-1)

    scene = id.HOME
    #game.start()

    running = True
    mouseDown = False
    while running:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        for event in events:
            # Close the game
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False
        
        if scene == id.HOME:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if play.state:
                        scene = id.GAME
                        game = Game(screen, (WIDTH, HEIGHT))
                    elif settings.state:
                        scene = id.SETTINGS
                    elif quit.state:
                        running = False
            
            home.update(pygame.mouse.get_pos(), mouseDown)
            
            ## Drawing ##
            
            screen.fill(color.FOREGROUND)
            
            home.draw()
        
        elif scene == id.SETTINGS:
            for event in events:
                pass
                    
            screen.fill(color.FOREGROUND)
                    
        elif scene == id.GAME:
            # Handle events
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
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
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    scene = id.HOME
        
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


