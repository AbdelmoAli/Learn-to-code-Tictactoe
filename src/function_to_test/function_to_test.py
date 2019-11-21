def function(L):
	def new_grid():
		return [['' for i in range(3)] for j in range(3)]
	

	def value(grid,i,j):
		return grid[i][j]
	

	def is_empty(grid,i,j):
		return value(grid,i,j)==""

	def add_mark(grid,i,j,mark):
				b=is_empty(grid,i,j)
				if b:
					grid[i][j]=mark
				return b,grid

	def switch_mark(mark): 	#pour l'instant
			if mark=='X':
				mark='O'
			else:
				mark='X'
			return mark

	def is_align(row):
		if row==['X' for i in range(3)] or row==['O' for i in range(3)]:
			return True
		else:
			return False 

	def get_rows(grid):
				rows = grid[:]	
				rows += [[grid[j][i] for j in range(3)] for i in range(3)]    
				rows.append( [grid[i][i] for i in range(3)] )
				rows.append( [grid[i][2-i] for i in range(3)] )
				return rows

	def has_winner(grid):
		if ['X','X','X'] in get_rows(grid) or ['O','O','O'] in get_rows(grid):
			return True
		else:
			return False

	def get_winner(grid):
		if ['X','X','X'] in get_rows(grid):
			return 'X'
		else:
			return 'O'

	def is_full(grid):
		for i in range(3):
			for j in range(3):
				if grid[i][j]=='':
					return False
		return True
	return (is_full(*L))