import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = WIDTH
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = WIDTH // 10
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# RGB
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

def drawLines():

    #1st horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    #2nd horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    # 1st vertical line
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2nd vertical line
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def drawFigures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + (SQUARE_SIZE / 2)), int(row * SQUARE_SIZE + (SQUARE_SIZE / 2))), CIRCLE_RADIUS, CIRCLE_WIDTH)

            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)


def markSquare(row, col, player):
    board[row][col] = player

def availableSquare(row, col):
    return board[row][col] == 0 #same as if-else statement

def isBoardFull():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True

def checkWin(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            drawVerticalWinningLine(col, player)
            return True

    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            drawHorizontalWinningLine(row, player)
            return True

    #asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        drawAscDiagonalLine(player)
        return True

    #desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        drawDescDiagonalLine(player)
        return True

    return False

def drawVerticalWinningLine(col, player):
    posX = col * SQUARE_SIZE + (SQUARE_SIZE // 2)

    if player == 1:
        color = CIRCLE_COLOR

    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)

def drawHorizontalWinningLine(row, player):
    posY = row * SQUARE_SIZE + (SQUARE_SIZE // 2)

    if player == 1:
        color = CIRCLE_COLOR

    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)

def drawAscDiagonalLine(player):
    if player == 1:
        color = CIRCLE_COLOR

    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def drawDescDiagonalLine(player):
    if player == 1:
        color = CIRCLE_COLOR

    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

def restart():
    screen.fill(BG_COLOR)
    drawLines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

drawLines()

player = 1

gameOver = False

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y

            clickedRow = int(mouseY // SQUARE_SIZE)
            clickedCol = int(mouseX // SQUARE_SIZE)

            if availableSquare(clickedRow, clickedCol):

                markSquare(clickedRow, clickedCol, player)
                if checkWin(player):
                    gameOver = True
                player = player % 2 + 1

                drawFigures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                gameOver = False

    pygame.display.update()