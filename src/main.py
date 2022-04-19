from game import GameState
from search import Search
from utils import Action, ALGORITHM


def main():
    inGame = True
    pieces = [['Q',0,0], ['T',1,4]]
    game = GameState(5, pieces)
    while(inGame):
        choice = mainMenu(game)

        if choice == Action.SHOWH or choice == Action.SHOWE:
            if choice == Action.SHOWH:
                del game, pieces
                pieces = [['Q',0,0], ['T',1,4], ['H',3,2]]
                game = GameState(6, pieces)
            elif choice == Action.SHOWE:
                del game, pieces
                pieces = [['Q',0,0], ['T',1,4]]
                game = GameState(5, pieces)

            search = Search(game)
            action = puzzleMenu(game)
            if action ==  Action.START:
                endGame = puzzle(game, search)
                if endGame == Action.QUIT:
                    break
            else:
                if action == Action.BFS:
                    sol = search.beginSearch(ALGORITHM.BFS)
                elif action == Action.UCOST:
                    sol = search.beginSearch(ALGORITHM.UCOST)
                elif action == Action.GS1:
                    sol = search.beginSearch(ALGORITHM.GS1)
                elif action == Action.AS1:
                    sol = search.beginSearch(ALGORITHM.As1)
                elif action == Action.AS2:
                    sol = search.beginSearch(ALGORITHM.As2)
                game.gui.playPuzzle(game.getSize(), game.getPieces(), sol)  
          
        elif choice == Action.RULES:
            action = rules(game)
        elif choice == Action.QUIT:
            break
        

def puzzle(game, search):
    inGame = True
    sol =  search.beginSearch(ALGORITHM.BFS)  
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
        else:
            if (game.evalMove(nextAction, game.snake)):
                game.snake.updateSnake(nextAction)

def rules(game):
    return game.gui.rules()

def puzzleMenu(game):
    print(game.getPieces())
    return game.gui.puzzleMenu(game.getSize(), game.getPieces(), game.snake)

def mainMenu(game):
    return game.gui.mainMenu()

main()