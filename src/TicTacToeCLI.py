class TicTacToeCLI():
    """
    TODO : documentation de la classe.
    """
    
    def empty_grid(self):
        """
        Create an empty grid.
        """
        return [[' ' for j in range(3)] for i in range(3)]

    def __init__(self):
        """
        Constructor
        """
        self.grid = self.empty_grid()
        self.mark = 'O'

    def reset(self):
        """
        Reset the grid to empty
        """
        self.grid = self.empty_grid()
        self.mark = 'O'

    def __str__(self):
        """
        Override to print a readable string presentation of the object
        """
        return ('\n-----\n').join( '|'.join(self.grid[i]) for i in range(3))

    def switch_mark(self):
        """
        Switch the current mark between 'O' and 'X'
        """
        self.mark = 'X' if self.mark == 'O' else 'O'

    def value(self, i, j):
        """
        Return the value of the (i,j) cell.
        """
        return self.grid[i][j]
    
    def is_empty(self, i, j):
        """
        Return a True if the (i,j) cell is empty.
        """
        return value(i,j) == ' '

    def is_full(self):
        """
        Return True if the tic tac toe is full.
        """
        for i in range(3):
            for j in range(3):
                if self.is_empty(i,j):
                    return False
        return True

    def add_mark(self, i, j):
        """
        Mark a grid cell if not empty (return False otherwise)
        TODO : add an exception ?
        """
        if not self.is_empty(i,j): return False
        self.grid[i][j] = self.mark
        self.switch_mark()

    def get_rows(self):
        """
        Generate all rows (lists of size 3) that of the grid
        """
        rows = [self.grid[i] for i in range(3)]
        rows += [[self.grid[j][i] for j in range(3)] for i in range(3)]
        rows.append([self.grid[i][i] for i in range(3)])
        rows.append([self.grid[i][2-i] for i in range(3)])

        return rows

    def is_align(self, row):
        """
        Determine if a row (or any list of size 3) is using only one mark
        """
        return row == ['X']*3 or row == ['O']*3

    def has_winner(self):
        """
        Determine whether a player has won yet
        """
        for row in self.get_rows():
            if self.is_align(row):
                return True
        return False

    def get_winner(self):
        """
        Return the winning player
        """
        if not self.has_winner(): return None

        rows = self.get_rows()
        if ['X']*3 in rows: return 'X'
        else : return 'O'
