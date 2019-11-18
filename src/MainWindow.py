from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QIcon
from PyQt5.QtCore import Qt, QPoint, QUrl

from src.TicTacToeGUI import TicTacToeGUI
from src.syntax import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Learn Python by coding a game - Tic Tac Toe")
        
        def show_popup(string):
            dialog = QMessageBox()
            if string in ['O','X'] :
                dialog.setWindowTitle("Victory")
                dialog.setText("The game is over !\nCongrates player %s : you win !" % string)
            else:
                dialog.setWindowTitle("Drawn")
                dialog.setText("The game is over !\nIt's a drawn, try again !")

            dialog.setModal(True)
            dialog.exec()
            game.reset()

        ## LEFT LAYOUT
        # The game
        game = TicTacToeGUI()
        game.ended.connect(show_popup)

        # The lesson + instructions
        inst = QTextBrowser()
        inst.setStyleSheet("background-color: rgb(240, 240, 240); border: none;")
        inst.setSource(QUrl("file:src/res/lesson1.htm"))

        # Layout to arrange all of it
        lay_left = QVBoxLayout()
        lay_left.addWidget(game)
        lay_left.setAlignment(game, Qt.AlignHCenter)
        lay_left.addWidget(inst, Qt.AlignHCenter)

        ## RIGHT LAYOUT
        # The text field to insert the code
        code = QTextEdit()
        code.setTextColor(QColor(Qt.white))
        highlight = PythonHighlighter(code)

        # Function to write in fichier.py
        def submit_text(self):
            fichier = open("src/submitted_files/file.py", "w")
            fichier.write(code.toPlainText())
            fichier.close()

        # Button to submit text -> fichier.py
        submit_button = QPushButton("Submit code",self)
        submit_button.clicked.connect(submit_text)

        # Layout to arrange all of it
        lay_right = QVBoxLayout()
        lay_right = QVBoxLayout()
        lay_right.addWidget(code)
        lay_right.addWidget(submit_button)

        ##GLOBAL LAYOUT
        lay_global = QHBoxLayout()
        
        lay_global.addLayout(lay_left)
        lay_global.addLayout(lay_right)

        widget = QWidget()
        widget.setLayout(lay_global)
        self.setCentralWidget(widget)