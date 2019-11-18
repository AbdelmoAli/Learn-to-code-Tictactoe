from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint, pyqtSignal

from src.TicTacToeCLI import TicTacToeCLI

class TicTacToeGUI(QWidget):
    game_ended = pyqtSignal(str)

    def __init__(self):
        super(TicTacToeGUI, self).__init__()
        self.setFixedSize(180,180)

        self.cli = TicTacToeCLI()

    def paintGrid(self, painter):
        painter.setPen(QColor(Qt.black))
        painter.drawLine(0,60,180,60)
        painter.drawLine(0,120,180,120)
        painter.drawLine(60,0,60,180)
        painter.drawLine(120,0,120,180)

    def paintPoints(self,painter):
        for i in range(3):
            for j in range(3):
                if not self.cli.is_empty(i,j):
                    if self.cli.value(i,j) == 'O':
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
        self.clic_pos = event.pos()
        i, j = self.clic_pos.x() // 60, self.clic_pos.y() // 60
        if i < 3 and j < 3: self.cli.add_mark(i,j)
        self.update()

        if self.cli.is_winner():
            game_ended.emit(cli.get_winner())
        elif self.cli.is_full():
            game_ended.emit(' ')

    def paintEvent(self, event):
        painter = QPainter(self)
        self.paintGrid(painter)
        self.paintPoints(painter)