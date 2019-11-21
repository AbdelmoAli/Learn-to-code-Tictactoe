from TicTacToeCLI import *
from pytest import *

game = TicTacToeCLI()

def test_empty_grid():
    assert game.empty_grid() == [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def test_reset():
    game.reset()
    assert game.grid == [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 

def test_switch_mark():
    assert game.mark == 'O'
    game.switch_mark()
    assert game.mark == 'X'

def test_value():
    assert game.value(1, 1) == ' '
    game.grid[1][1] = 'X'
    assert game.value(1, 1) == 'X'

def test_is_empty():
    game.grid[1][1] = 'X'
    assert game.is_empty(1,1) == False
    game.grid[1][1] = ' '
    assert game.is_empty(1,1) == True

def test_is_fulle():
    assert game.is_full() == False
    game.grid = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
    assert game.is_full() == True

def test_add_mark():
    game = TicTacToeCLI()
    assert game.add_mark(1,1) == True
    assert game.grid[1][1] == 'O'
    assert game.add_mark(1,1) == False

def test_get_rows():
    game = TicTacToeCLI()
    game.grid = [['O',' ',' '],[' ','X',' '],['O',' ','O']]
    assert sorted(game.get_rows()) == sorted([ ['O',' ',' '], [' ','X',' '], ['O',' ','O'], ['O',' ','O'], [' ','X',' '], [' ',' ','O'], ['O','X','O'], [' ','X','O'] ])

def test_is_align():
    assert game.is_align(['X', 'X', 'X']) == True
    assert game.is_align(['X', 'X', 'O']) == False

def test_has_winner():
    game = TicTacToeCLI()
    assert game.has_winner() == False
    game.grid[0] = ['X', 'X', 'X']
    assert game.has_winner() == True

def test_get_winner():
    game = TicTacToeCLI()
    assert game.get_winner() == None
    game.grid[0] = ['X', 'X', 'X']
    assert game.get_winner() == 'X'

