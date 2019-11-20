def function(L):
	def empty_grid():
		return [['' for j in range(3)] for i in range(3)]
	return (empty_grid(*L))