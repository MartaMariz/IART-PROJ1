from game import GameState
from bfs import BFS
from utils import Action

def main():
    inGame = True
    while(inGame):
        game = GameState(6, [['K',0,0], ['T',1,4]])
        choice = mainMenu(game)
        if choice == Action.SHOW:
            action = puzzleMenu(game)
            if action ==  Action.START:
                endGame = puzzle(game)
                if endGame == Action.QUIT:
                    break
            elif action == Action.BFS:
                BFS(game)
        elif choice == Action.QUIT:
            break
        

def puzzle(game):
    inGame = True
    while(inGame):
        if game.snake.endGame():
            game.gui.drawBoard(game.getSize(), game.getPieces(), game.snake)
            print("the game is over!")
            if (game.countAttacks(game.snake)):
                print("You win!!")
                return game.gui.drawFinalMsg("You win!")
            else:
                print("You loose!")
                return game.gui.drawFinalMsg("You loose!")

        pieces = game.checkPiecesNearby()
        print(pieces)
        if not game.snake.checkPossibleMoves(pieces):
            print("No moves available")
            inGame = False
        nextAction = game.gui.playPuzzle(game.getSize(), game.getPieces(), game.snake)
        if nextAction == Action.QUIT:
            print("bye!")
            inGame = False
        elif nextAction == Action.BFS:
            BFS(game)
            
        else:
            if (game.evalMove(nextAction, game.snake)):
                game.snake.updateSnake(nextAction)

def puzzleMenu(game):
    return game.gui.puzzleMenu(game.getSize(), game.getPieces(), game.snake)

def mainMenu(game):
    return game.gui.mainMenu()

main()