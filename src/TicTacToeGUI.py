from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint, pyqtSignal

from src.TicTacToeCLI import TicTacToeCLI

class TicTacToeGUI(QWidget):
    """
    This class implement the GUI for the Tic Tac Toe game
    already implemented in TicTacToeCLI
    """
    ended = pyqtSignal(str)

    def __init__(self):
        """
        Constructor.
        """
        super(TicTacToeGUI, self).__init__()
        self.setFixedSize(180,180)

        self.cli = TicTacToeCLI()
        self.level = 1

    def reset(self):
        """
        Trigger reset of TicTacToeCLI.
        """
        self.cli.reset()
        self.update()

    def change_level(self, level):
        """
        Manage the current level.
        Reset the grid and update the display.
        """
        self.level = level
        self.reset()
        self.update()

    def paintGrid(self, painter):
        """
        Paint the grid.
        """
        painter.setPen(QColor(Qt.white))
        painter.drawLine(0,60,180,60)
        painter.drawLine(0,120,180,120)
        painter.drawLine(60,0,60,180)
        painter.drawLine(120,0,120,180)

    def paintPoints(self,painter):
        """
        Paint circles and crosses inside the grid. 
        """
        for i in range(3):
            for j in range(3):
                if not self.cli.is_empty(i,j):
                    if self.cli.value(i,j) == 'O' or self.level <= 5:
                        painter.setPen(QColor(Qt.cyan))
                        painter.drawEllipse(    QPoint(30 + 60*i, 30 + 60*j),\
                                                10, 10)
                        painter.drawEllipse(    QPoint(30 + 60*i, 30 + 60*j),\
                                                9, 9)
                        painter.drawEllipse(    QPoint(30 + 60*i, 30 + 60*j),\
                                                10, 9)
                        painter.drawEllipse(    QPoint(30 + 60*i, 30 + 60*j),\
                                                9, 10)
                        
                    else:
                        painter.setPen(QColor(Qt.magenta))
                        painter.drawLine(   QPoint(20 + 60*i, 20 + 60*j),\
                                            QPoint(40 + 60*i, 40 + 60*j))
                        painter.drawLine(   QPoint(20 + 60*i+1, 20 + 60*j),\
                                            QPoint(40 + 60*i+1, 40 + 60*j))
                        painter.drawLine(   QPoint(20 + 60*i-1, 20 + 60*j),\
                                            QPoint(40 + 60*i-1, 40 + 60*j))

                        painter.drawLine(   QPoint(20 + 60*i, 40 + 60*j),\
                                            QPoint(40 + 60*i, 20 + 60*j))
                        painter.drawLine(   QPoint(20 + 60*i+1, 40 + 60*j),\
                                            QPoint(40 + 60*i+1, 20 + 60*j))
                        painter.drawLine(   QPoint(20 + 60*i-1, 40 + 60*j),\
                                            QPoint(40 + 60*i-1, 20 + 60*j))

    def mousePressEvent(self, event):
        """
        Add a mark to a grid when the user click.
        """
        self.clic_pos = event.pos()
        i, j = self.clic_pos.x() // 60, self.clic_pos.y() // 60
        if i < 3 and j < 3: self.cli.add_mark(i,j)
        self.update()

        if self.cli.has_winner() and self.level > 8:
            self.ended.emit(self.cli.get_winner() if self.level > 9 else '???')
        elif self.cli.is_full() and self.level > 10:
            self.ended.emit(' ')

    def paintEvent(self, event):
        """
        Manage the graphical interface.
        """
        painter = QPainter(self)
        if self.level > 1 : self.paintGrid(painter)
        if self.level > 4 : self.paintPoints(painter)
