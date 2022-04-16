from game import GameState
from search import Search
from utils import Action, ALGORITHM

def main():
    inGame = True
    while(inGame):
        game = GameState(5, [['Q',0,0], ['T',1,4]])
        search = Search(game)
        choice = mainMenu(game)
        if choice == Action.SHOW:
            action = puzzleMenu(game)
            if action ==  Action.START:
                endGame = puzzle(game, search)
                if endGame == Action.QUIT:
                    break
            elif action == Action.BFS:
                search.beginSearch(ALGORITHM.BFS)
            elif action == Action.UCOST:
                search.beginSearch(ALGORITHM.UCOST)
            elif action == Action.GS1:
                search.beginSearch(ALGORITHM.GS1)
            elif action == Action.AS1:
                search.beginSearch(ALGORITHM.As1)
            elif action == Action.AS2:
                search.beginSearch(ALGORITHM.As2)

        elif choice == Action.QUIT:
            break
        

def puzzle(game, search):
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
            search.beginSearch(ALGORITHM.BFS)
        elif nextAction == Action.UCOST:
            search.beginSearch(ALGORITHM.UCOST)
        elif nextAction == Action.GS1:
            search.beginSearch(ALGORITHM.GS1)
        elif nextAction == Action.AS1:
            search.beginSearch(ALGORITHM.As1)
        elif nextAction == Action.AS2:
            search.beginSearch(ALGORITHM.As2)
            
        else:
            if (game.evalMove(nextAction, game.snake)):
                game.snake.updateSnake(nextAction)

def puzzleMenu(game):
    return game.gui.puzzleMenu(game.getSize(), game.getPieces(), game.snake)

def mainMenu(game):
    return game.gui.mainMenu()

main()