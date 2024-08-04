
import pygame
import random as rand
import id, color
from Game import Game
from Board import Board
from Engine import Engine
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
    play = Button("Play", color.COLORS[id.BLUE])
    settings = Button("Engine", color.COLORS[id.GREEN])
    quit = Button("Quit", color.COLORS[id.RED])
    home.add_buttons(play, settings, quit)
    modeMenu = Menu(screen)
    person = Button("Person", color.COLORS[id.YELLOW])
    computer = Button("Computer", color.COLORS[id.PURPLE])
    backHome = Button("Back", color.COLORS[id.BLACK])
    modeMenu.add_buttons(person, computer, backHome)
    levelMenu = Menu(screen)
    easy = Button("Super Easy", color.COLORS[id.GREEN])
    medium = Button("Very Easy", color.COLORS[id.YELLOW])
    hard = Button("Easy", color.COLORS[id.RED])
    backMenu = Button("Back", color.COLORS[id.BLACK])
    levelMenu.add_buttons(easy, medium, hard, backMenu)
    engineMenu = Menu(screen, (WIDTH - 125, HEIGHT - 200))
    done = Button("Done", color.COLORS[id.GREEN], 40)
    cancel = Button("Back", color.COLORS[id.RED], 40)
    engineMenu.add_buttons(done, cancel)

    music = pygame.mixer.music.load("ambient.mp3")
    #pygame.mixer.music.play(-1)

    scene = id.HOME

    menuBoard = generateBoard()

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
                        scene = id.MODE
                        menuBoard = generateBoard()
                    elif settings.state:
                        scene = id.ENGINE
                        engine = Engine(screen)
                    elif quit.state:
                        running = False
            
            home.update(mouseDown)
            
            ## Drawing ##
            
            screen.fill(color.FOREGROUND)
            
            screen.blit(menuBoard, (0, 0))

            home.draw()

        elif scene == id.MODE:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if person.state:
                        scene = id.GAME
                        game = Game(screen, id.PERSON)
                    elif computer.state:
                        scene = id.LEVEL
                        menuBoard = generateBoard()
                    elif backHome.state:
                        scene = id.HOME
                        menuBoard = generateBoard()

            modeMenu.update(mouseDown)
            
            ## Drawing ##
            
            screen.fill(color.FOREGROUND)
            
            screen.blit(menuBoard, (0, 0))
            
            modeMenu.draw()

        elif scene == id.LEVEL:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if easy.state:
                        scene = id.GAME
                        game = Game(screen, id.EASY)
                    elif medium.state:
                        scene = id.GAME
                        game = Game(screen, id.MEDIUM)
                    elif hard.state:
                        scene = id.GAME
                        game = Game(screen, id.HARD)
                    elif backMenu.state:
                        scene = id.MODE
                        menuBoard = generateBoard()

            levelMenu.update(mouseDown)
            
            ## Drawing ##
            
            screen.fill(color.FOREGROUND)
            
            screen.blit(menuBoard, (0, 0))
            
            levelMenu.draw()
        
        elif scene == id.ENGINE:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    engine.click()

                    if done.state:
                        scene = id.GAME
                        game = Game(screen, id.PERSON, engine.board)
                    elif cancel.state:
                        scene = id.HOME

            engineMenu.update(mouseDown)
                    
            screen.fill(color.FOREGROUND)
            engine.draw()

            engineMenu.draw()
                    
        elif scene == id.GAME:
            # Handle events
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    game.panel.click()

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
            text = ["YOU WIN!", "YOU LOSE!", "DRAW!"][(game.playerScore <= game.opponentScore) + (game.playerScore == game.opponentScore)]
            screen.blit(gameFont.render(text, True, color.GAMEOVER[game.playerScore < game.opponentScore]),
                        (WIDTH/2 - gameFont.size(text)[0]/2, HEIGHT/2 - gameFont.size(text)[1]/2, *gameFont.size(text)))
        
        # Refresh the screen
        clock.tick(30)
        pygame.display.update()

def generateBoard() -> pygame.Surface:
    board_surface = pygame.Surface((8, 7), pygame.SRCALPHA)
    board = Board.create_board(None)

    rands = [(0, 3), (1, 3), (2, 4), (4, 4), (4, 4), (4, 4), (4, 4)]
    for row in range(7):
        for side in range(2):
            for square in range(0, rand.randint(*rands[row])):
                column = 7-square if side else square
                board_color = color.COLORS[board[column][row]]
                board_surface.set_at((column, row), board_color)

    surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    surface.blit(pygame.transform.rotate(pygame.transform.scale(board_surface, (WIDTH, HEIGHT)), -30), (-300, 200))

    return surface


if __name__ == "__main__":
    init()
    pygame.quit()


