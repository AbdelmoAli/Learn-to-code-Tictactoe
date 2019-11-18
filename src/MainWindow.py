from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint

from src.TicTacToeGUI import TicTacToeGUI

import lorem

html_string = """\
<h1> Titre H1 </h1>
<h2> Titre H2 </h2>
<h3> Titre H3 </h3>
<h4> Titre H4 </h4>
<h5> Titre H5 </h5>
<pre>
    print("Hello World !") 
    print("Working f****** well !")
</pre>
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Learn Python by coding a game - Tic Tac Toe")

        # The game
        game = TicTacToeGUI()

        # The lesson + instructions
        inst = QTextEdit()
        inst.setReadOnly(True)
        inst.setHtml(html_string + lorem.text())

        # The text field to insert the code
        code = QTextEdit()
        # code.append("HERE the code to be edited")
        code.append(lorem.text())

        # Layout to arrange all of it
        lay_left = QVBoxLayout()
        lay_left.addWidget(game)
        lay_left.setAlignment(game, Qt.AlignHCenter)
        lay_left.addWidget(inst)

        lay_right = QVBoxLayout()
        # TODO TEST BUTTON

        lay_global = QHBoxLayout()
        lay_global.addLayout(lay_left)
        lay_global.addWidget(code)

        widget = QWidget()
        widget.setLayout(lay_global)
        self.setCentralWidget(widget)