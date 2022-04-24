from game import GameState
from search import Search
from utils import Action, ALGORITHM
import random

def main():
    inGame = True
    pieces = [['Q',0,0], ['T',1,4]]
    game = GameState(5, pieces)

    while(inGame):
        choice = mainMenu(game)

        if choice == Action.SHOWH or choice == Action.SHOWE:
            if choice == Action.SHOWH:
                del game, pieces
                pieces = prepare_game(6)
                print(pieces)
                game = GameState(6, pieces)
            elif choice == Action.SHOWE:
                del game, pieces
                pieces = prepare_game(5)
                game = GameState(5, pieces)

            search = Search(game)
            action = puzzleMenu(game)
            if action == Action.START:
                endGame = puzzle(game, search)
                if endGame == Action.QUIT:
                    break
                elif endGame == Action.MENU:
                    continue
            elif action == Action.MENU:
                continue
            else:
                if action == Action.BFS:
                    result = search.beginSearch(ALGORITHM.BFS)
                elif action == Action.UCOST:
                    result = search.beginSearch(ALGORITHM.UCOST)
                elif action == Action.GS1:
                    result = search.beginSearch(ALGORITHM.GS1)
                elif action == Action.AS1:
                     result = search.beginSearch(ALGORITHM.As1)
                elif action == Action.AS2:
                     result = search.beginSearch(ALGORITHM.As2)        
                print(result)
                if result == Action.LOST:
                    return game.gui.drawFinalMsg("You lose!")
                else: 
                    action = game.gui.showResult(game.getSize(), game.getPieces(), result)
                    if action == Action.MENU:
                        continue

            
        elif choice == Action.RULES:
            action = rules(game) 
        elif choice == Action.QUIT:
            break
        if action == Action.QUIT:
                break
        

def puzzle(game, search):
    inGame = True
    while(inGame):
        if game.snake.endGame():
            game.gui.drawBoard(game.getSize(), game.getPieces(), game.snake)
            if (game.countAttacks(game.snake)):
                print("You win!")
                return game.gui.drawFinalMsg("You win!")
            else:
                print("You lose!")
                return game.gui.drawFinalMsg("You lose!")

        pieces = game.checkPiecesNearby()
        if not game.snake.checkPossibleMoves(pieces):
            return game.gui.drawFinalMsg("No movements left!")
        nextAction = game.gui.playPuzzle(game.getSize(), game.getPieces(), game.snake)
        if nextAction == Action.QUIT:
            return Action.QUIT
        elif nextAction == Action.MENU:
            return Action.MENU
        elif nextAction == Action.AS1:
            result = search.beginSearch(ALGORITHM.As1)
            print(result)
            if result == Action.LOST:
                return game.gui.drawFinalMsg("You lose!")
            else: return game.gui.showResult(game.getSize(), game.getPieces(), result)
            
        else:
            if (game.evalMove(nextAction, game.snake)):
                game.snake.updateSnake(nextAction)

def rules(game):
    return game.gui.rules()

def puzzleMenu(game):
    return game.gui.puzzleMenu(game.getSize(), game.getPieces(), game.snake)

def mainMenu(game):
    return game.gui.mainMenu()

def prepare_game(level):
    boards = {
        "board1": [['T', 1, 1], ['K', 1, 3]],
        "board2": [['B', 2, 1], ['H', 1, 4]],
        "board3": [['Q', 0, 0], ['T', 1, 4]],
        "board4": [['B', 1, 1], ['K', 2, 2]],
        "board5": [['Q', 1, 1], ['H', 3, 4]],
        "board6": [['B', 2, 4], ['T', 4, 3]],
        "board7": [['H', 3, 1], ['K', 4, 3]],
        "board8": [['B', 4, 1], ['Q', 1, 2]],
        "board9": [['T', 4, 3], ['H', 4, 4]],
        "board10": [['K', 1, 0], ['Q', 1, 4]],
        "board11": [['B', 4, 1], ['T', 1, 5], ['Q', 5, 5]],
        "board12": [['T', 0, 3], ['H', 3, 3], ['K', 2, 4]],
        "board13": [['B', 4, 1], ['H', 1, 2], ['Q', 4, 4]],
        "board14": [['Q', 2, 0], ['T', 5, 1], ['K', 4, 3]],
        "board15": [['B', 0, 2], ['T', 4, 3], ['K', 1, 5]],
        "board16": [['Q', 3, 0], ['H', 3, 3], ['T', 2, 4]],
        "board17": [['K', 3, 0], ['H', 2, 4], ['B', 4, 3]],
        "board18": [['Q', 1, 1], ['B', 4, 1], ['K', 3, 4]],
        "board19": [['B', 0, 2], ['H', 2, 1], ['T', 4, 4]],
        "board20": [['H', 1, 2], ['K', 2, 3], ['Q', 2, 5]]
    }

    if level == 5:
        number_board = random.randint(1, 10)
    if level == 6:
        number_board = random.randint(11, 20)

    pieces = boards["board"+str(number_board)]
    print(pieces)

    return pieces

main()
