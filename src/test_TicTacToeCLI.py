from TicTacToeCLI import *
from TicTacToeGUI import TicTacToeGUI
from pytest import *

game = TicTacToeGUI()

def test_empty_grid():
    assert empty_grid == [['','',''],['','',''],['','','']]

