from PyQt5.QtWidgets import QApplication
from src.MainWindow import MainWindow

def main():
    app = QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec_()

if __name__ == "__main__":
    main()

    