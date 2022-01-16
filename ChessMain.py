import pygame
import ChessEngine

Width = Height = 512
DEM = 8
SO_SIZE = Height // DEM
MAX_FPS = 15
IMAGES = {}




def loadImages():
    pieces = ['wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:        
        IMAGES[piece] = pygame.image.load("images/"+ piece +".png"), (SO_SIZE, SO_SIZE)
        pass


 


def main():
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0]//SO_SIZE
                row = location[1]//SO_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                    sqSelected = ()
                    playerClicks = []
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    gs.undoMove()
                    moveMade = True

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        pygame.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)

    drawPieces(screen, gs.board)





def drawBoard(screen):
    colors = [pygame.Color("White"), pygame.Color("gray")]
    for r in range(DEM):
        for c in range(DEM):
            color = colors[((r+c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))



     
def drawPieces(screen, board):
    for r in range(DEM):
        for c in range(DEM):
            piece = board[r][c]
            if piece == "wp":
                screen.blit(pygame.image.load("images/wp.png"), (c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))
            if piece == "bp":
                screen.blit(pygame.image.load("images/bp.png"), (c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))
            if piece == "bR":
                screen.blit(pygame.image.load("images/bR.png"), (c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))
            if piece == "bN":
                screen.blit(pygame.image.load("images/bN.png"), (c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))
            if piece == "bB":
                screen.blit(pygame.image.load("images/bB.png"), (c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))
            if piece == "wR":
                screen.blit(pygame.image.load("images/wR.png"), (c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))
            if piece == "wN":
                screen.blit(pygame.image.load("images/wN.png"), (c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))
            if piece == "wB":
                screen.blit(pygame.image.load("images/wB.png"), (c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))
            if piece == "wK":
                screen.blit(pygame.image.load("images/wK.png"), (c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))
            if piece == "wQ":
                screen.blit(pygame.image.load("images/wQ.png"), (c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))
            if piece == "bK":
                screen.blit(pygame.image.load("images/bK.png"), (c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))
            if piece == "bQ":
                screen.blit(pygame.image.load("images/bQ.png"), (c*SO_SIZE, r*SO_SIZE, SO_SIZE, SO_SIZE))



if __name__ == "__main__":
    main()

 