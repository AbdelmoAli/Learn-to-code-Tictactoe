from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QIcon
from PyQt5.QtCore import Qt, QPoint, QUrl, pyqtSlot

from src.TicTacToeGUI import TicTacToeGUI
from src.syntax import *

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

html_code = """\
<body bgcolor="#1E1E1E">
</body>

"""

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Learn Python by coding a game - Tic Tac Toe")
        # LEFT LAYOUT

        # The game
        game = TicTacToeGUI()

        # The lesson + instructions
        inst = QTextBrowser()
        inst.setStyleSheet("background-color: rgb(240, 240, 240); border: none;")
        inst.setSource(QUrl("file:src/res/lesson1.htm"))

        # Layout to arrange all of it
        lay_left = QVBoxLayout()
        lay_left.addWidget(game)
        lay_left.setAlignment(game, Qt.AlignHCenter)
        lay_left.addWidget(inst, Qt.AlignHCenter)

        # RIGHT LAYOUT

        # The text field to insert the code
        code = QTextEdit()
        code.setHtml(html_code)
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

        #GLOBAL LAYOUT

        lay_global = QHBoxLayout()
        
        lay_global.addLayout(lay_left)
        lay_global.addLayout(lay_right)

        widget = QWidget()
        widget.setLayout(lay_global)
        self.setCentralWidget(widget)