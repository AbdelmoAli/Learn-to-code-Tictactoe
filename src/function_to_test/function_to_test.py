def function(L):
		from PyQt5.QtCore import QRegExp, Qt
	from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter, qRgb
	
def format(r,g,b):
	    """Return a QTextCharFormat with the given attributes.
	    """
	    _color = QColor(qRgb(r,g,b))
	    _format = QTextCharFormat()
	    _format.setForeground(_color)
	
	    return _format
	
	
	# Syntax styles that can be shared by all languages
	STYLES = {
	    'magenta': format(249,36,114),
	    'cyan': format(103,216,239),
	    'purple': format(172,128,255),
	    'yellow': format(231,219,116),
	    'grey': format(116,112,93),
	    'green': format(116,226,43),
	    'orange': format(253,150,34)
	}
	
	
	class PythonHighlighter(QSyntaxHighlighter):
	    """Syntax highlighter for the Python language.
	    """
	    keywords = [
	        'and', 'assert', 'break', 'continue',
	        'del', 'elif', 'else', 'except', 'finally',
	        'for', 'from', 'global', 'if', 'import', 'in',
	        'is', 'not', 'or', 'pass', 'print',
	        'raise', 'return', 'try', 'while', 'yield']
	    operators = [
	        '=', '==', '!=', '<', '<=', '>', '>=',
	        '\+', '-', '\*', '/', '//', '\%', '\*\*',
	        '\+=', '-=', '\*=', '/=', '\%=',
	        '\^', '\|', '\&', '\~', '>>', '<<']
	    functions = ['class', 'def', 'exec', 'lambda']
		logic = ['None', 'True', 'False']
	
def __init__(self, document):
	        QSyntaxHighlighter.__init__(self, document)
	    
	return (__init__(*L))