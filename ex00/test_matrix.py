import Matrix
import unittest

class Test_Matrix(unittest.TestCase):
	def test_matrix_init_tuple(self):
		mat = Matrix.Matrix((2,3))
		self.assertEqual(mat.data, 2 * [3 * [0]])

	def test_matrix_init_lists(self):
		mat = Matrix.Matrix([[2,1,3],[3,4,3]])
		self.assertEqual(mat.shape[0], 2)
		self.assertEqual(mat.shape[1], 3)

	def test_matrix_add(self):
		mat1 = Matrix.Matrix([[2,1,3],[3,4,3]])
		mat2 = Matrix.Matrix([[1,6,3],[0,4,-2]])
		self.assertEqual((mat1 + mat2).data, [[3,7,6],[3,8,1]])

	def test_matrix_sub(self):
		mat1 = Matrix.Matrix([[2,1,3],[3,4,3]])
		mat2 = Matrix.Matrix([[1,6,3],[0,4,-2]])
		self.assertEqual((mat1 - mat2).data, [[1,-5,0],[3,0,5]])

	def test_matrix_div(self):
		mat1 = Matrix.Matrix([[2,1,3],[3,4,3]])
		self.assertEqual((mat1 / 2).data, [[1,0.5,1.5],[1.5,2,1.5]])

	def test_matrix_transpose(self):
		mat1 = Matrix.Matrix([[2,1,3],[3,4,3]])
		self.assertEqual((mat1.T()).data, [[2,3],[1,4],[3,3]])

	def test_matrix_mul(self):
		mat1 = Matrix.Matrix([[2,1],[3,4]])
		mat2 = Matrix.Matrix([[2,1],[3,4]])
		self.assertEqual((mat1 * mat2).data, [[7,6],[18,19]])
