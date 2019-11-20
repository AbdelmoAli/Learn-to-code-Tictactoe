from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QIcon
from PyQt5.QtCore import Qt, QPoint, QUrl

from src.TicTacToeGUI import TicTacToeGUI
from src.syntax import *
from src.modify_function import read_and_modify_function

from src.test import check_for_errors

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Learn Python by coding a game - Tic Tac Toe")
        self.level = 1; self.level_max = 1; self.nbr_level = 11
        

        ## SLOTS
        def show_popup(string):
            dialog = QMessageBox()
            if string in ['O','X', "???"] :
                dialog.setWindowTitle("Victory")
                dialog.setText("The game is over !\nCongrates player %s : you win !" % string)
            else:
                dialog.setWindowTitle("Drawn")
                dialog.setText("The game is over !\nIt's a drawn, try again !")

            dialog.setModal(True)
            dialog.exec()
            game.reset()

        def load_level():
            inst.setSource(QUrl("file:src/res/lesson/%d.html" % self.level))
            code.setText('')
            if self.level < self.level_max : next_lesson_button.setEnabled(True) # "or True"  FOR DEBUGING PURPOSE
            else : next_lesson_button.setEnabled(False)

            game.change_level(self.level)

            # Manage levels in test -- TODO

        def go_to_next_lesson():
            self.level = min(self.nbr_level, self.level + 1)
            self.level_max = max(self.level, self.level_max)
            next_lesson_button.setEnabled(self.level<self.level_max)
            output.clear()
            load_level()

        def go_to_previous_lesson():
            self.level = max(1, self.level - 1)
            load_level()

        def submit_text():
            user_code, name = read_and_modify_function(code.toPlainText())

            with open("src/submitted_files/function_to_test.py", "w") as fichier:
                fichier.write('def function(L):\n\t' + user_code + '\treturn (' + name + '(*L))' )
                
            b, msg  = check_for_errors(str(self.level))
            if b and self.level == self.level_max:
                self.level_max +=1
                next_lesson_button.setEnabled(b)
            output.setText(msg)

        ## LEFT LAYOUT
        # The game
        game = TicTacToeGUI()
        game.ended.connect(show_popup)

        # Reset button
        reset_button = QPushButton("Reset", self)
        reset_button.clicked.connect(game.reset)

        # The lesson + instructions
        inst = QTextBrowser()
        inst.adjustSize()
        inst.setStyleSheet("background-color: rgb(240, 240, 240); border: none;")

        # Previous lesson button
        previous_lesson_button = QPushButton("Previous lesson",self)
        previous_lesson_button.setMaximumWidth(150)
        previous_lesson_button.clicked.connect(go_to_previous_lesson)

        # Layout to arrange all of it
        lay_left = QVBoxLayout()
        lay_left.addWidget(game); lay_left.setAlignment(game, Qt.AlignHCenter)
        lay_left.addWidget(reset_button)
        lay_left.addWidget(inst)
        lay_left.addWidget(previous_lesson_button)


        ## RIGHT LAYOUT
        # The text field to insert the code
        code = QTextEdit()
        code.setTabStopDistance(23)
        # code.setHtml(html_code)
        # code.setTextColor(QColor(Qt.white))
        PythonHighlighter(code)

        # The errors + congrats
        output = QTextBrowser()
        output.setStyleSheet("background-color: rgb(200, 200, 200);")

        # Next lesson button
        next_lesson_button = QPushButton("Next lesson",self)
        next_lesson_button.setEnabled(self.level<self.level_max)
        next_lesson_button.setMaximumWidth(150)
        next_lesson_button.clicked.connect(go_to_next_lesson)

        # Submit text button
        submit_button = QPushButton("Submit code",self)
        submit_button.clicked.connect(submit_text)
        submit_button.setMaximumWidth(150)

        # Layout to arrange all of it
        lay_right = QVBoxLayout()
        lay_right = QVBoxLayout()
        lay_right.addWidget(code)
        lay_right.addWidget(submit_button, Qt.AlignRight)
        lay_right.addWidget(output)
        lay_right.addWidget(next_lesson_button)
        lay_right.setAlignment(submit_button, Qt.AlignRight)
        lay_right.setAlignment(next_lesson_button, Qt.AlignRight)


        ## GLOBAL LAYOUT
        lay_global = QHBoxLayout()
        lay_global.addLayout(lay_left)
        lay_global.addLayout(lay_right)
        widget = QWidget()
        widget.setLayout(lay_global)

        load_level()
        self.setCentralWidget(widget)

