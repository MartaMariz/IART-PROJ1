from re import A
from piece import Bishop, Tower, Queen, Horse, King
from utils import Action
import pygame
import pygame.freetype

class GUI:
    BG = (0,0,0)
    DIV = (255,255,255)
    SNAKE = (28, 29, 83)
    MENU_BOX = (4,6,21)
    MENU_TITLE = (97,106,154)
    MENU_FONT = (64,72,101)
    SCREENWIDTH = 600
    SCREENHEIGHT = 850
    COMMANDS = 250
    
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((self.SCREENWIDTH,self.SCREENHEIGHT))

    def mainMenu(self):
        """Function responsible for displaying the main menu
        Returns:
            Action(Enum): the action chosen by the user
        """
        inMenu = True
        while (inMenu):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return Action.QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return Action.SHOWE
                    if event.key == pygame.K_2:
                        return Action.SHOWH
                    if event.key == pygame.K_3:
                        return Action.RULES
                    elif event.key == pygame.K_ESCAPE:
                        return Action.QUIT
            self._screen.fill(self.BG)
            background_image = pygame.image.load("resources/stars.jpeg")
            self._screen.blit(background_image, (0, 0))
            font = pygame.font.Font("resources/Emulogic-zrEw.ttf", 20)
            font1 = pygame.font.Font("resources/Emulogic-zrEw.ttf", 48)
            font2 = pygame.font.Font("resources/Emulogic-zrEw.ttf", 13)
            img = font1.render("Chess Snake", True, self.MENU_TITLE, self.MENU_BOX)
            self._screen.blit(img, (30, 100))
            img = font1.render("Puzzles", True, self.MENU_TITLE, self.MENU_BOX)
            self._screen.blit(img, (130, 160))
            img = font2.render("Press to choose next action:", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (self.SCREENWIDTH/5, self.SCREENHEIGHT/3+70))
            img = font.render("1- Easy puzzle", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (self.SCREENWIDTH/5, self.SCREENHEIGHT/3+110))
            img = font.render("2- Hard puzzle", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (self.SCREENWIDTH/5, self.SCREENHEIGHT/3+140))
            img = font.render("3- Rules", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (self.SCREENWIDTH/5, self.SCREENHEIGHT/3+170))
            img = font.render("ESC- Quit", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (self.SCREENWIDTH/5, self.SCREENHEIGHT/3+200))
            pygame.display.update()
        return Action.MENU

    def rules(self):
        """Function responsible for displaying the rules

        Returns:
            Action(Enum): the action chosen by the user
        """
        inRules = True
        while (inRules):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return Action.QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        inRules = False
            self._screen.fill(self.BG)
            font = pygame.freetype.Font("resources/Emulogic-zrEw.ttf", 12)

            text_file = open("docs/rules.txt", "r")
            with open("docs/rules.txt") as text_file:
                lines = [line.rstrip() for line in text_file]
            label = []

            for i in range(len(lines)):
                img = font.render(lines[i], self.MENU_FONT, self.MENU_BOX)
                self._screen.blit(img[0], (20, 20+(i*26)+(15*i)))
            font = pygame.font.Font("resources/Emulogic-zrEw.ttf", 20)
            img = font.render("SPACE- Main menu", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (20, self.SCREENHEIGHT-self.COMMANDS+200))
            pygame.display.update()

        return Action.MENU


    def playPuzzle(self, size, pieces, snake):
        """Function responsible for displaying the board and expecting next action - 
        a move of the snake, a request for the solution (A*) or quitting

        Args:
            size (int): size of the board
            pieces (vector): vector of chess pieces
            snake (object Snake): current Snake

        Returns:
            Action(Enum): the action chosen by the user
        """
        global inGame
        inGame = True
        while inGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return Action.QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inGame = False
                    if event.key == pygame.K_UP:
                        if snake.up():
                            return Action.UP
                    if event.key == pygame.K_DOWN:
                        if snake.down():
                            return Action.DOWN
                    if event.key == pygame.K_LEFT:
                        if snake.left():
                            return Action.LEFT    
                    if event.key == pygame.K_RIGHT:
                        if snake.right():
                            return Action.RIGHT
                    if event.key == pygame.K_SPACE:
                        return Action.AS1

            self.drawBoard(size, pieces, snake)
            font = pygame.font.Font("resources/Emulogic-zrEw.ttf", 20)
            img = font.render("SPACE- Solve puzzle", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+20))
            img = font.render("ESC- Main Menu", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+50))
            pygame.display.update()

        return Action.MENU
        
    def showResult(self, size, pieces, snake):
        """Fuction responsible for displaying the result after solving with an algorithm

        Args:
            size (int): size of the board
            pieces (vector): vector of chess pieces
            snake (object Snake): current Snake

        Returns:
            Action(Enum): the action chosen by the user
        """
        global inGame
        inGame = True
        while inGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return Action.QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inGame = False
                    if event.key == pygame.K_SPACE:
                        return Action.START

            self.drawBoard(size, pieces, snake)
            font = pygame.font.Font("resources/Emulogic-zrEw.ttf", 20)
            img = font.render("SPACE- Try again", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+20))
            img = font.render("ESC- Main Menu", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+50))
            pygame.display.update()

        return Action.MENU
        
    def puzzleMenu(self, size, pieces, snake):
        """Function responsible for displaying the menu when looking at a puzzle - 
        either trying to solve it, solving with an algorithm

        Args:
            size (int): size of the board
            pieces (vector): vector of chess pieces
            snake (object Snake): current Snake

        Returns:
            Action(Enum): the action chosen by the user
        """
        inDisplay = True
        while inDisplay:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return Action.QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inDisplay = False
                    if event.key == pygame.K_1:
                        return Action.BFS
                    if event.key == pygame.K_2:
                        return Action.UCOST
                    if event.key == pygame.K_3:
                        return Action.GS1
                    if event.key == pygame.K_4:
                        return Action.AS1
                    if event.key == pygame.K_5:
                        return Action.AS2
                    elif event.key == pygame.K_SPACE:
                        return Action.START

            self.drawBoard(size, pieces, snake)
            font = pygame.font.Font("resources/Emulogic-zrEw.ttf", 15)
            font1 = pygame.font.Font("resources/Emulogic-zrEw.ttf", 28)
            font2 = pygame.font.Font("resources/Emulogic-zrEw.ttf", 13)
            img = font1.render("SPACE- Start game", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS))
            img = font2.render("Press number to solve with each algorithm:", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+40))
            img = font.render("1- BFS", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+70))
            img = font.render("2- Uniform cost", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+100))
            img = font.render("3- Greedy search", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+130))
            img = font.render("4- A* - Manhattan distance", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+160))
            img = font.render("5- A* - Diff between number of attacks", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+190))
            img = font.render("ESC- Main Menu", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+220))
            pygame.display.update()

        return Action.MENU    

    def drawBoard(self, size, pieces, snake):
        """Function responsible for displaying the board whenever a bigger function such as puzzleMenu or showResult is called

        Args:
            size (int): size of the board
            pieces (vector): vector of chess pieces
            snake (object Snake): current Snake
        """
        self._screen.fill(self.BG)
        self.size = size
        if size == 6:
            self.draw6x6()
        else:
            self.draw5x5()

        self.setPieces(pieces)
        self.setSnake(snake)


    def drawFinalMsg(self, msg):
        """Function responsible for displaying the final message

        Args:
            msg (String): final message after the game is over

        Returns:
            Action(Enum): the action chosen by the user
        """
        inMsg = True
        while (inMsg):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return Action.QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inMsg = False
                    if event.key == pygame.K_SPACE:
                        return Action.START

            self._screen.fill(self.BG)
            font = pygame.font.Font("resources/Emulogic-zrEw.ttf", 26)
            #font1 = pygame.font.SysFont('comicsansms', 72)
            img = font.render(msg, True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (self.SCREENWIDTH/5-len(msg)/2, self.SCREENHEIGHT/3))
            img = font.render("SPACE- Try Again", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (10, self.SCREENHEIGHT-self.COMMANDS+100))
            img = font.render("ESC- Main Menu", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (10, self.SCREENHEIGHT-self.COMMANDS+150))
            pygame.display.update()
        return Action.MENU

    def draw6x6(self):
        """Function that draws the lines for a 6x6 board
        """
        pygame.draw.line(self._screen, self.DIV, [0,100], [self.SCREENWIDTH,100], 3)
        pygame.draw.line(self._screen, self.DIV, [0,200], [self.SCREENWIDTH,200], 3)
        pygame.draw.line(self._screen, self.DIV, [0,300], [self.SCREENWIDTH,300], 3)
        pygame.draw.line(self._screen, self.DIV, [0,400], [self.SCREENWIDTH,400], 3)
        pygame.draw.line(self._screen, self.DIV, [0,500], [self.SCREENWIDTH,500], 3)

        pygame.draw.line(self._screen, self.DIV, [100,0], [100,self.SCREENHEIGHT-self.COMMANDS], 3)
        pygame.draw.line(self._screen, self.DIV, [200,0], [200,self.SCREENHEIGHT-self.COMMANDS], 3)
        pygame.draw.line(self._screen, self.DIV, [300,0], [300,self.SCREENHEIGHT-self.COMMANDS], 3)
        pygame.draw.line(self._screen, self.DIV, [400,0], [400,self.SCREENHEIGHT-self.COMMANDS], 3)
        pygame.draw.line(self._screen, self.DIV, [500,0], [500,self.SCREENHEIGHT-self.COMMANDS], 3)

    def draw5x5(self):
        """Function that draws the lines for a 5x5 board
        """
        pygame.draw.line(self._screen, self.DIV, [0,120], [self.SCREENWIDTH,120], 3)
        pygame.draw.line(self._screen, self.DIV, [0,240], [self.SCREENWIDTH,240], 3)
        pygame.draw.line(self._screen, self.DIV, [0,360], [self.SCREENWIDTH,360], 3)
        pygame.draw.line(self._screen, self.DIV, [0,480], [self.SCREENWIDTH,480], 3)

        pygame.draw.line(self._screen, self.DIV, [120,0], [120,self.SCREENHEIGHT-self.COMMANDS], 3)
        pygame.draw.line(self._screen, self.DIV, [240,0], [240,self.SCREENHEIGHT-self.COMMANDS], 3)
        pygame.draw.line(self._screen, self.DIV, [360,0], [360,self.SCREENHEIGHT-self.COMMANDS], 3)
        pygame.draw.line(self._screen, self.DIV, [480,0], [480,self.SCREENHEIGHT-self.COMMANDS], 3)

    def setPieces(self, vec):
        """Function that creates the sprites for each piece and draws it in the screen

        Args:
            vec (vector): vector with the Piece objects
        """
        sprites = pygame.sprite.Group()
        if self.size == 6:
            pieceSize = 100
        else:
            pieceSize = 120
        for v in vec:
            if isinstance(v,Tower):
                sprites.add(Tower_sprite(pieceSize, v))
            elif isinstance(v,Bishop):
                sprites.add(Bishop_sprite(pieceSize, v))
            elif isinstance(v,Queen):
                sprites.add(Queen_sprite(pieceSize, v))
            elif isinstance(v,King):
                sprites.add(King_sprite(pieceSize, v))
            else:
                sprites.add(Horse_sprite(pieceSize, v))
        sprites.draw(self._screen)

    def setSnake(self, snake):
        """Function that creates the rectangles that represent the snake in the board and draws them

        Args:
            snake (object Snake): current Snake created in the game
        """
        size = snake.getBoardSize()
        if size == 5:
            space = 120
        else:
            space = 100
        for i in range(size):
            for j in range(size):
                if snake.isOcupied(i,j): 
                    pygame.draw.rect(self._screen, self.SNAKE, [space*j,space*i,space,space])


class Piece_sprite(pygame.sprite.Sprite):
    """Class that represents the chess pieces as sprites in the screen. 
    Each piece is loaded with an image representing the chess piece (King, Queen, Bishop, Tower, Horse)

    Args:
        pygame (Sprite): Superclass
    """
    _width = 0
    _height = 0
    def __init__(self, size, obj):
        super().__init__()
        self._line = obj._line
        self._col = obj._col

class Tower_sprite(Piece_sprite):
    def __init__(self, size, obj):
        super().__init__(size, obj)
        self.image = pygame.Surface([size, size])
        
        image1_not_scaled = pygame.image.load("resources/tower.png").convert_alpha()
        
        self.image = pygame.transform.scale(image1_not_scaled, [size, size])
 
        self.rect = self.image.get_rect()

        self.rect.x = self._col*size
        self.rect.y = self._line*size

class Queen_sprite(Piece_sprite):
    def __init__(self, size, obj):
        super().__init__(size, obj)
        self.image = pygame.Surface([size, size])
        
        image1_not_scaled = pygame.image.load("resources/queen.png").convert_alpha()
        
        self.image = pygame.transform.scale(image1_not_scaled, [size, size])
 
        self.rect = self.image.get_rect()

        self.rect.x = self._col*size
        self.rect.y = self._line*size

class Horse_sprite(Piece_sprite):
    def __init__(self, size, obj):
        super().__init__(size, obj)
        self.image = pygame.Surface([size, size])
        
        image1_not_scaled = pygame.image.load("resources/horse.png").convert_alpha()
        
        self.image = pygame.transform.scale(image1_not_scaled, [size, size])
 
        self.rect = self.image.get_rect()

        self.rect.x = self._col*size
        self.rect.y = self._line*size

class Bishop_sprite(Piece_sprite):
    def __init__(self, size, obj):
        super().__init__(size, obj)
        self.image = pygame.Surface([size, size])
        
        image1_not_scaled = pygame.image.load("resources/bishop.png").convert_alpha()
        
        self.image = pygame.transform.scale(image1_not_scaled, [size, size])
 
        self.rect = self.image.get_rect()

        self.rect.x = self._col*size
        self.rect.y = self._line*size

class King_sprite(Piece_sprite):
    def __init__(self, size, obj):
        super().__init__(size, obj)
        self.image = pygame.Surface([size, size])
        
        image1_not_scaled = pygame.image.load("resources/king.png").convert_alpha()
        
        self.image = pygame.transform.scale(image1_not_scaled, [size, size])
 
        self.rect = self.image.get_rect()

        self.rect.x = self._col*size
        self.rect.y = self._line*size