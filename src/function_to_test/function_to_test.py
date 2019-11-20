def function(L):
	def foo():
		return print(3)
	return (foo(*L))