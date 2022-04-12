from piece import Bishop, Tower, Queen, Horse
from snake import Snake
from utils import Action
import pygame


class GUI:
    _BG = (0,0,0)
    _DIV = (255,255,255)
    _SNAKE = (2, 90, 22)
    SCREENWIDTH = 600
    SCREENHEIGHT = 600
    
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((self.SCREENWIDTH,self.SCREENHEIGHT))


    def showboard(self, size, pieces, snake):
        clock=pygame.time.Clock()
        global inGame
        inGame = True
        while inGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    inGame = False
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                if snake.up():
                    print("up")
                    return Action.UP
            #if keys[pygame.K_RIGHT]:
            #    if right():

            self._screen.fill(self._BG)
            self.size = size
            if size == 4:
                self.draw4x4()
            else:
                self.draw5x5()

            self.setPieces(pieces)
            self.setSnake(snake)
            
            pygame.display.flip()

            clock.tick(50)

        pygame.quit()
        return Action.QUIT
            


    def draw4x4(self):
        pygame.draw.line(self._screen, self._DIV, [0,150], [self.SCREENWIDTH,150], 3)
        pygame.draw.line(self._screen, self._DIV, [0,300], [self.SCREENWIDTH,300], 3)
        pygame.draw.line(self._screen, self._DIV, [0,450], [self.SCREENWIDTH,450], 3)

        pygame.draw.line(self._screen, self._DIV, [150,0], [150,self.SCREENHEIGHT], 3)
        pygame.draw.line(self._screen, self._DIV, [300,0], [300,self.SCREENHEIGHT], 3)
        pygame.draw.line(self._screen, self._DIV, [450,0], [450,self.SCREENHEIGHT], 3)

    def draw5x5(self):
        pygame.draw.line(self._screen, self._DIV, [0,120], [self.SCREENWIDTH,120], 3)
        pygame.draw.line(self._screen, self._DIV, [0,240], [self.SCREENWIDTH,240], 3)
        pygame.draw.line(self._screen, self._DIV, [0,360], [self.SCREENWIDTH,360], 3)
        pygame.draw.line(self._screen, self._DIV, [0,480], [self.SCREENWIDTH,480], 3)

        pygame.draw.line(self._screen, self._DIV, [120,0], [120,self.SCREENHEIGHT], 3)
        pygame.draw.line(self._screen, self._DIV, [240,0], [240,self.SCREENHEIGHT], 3)
        pygame.draw.line(self._screen, self._DIV, [360,0], [360,self.SCREENHEIGHT], 3)
        pygame.draw.line(self._screen, self._DIV, [480,0], [480,self.SCREENHEIGHT], 3)

    def setPieces(self, vec):
        sprites = pygame.sprite.Group()
        if self.size == 4:
            pieceSize = 150
        else:
            pieceSize = 120
        for v in vec:
            if isinstance(v,Tower):
                sprites.add(Tower_sprite(pieceSize, v))
            elif isinstance(v,Bishop):
                sprites.add(Bishop_sprite(pieceSize, v))
            elif isinstance(v,Queen):
                sprites.add(Queen_sprite(pieceSize, v))
            else:
                sprites.add(Horse_sprite(pieceSize, v))
        sprites.draw(self._screen)
        pygame.display.flip()

    def setSnake(self, snake):
        if len(snake.bitmap) == 5:
            space = 120
        else:
            space = 150
        for i in range(len(snake.bitmap)):
            for j in range(len(snake.bitmap[i])):
                if snake.bitmap[i][j]: 
                    pygame.draw.rect(self._screen, self._SNAKE, [space*j,space*i,space,space])



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