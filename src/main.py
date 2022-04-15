from game import GameState
from bfs import BFS
from utils import Action

def main():
    game = GameState(5, [['Q',0,0], ['T',1,4 ]])

    inGame = True
    while(inGame):
        if game.snake.endGame():
            print("the game is over!")
            if (game.CountAttacks(game.snake)):
                    print("You win!!")
            else:
                    print("You loose!")
            inGame = False
            game.gui.showboard(game.getSize(), game.getPieces(), game.snake)
        pieces = game.checkPiecesNearby()
        print(pieces)
        if not game.snake.checkPossibleMoves(pieces):
            print("No moves available")
            inGame = False
        nextAction = game.gui.showboard(game.getSize(), game.getPieces(), game.snake)
        if nextAction == Action.QUIT:
            print("bye!")
            inGame = False
        elif nextAction == Action.BFS:
            BFS(game)
            
        else:
            if (game.evalMove(nextAction, game.snake)):
                game.snake.updateSnake(nextAction)

main()