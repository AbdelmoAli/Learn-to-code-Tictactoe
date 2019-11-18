class TicTacToeCLI():
    def empty_grid(self):
        return [[' ' for j in range(3)] for i in range(3)]

    def __init__(self):
        self.grid = self.empty_grid()
        self.mark = 'O'

    def reset(self):
        self.grid = self.empty_grid()
        self.mark = 'O'

    def __str__(self):
        return ('\n-----\n').join( '|'.join(self.grid[i]) for i in range(3))

    def switch_mark(self):
        if self.mark == 'O': self.mark = 'X'
        else: self.mark = 'O'

    def is_empty(self, i, j):
        return self.grid[i][j] == ' '

    def value(self, i, j):
        return self.grid[i][j]

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.is_empty(i,j):
                    return False
        return True

    def add_mark(self, i, j):
        if not self.is_empty(i,j): return False
        self.grid[i][j] = self.mark
        self.switch_mark()

    def is_align(self, row):
        return row == ['X'] * 3 or row == ['O']

    def mark_case(self, x, y, mark):
        self.grid[x][y] = mark
        self.possible_pos.remove((x, y))

    def get_rows(self):
        rows = [self.grid[i] for i in range(3)]
        rows += [[self.grid[j][i] for j in range(3)] for i in range(3)]
        rows.append([self.grid[i][i] for i in range(3)])
        rows.append([self.grid[i][2-i] for i in range(3)])

        return rows

    def is_align(self, row):
        return row == ['X']*3 or row == ['O']*3

    def is_winner(self):
        for row in self.get_rows():
            if self.is_align(row):
                return True
        return False

    def get_winner(self):
        if not self.is_winner(): return None

        rows = self.get_rows()
        if ['X']*3 in rows: return 'X'
        else : return 'O'