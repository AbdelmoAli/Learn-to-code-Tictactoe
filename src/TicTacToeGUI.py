from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint

class TicTacToeGUI(QWidget):
    def __init__(self):
        super(TicTacToeGUI, self).__init__()
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