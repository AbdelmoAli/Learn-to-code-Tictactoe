def function(L):
	def new_grid():
			return [['' for i in range(3)] for j in range(3)]
	
	return (new_grid(*L))