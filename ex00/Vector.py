import Matrix



class Vector(Matrix):
	def __init__(self, param):
		if not (type(param) is list):
			raise ValueError("Vector init accept only array")
		if ( not (len(param) == 1) and not all([len(p) == 0 for p in param])):
			raise ValueError("Invalid size for array")
		Matrix.__init__(self, param)

	def dot(self, v : "Vector"):
		if not (self.shape[1] == v.shape[1]):
			raise ValueError("Unproperly scaled matrix")
		else:
			dot_product = 0
			for k in range(self.shape[0]):
				dot_product += self.data[0][k] * self.data[k][0]
		return Matrix(dot_product)
