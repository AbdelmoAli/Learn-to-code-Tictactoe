from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint
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

class Game(QWidget):
    def __init__(self):
        super(Game, self).__init__()
        self.setFixedSize(180,180)
        self.circle = True
        self.points = []

    def paintGrid(self, painter):
        painter.setPen(QColor(Qt.black))
        painter.drawLine(0,60,180,60)
        painter.drawLine(0,120,180,120)
        painter.drawLine(60,0,60,180)
        painter.drawLine(120,0,120,180)

    def paintPoint(self,painter):
        for (i, j, is_circle) in self.points:
            if is_circle:
                painter.setPen(QColor(Qt.blue))
                painter.drawEllipse(    QPoint(30 + 60*i, 30 + 60*j),\
                                        10, 10)
            else:
                painter.setPen(QColor(Qt.red))
                painter.drawLine(   QPoint(20 + 60*i, 20 + 60*j),\
                                    QPoint(40 + 60*i, 40 + 60*j))
                painter.drawLine(   QPoint(20 + 60*i, 40 + 60*j),\
                                    QPoint(40 + 60*i, 20 + 60*j))

    def mousePressEvent(self, event):
        clic_pos = event.pos()
        i, j = clic_pos.x() // 60, clic_pos.y() // 60
        if i < 3 and j < 3:
            if len(self.points) == 0:
                self.points.append( (i, j, True) )
            else:
                self.points.append( (i, j, not self.points[-1][-1]) )
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.paintGrid(painter)
        self.paintPoint(painter)
        del(painter)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Learn Python by coding a game - Tic Tac Toe")

        # The game
        game = Game()

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

### MAIN ###
app = QApplication([])
mw = MainWindow()
mw.show()
app.exec_()

