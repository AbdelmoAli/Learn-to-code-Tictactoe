from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter, qRgb

def format(r,g,b):
    """Return a QTextCharFormat with the given attributes.
    """
    _color = QColor(qRgb(r,g,b))
    _format = QTextCharFormat()
    _format.setForeground(_color)

    return _format

COLORS = {
    'magenta': format(249,36,114),
    'cyan': format(103,216,239),
    'purple': format(172,128,255),
    'yellow': format(231,219,116),
    'grey': format(116,112,93),
    'green': format(116,226,43),
    'orange': format(253,150,34)
}