from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QIcon, QFont
from PyQt5.QtCore import Qt, QPoint, QUrl

from src.TicTacToeGUI import TicTacToeGUI
from src.syntax import *
from src.get_name_of_function import get_name_of_function

from os.path import exists
from os import remove

from src.test import check_for_errors

class MainWindow(QMainWindow):
    """
    A window wrapper to manage the interaction between all the widgets.
        game : the GUI of the game;
        inst : the widget where are displayed lesson and instructions;
        code : the widget where the user writes code;
        output : the widget where are displayed the errors.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(MainWindow, self).__init__()
        self.setWindowTitle("Learn Python by coding a game - Tic Tac Toe")
        self.level = 1; self.level_max = 1; self.nbr_level = 11
        self.submitted_functions = {1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:'', 10:'', 11:''}

        stylesheet_path='src/res/darkorange.stylesheet'
        with open(stylesheet_path,"r") as fh:
            self.setStyleSheet(fh.read())
        self.setWindowIcon(QIcon("src/res/app.ico"))

        ## SLOTS

        def show_popup(string):
            """
            Show popup at the end of the Tic Tac Toe game. 
            """
            dialog = QMessageBox()
            if string in ['O','X', "???"] :
                dialog.setWindowTitle("Victory")
                dialog.setText("The game is over !\nCongrates player %s : you win !" % string)
            else:
                dialog.setWindowTitle("Draw")
                dialog.setText("The game is over !\nIt's a draw, try again !")

            dialog.setModal(True)
            dialog.exec()
            game.reset()

        def load_level():
            """
            Load the level (i.e. lesson and user code) and update UI. 
            """
            inst.setSource(QUrl("file:src/res/lesson/%d.html" % self.level))
            next_lesson_button.setEnabled(self.level < self.level_max)
            code.setText(self.submitted_functions[self.level])
            game.change_level(self.level + 1 if self.level < self.level_max else self.level)
            output.clear()

        def go_to_next_lesson():
            """
            Slot to go to the next lesson.
            """
            self.level = min(self.nbr_level, self.level + 1)
            print(self.level)
            load_level()

        def go_to_previous_lesson():
            """
            Slot to go to the previous lesson.
            """
            self.level = max(1, self.level - 1)
            load_level()

        def submit_text():
            """
            Slot to submit code and to test it. 
            """
            user_code, name = get_name_of_function(code.toPlainText())
            ancient_code = ''
            for i in range(1,self.level):
                ancient_code += '\t'
                ancient_code += self.submitted_functions[i]
                ancient_code += '\n'

            with open("src/function_to_test/function_to_test.py", "w") as fichier:
                fichier.write('def function(L):\n' + ancient_code + '\t' + user_code + '\treturn (' + name + '(*L))' )
            
            no_errors, msg  = check_for_errors(str(self.level))
            if no_errors:
                if self.level == self.level_max:
                    self.level_max +=1
                next_lesson_button.setEnabled(no_errors)
                self.submitted_functions[self.level] = user_code
                load_level()
            output.setText(msg)

        ## LEFT LAYOUT
        # The game
        game = TicTacToeGUI()
        game.ended.connect(show_popup)

        # Reset button
        reset_button = QPushButton("Reset", self)
        reset_button.setFixedWidth(150)
        reset_button.clicked.connect(game.reset)

        # The lesson + instructions
        inst = QTextBrowser()
        inst.adjustSize()
        inst.setStyleSheet("background-color: rgb(240, 240, 240); border: none;")

        # Previous lesson button
        previous_lesson_button = QPushButton("Previous lesson",self)
        previous_lesson_button.setFixedWidth(150)
        previous_lesson_button.clicked.connect(go_to_previous_lesson)

        # Layout to arrange all of it
        lay_left = QVBoxLayout()
        lay_left.addWidget(game); lay_left.setAlignment(game, Qt.AlignHCenter)
        lay_left.addWidget(reset_button); lay_left.setAlignment(reset_button, Qt.AlignHCenter)
        lay_left.addWidget(inst)
        lay_left.addWidget(previous_lesson_button)


        ## RIGHT LAYOUT
        # The text field to insert the code
        font = QFont();
        font.setFamily("Courier");
        font.setStyleHint(QFont.Monospace);
        font.setFixedPitch(True);
        font.setPointSize(13);

        code = QTextEdit()
        code.setFont(font)
        code.setTabStopDistance(32)
        code.setStyleSheet("color: rgb(255,255,255); background-color: rgb(40, 41, 35);")
        PythonHighlighter(code)

        # The errors + congrats
        output = QTextBrowser()
        output.setMaximumHeight(100)
        output.setFont(font)
        output.setStyleSheet("color: #b05656; background-color: rgb(40, 41, 35);")

        # Next lesson button
        next_lesson_button = QPushButton("Next lesson",self)
        next_lesson_button.setEnabled(self.level<self.level_max)
        next_lesson_button.setFixedWidth(150)
        next_lesson_button.clicked.connect(go_to_next_lesson)

        # Submit text button
        submit_button = QPushButton("Submit code",self)
        submit_button.clicked.connect(submit_text)
        submit_button.setFixedWidth(150)

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
    
    def closeEvent(self, event):
        path = "src/function_to_test/function_to_test.py"
        if exists(path): remove(path)