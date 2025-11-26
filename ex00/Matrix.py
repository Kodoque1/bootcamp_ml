
from typing import Union,TypeVar

Num = Union[int, float]
Coeff = Union[list[list[Num]],tuple[int,int]]

class Matrix:
	def __init__(self, init_values : Coeff):
		if (type(init_values) is list):
			it = iter(init_values)
			the_len = len(next(it))
			if not all(len(l) == the_len for l in it):
				raise ValueError('Not all lists have same length')
			self.data = init_values
			self.shape = (len(init_values), len(init_values[0]))
		elif ((type(init_values) is tuple)):
			if len(init_values) != 2:
				raise ValueError('Shape should have 2 values')
			self.shape = init_values
			self.data = [[0 for j in range(init_values[1])] for i in range(init_values[0])]

	def __add__(self, mat : "Matrix"):
		if self.shape != mat.shape:
			raise ValueError("Matrix must be the same shape")
		else:
			tmp = [[0 for j in range(self.shape[1])] for i in range(self.shape[0])]
			for i in range(self.shape[0]):
				for j in range(self.shape[1]):
					tmp[i][j] = self.data[i][j] + mat.data[i][j]
		return Matrix(tmp)

	def __radd__(self, mat : "Matrix"):
		if self.shape != mat.shape:
			raise ValueError("Matrix must be the same shape")
		else:
			tmp = [[0 for j in range(self.shape[1])] for i in range(self.shape[0])]
			for i in range(self.shape[0]):
				for j in range(self.shape[1]):
					tmp[i][j] = self.data[i][j] + mat.data[i][j]
		return Matrix(tmp)

	def __sub__(self, mat : "Matrix"):
		if self.shape != mat.shape:
			raise ValueError("Matrix must be the same shape")
		else:
			tmp = [[0 for j in range(self.shape[1])] for i in range(self.shape[0])]
			for i in range(self.shape[0]):
				for j in range(self.shape[1]):
					tmp[i][j] = self.data[i][j] - mat.data[i][j]
		return Matrix(tmp)

	def __sub__(self, mat : "Matrix"):
		if self.shape != mat.shape:
			raise ValueError("Matrix must be the same shape")
		else:
			tmp = [[0 for j in range(self.shape[1])] for i in range(self.shape[0])]
			for i in range(self.shape[0]):
				for j in range(self.shape[1]):
					tmp[i][j] = self.data[i][j] - mat.data[i][j]
		return Matrix(tmp)

	def __truediv__(self, scalar : Num):
		if scalar == 0:
			raise ValueError("Can't divide by Zero")
		else:
			tmp = [[0 for j in range(self.shape[1])] for i in range(self.shape[0])]
			for i in range(self.shape[0]):
				for j in range(self.shape[1]):
					tmp[i][j] = self.data[i][j] / scalar
		return Matrix(tmp)

	def __rtruediv__(self, scalar):
		raise ValueError("Can't divide scalar by Matrix")

	def __mul__(self, mat : "Matrix"):
		if not (self.shape[1] == mat.shape[0]):
			raise ValueError("Unproperly scaled matrix")
		else:
			tmp = [[0 for j in range(self.shape[1])] for i in range(self.shape[0])]
			for i in range(self.shape[0]):
				for j in range(self.shape[1]):
					for k in range(self.shape[0]):
						tmp[i][j] += self.data[i][k] * self.data[k][j]
		return Matrix(tmp)

	def __rmul__(self, mat : "Matrix"):
		if not (self.shape[1] == mat.shape[0]):
			raise ValueError("Unproperly scaled matrix")
		else:
			tmp = [[0 for j in range(self.shape[1])] for i in range(self.shape[0])]
			for i in range(self.shape[0]):
				for j in range(self.shape[1]):
					for k in range(self.shape[0]):
						tmp[i][j] += self.data[i][k] * self.data[k][j]
		return Matrix(tmp)

	def __str__(self):
		return str(self.data)

	def __repr__(self):
		return str(self.data)

	def T(self):
		tmp = [[0 for j in range(self.shape[0])] for i in range(self.shape[1])]
		for i in range(self.shape[0]):
				for j in range(self.shape[1]):
					tmp[j][i] = self.data[i][j]
		return Matrix(tmp)

