from piece import Bishop, Tower, Queen, Horse, King
from utils import Action
import pygame
import pygame.freetype

class GUI:
    BG = (0,0,0)
    DIV = (255,255,255)
    SNAKE = (188,186,205)
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
        inMenu = True
        while (inMenu):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("sai")
                    inMenu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        return Action.SHOWE
                    if event.key == pygame.K_h:
                        return Action.SHOWH
                    if event.key == pygame.K_r:
                        return Action.RULES
                    elif event.key == pygame.K_ESCAPE:
                        inMenu = False
            self._screen.fill(self.BG)
            background_image = pygame.image.load("images/stars.jpeg")
            self._screen.blit(background_image, (0, 0))
            font = pygame.font.SysFont('comicsansms', 48)
            font1 = pygame.font.SysFont('comicsansms', 72)
            img = font1.render("Chess Snake Puzzles", True, self.MENU_TITLE, self.MENU_BOX)
            self._screen.blit(img, (20, 100))
            img = font.render("Press E to see easy puzzle", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (20, self.SCREENHEIGHT-self.COMMANDS+110))
            img = font.render("Press H to see hard puzzle", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (20, self.SCREENHEIGHT-self.COMMANDS+140))
            img = font.render("Press R to see rules", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (20, self.SCREENHEIGHT-self.COMMANDS+170))
            img = font.render("Press ESC to quit", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (20, self.SCREENHEIGHT-self.COMMANDS+200))
            pygame.display.update()
        return Action.QUIT

    def rules(self):
        inRules = True
        while (inRules):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("sai")
                    inRules = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        inRules = False
            self._screen.fill(self.BG)
            font = pygame.font.SysFont('comicsansms', 48)

            text_file = open("docs/rules.txt", "r")
            rules = text_file.read()

            font1 = pygame.freetype.SysFont('comicsansms', 24)
            word_wrap(self._screen, rules, font1, self.MENU_FONT)
            #img = font.render(rules, True, self.MENU_FONT, self.MENU_BOX)
            #self._screen.blit(img, (20, 20))
            img = font.render("Press SPACE to main menu", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (20, self.SCREENHEIGHT-self.COMMANDS+200))
            pygame.display.update()
        return Action.QUIT


    def playPuzzle(self, size, pieces, snake):
        global inGame
        inGame = True
        while inGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    inGame = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inGame = False
                    if event.key == pygame.K_UP:
                        if snake.up():
                            print("up")
                            return Action.UP
                    if event.key == pygame.K_DOWN:
                        if snake.down():
                            print("down")
                            return Action.DOWN
                    if event.key == pygame.K_LEFT:
                        if snake.left():
                            print("left")
                            return Action.LEFT    
                    if event.key == pygame.K_RIGHT:
                        if snake.right():
                            print("right")
                            return Action.RIGHT
                    if event.key == pygame.K_SPACE:
                        return Action.AS1

            self.drawBoard(size, pieces, snake)
            font = pygame.font.SysFont(None, 48)
            img = font.render("Press SPACE to solve puzzle", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+20))
            img = font.render("Press ESC to Main Menu", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+50))
            pygame.display.update()

        return Action.QUIT

    def puzzleMenu(self, size, pieces, snake):
        print(pieces)
        inDisplay = True
        while inDisplay:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    inDisplay = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inDisplay = False
                    if event.key == pygame.K_1:
                        return Action.BFS
                    if event.key == pygame.K_2:
                        return Action.UCOST
                    if event.key == pygame.K_3:
                        return Action.GS1
                    if event.key == pygame.K_5:
                        return Action.AS1
                    if event.key == pygame.K_6:
                        return Action.AS2
                    elif event.key == pygame.K_s:
                        return Action.START

            self.drawBoard(size, pieces, snake)
            font = pygame.font.SysFont(None, 36)
            font1 = pygame.font.SysFont(None, 48)
            img = font1.render("Press S to start game", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS))
            img = font.render("Press number to solve with each algorithm:", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+40))
            img = font.render("1 - BFS", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+70))
            img = font.render("2 - uniform cost", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+100))
            img = font.render("3 - greedy search", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+130))
            img = font.render("5 - A* - Manhattan distance", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+160))
            img = font.render("6 - A* - Diff between number of attacks", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+190))
            img = font.render("Press ESC to main menu", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (0, self.SCREENHEIGHT-self.COMMANDS+220))
            pygame.display.update()

        return Action.QUIT    

    def drawBoard(self, size, pieces, snake):
        self._screen.fill(self.BG)
        self.size = size
        if size == 6:
            self.draw6x6()
        else:
            self.draw5x5()

        self.setPieces(pieces)
        self.setSnake(snake)


    def drawFinalMsg(self, msg):
        inMsg = True
        while (inMsg):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    inMsg = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return Action.MENU

            self._screen.fill(self.BG)
            font = pygame.font.SysFont(None, 48)
            #font1 = pygame.font.SysFont('comicsansms', 72)
            img = font.render(msg, True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (20, 20))
            img = font.render("Press ESC to main menu", True, self.MENU_FONT, self.MENU_BOX)
            self._screen.blit(img, (20, self.SCREENHEIGHT-self.COMMANDS+150))
            pygame.display.update()
        return Action.QUIT

    def draw6x6(self):
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
        pygame.draw.line(self._screen, self.DIV, [0,120], [self.SCREENWIDTH,120], 3)
        pygame.draw.line(self._screen, self.DIV, [0,240], [self.SCREENWIDTH,240], 3)
        pygame.draw.line(self._screen, self.DIV, [0,360], [self.SCREENWIDTH,360], 3)
        pygame.draw.line(self._screen, self.DIV, [0,480], [self.SCREENWIDTH,480], 3)

        pygame.draw.line(self._screen, self.DIV, [120,0], [120,self.SCREENHEIGHT-self.COMMANDS], 3)
        pygame.draw.line(self._screen, self.DIV, [240,0], [240,self.SCREENHEIGHT-self.COMMANDS], 3)
        pygame.draw.line(self._screen, self.DIV, [360,0], [360,self.SCREENHEIGHT-self.COMMANDS], 3)
        pygame.draw.line(self._screen, self.DIV, [480,0], [480,self.SCREENHEIGHT-self.COMMANDS], 3)

    def setPieces(self, vec):
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
        
        image1_not_scaled = pygame.image.load("images/tower.png").convert_alpha()
        
        self.image = pygame.transform.scale(image1_not_scaled, [size, size])
 
        self.rect = self.image.get_rect()

        self.rect.x = self._col*size
        self.rect.y = self._line*size

class Queen_sprite(Piece_sprite):
    def __init__(self, size, obj):
        super().__init__(size, obj)
        self.image = pygame.Surface([size, size])
        
        image1_not_scaled = pygame.image.load("images/queen.png").convert_alpha()
        
        self.image = pygame.transform.scale(image1_not_scaled, [size, size])
 
        self.rect = self.image.get_rect()

        self.rect.x = self._col*size
        self.rect.y = self._line*size

class Horse_sprite(Piece_sprite):
    def __init__(self, size, obj):
        super().__init__(size, obj)
        self.image = pygame.Surface([size, size])
        
        image1_not_scaled = pygame.image.load("images/horse.png").convert_alpha()
        
        self.image = pygame.transform.scale(image1_not_scaled, [size, size])
 
        self.rect = self.image.get_rect()

        self.rect.x = self._col*size
        self.rect.y = self._line*size

class Bishop_sprite(Piece_sprite):
    def __init__(self, size, obj):
        super().__init__(size, obj)
        self.image = pygame.Surface([size, size])
        
        image1_not_scaled = pygame.image.load("images/bishop.png").convert_alpha()
        
        self.image = pygame.transform.scale(image1_not_scaled, [size, size])
 
        self.rect = self.image.get_rect()

        self.rect.x = self._col*size
        self.rect.y = self._line*size

class King_sprite(Piece_sprite):
    def __init__(self, size, obj):
        super().__init__(size, obj)
        self.image = pygame.Surface([size, size])
        
        image1_not_scaled = pygame.image.load("images/king.png").convert_alpha()
        
        self.image = pygame.transform.scale(image1_not_scaled, [size, size])
 
        self.rect = self.image.get_rect()

        self.rect.x = self._col*size
        self.rect.y = self._line*size

def word_wrap(surf, text, font, color=(0, 0, 0)):
    font.origin = True
    words = text.split(' ')
    width, height = surf.get_size()
    line_spacing = font.get_sized_height() + 2
    x, y = 0, line_spacing
    space = font.get_rect(' ')
    for word in words:
        bounds = font.get_rect(word)
        if x + bounds.width + bounds.x >= width:
            x, y = 0, y + line_spacing
        if x + bounds.width + bounds.x >= width:
            raise ValueError("word too wide for the surface")
        if y + bounds.height - bounds.y >= height:
            raise ValueError("text to long for the surface")
        font.render_to(surf, (x, y), None, color)
        x += bounds.width + space.width
    return x, y