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

        # Multi-line strings (expression, flag, style)
        # FIXME: The triple-quotes in these two lines will mess up the
        # syntax highlighting from this point onward
        self.tri_single = (QRegExp("'''"), 1, STYLES['grey'])
        self.tri_double = (QRegExp('"""'), 2, STYLES['grey'])

        rules = []
        rules += [(r'\b%s\b' % w, 0, STYLES['magenta']) for w in PythonHighlighter.keywords]
        rules += [(r'%s' % o, 0, STYLES['magenta']) for o in PythonHighlighter.operators]
        rules += [(r'\b%s\b' % w, 0, STYLES['cyan']) for w in PythonHighlighter.functions]
        rules += [(r'\b%s\b' % w, 0, STYLES['purple']) for w in PythonHighlighter.logic]
        
        rules += [
            (r'\bself\b', 0, STYLES['orange']),                                                 # self   
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['yellow']),                                   # STRINGS '...'
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['yellow']),                                   # STRINGS "..."
            (r'(\w+)\s*\b\(', 1, STYLES['cyan']),                                               # FUCNTIONS ...(
            (r'\bdef\b\s*(\w+)', 1, STYLES['green']),                                           # FUCNTIONS def ...
            (r'\bclass\b\s*(\w+)', 1, STYLES['green']),                                         # CLASS class ...
            (r'#[^\n]*', 0, STYLES['grey']),                                                    # COMMENTS #...
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['purple']),                                     # NUMBERS
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['purple']),                          # NUMBERS
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['purple']),         # NUMBERS
        ]

        # Build a QRegExp for each pattern
        self.rules = [(QRegExp(pat), index, fmt) for (pat, index, fmt) in rules]


    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text.
        """
        # Do other syntax formatting
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # Do multi-line strings
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)


    def match_multiline(self, text, delimiter, in_state, style):
        """Do highlighting of multi-line strings. ``delimiter`` should be a
        ``QRegExp`` for triple-single-quotes or triple-double-quotes, and
        ``in_state`` should be a unique integer to represent the corresponding
        state changes when inside those strings. Returns True if we're still
        inside a multi-line string when this function is finished.
        """
        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            start = delimiter.indexIn(text)
            # Move past this match
            add = delimiter.matchedLength()

        # As long as there's a delimiter match on this line...
        while start >= 0:
            # Look for the ending delimiter
            end = delimiter.indexIn(text, start + add)
            # Ending delimiter on this line?
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            # No; multi-line string
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            # Apply formatting
            self.setFormat(start, length, style)
            # Look for the next match
            start = delimiter.indexIn(text, start + length)

        # Return True if still inside a multi-line string, False otherwise
        if self.currentBlockState() == in_state:
            return True
        else:
            return False