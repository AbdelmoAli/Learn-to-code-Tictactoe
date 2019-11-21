from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from src.MainWindow import MainWindow

from PyQt5.QtCore import QUrl

def main():
    app = QApplication([])
    mw = MainWindow()
    mw.showMaximized()
    app.exec_()

if __name__ == "__main__":
    main()

