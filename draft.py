from PyQt5.QtWidgets import QApplication, QTextBrowser
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

def main():
    app = QApplication([])
    text = QTextBrowser()
    text.setSource(QUrl("file:src/res/lesson1.htm"))
    text.show()
    app.exec_()

if __name__ == "__main__":
    main()