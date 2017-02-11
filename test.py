from adeli import *
import unittest


class TestAdeli(unittest.TestCase):
    def test_dot(self):
        a = [1, 2]
        b = [3, 4]
        self.assertEqual(dot(a, b), 11)

    def test_matrix(self):
        row = 3
        col = 2
        m = matrix(row, col)
        self.assertEqual(matrix_row(m), row)
        self.assertEqual(matrix_col(m), col)
        for i in range(row):
            for j in range(col):
                self.assertEqual(m[i][j], 0.0)

    def test_frobenius_norm(self):
        m = matrix(3, 2)
        m[0][0] = 3.0
        m[0][1] = 4.0
        self.assertEqual(frobenius_norm(m), 5.0)

    def test_identity_matrix(self):
        m = matrix_identity(4)
        for i in range(matrix_row(m)):
            for j in range(matrix_col(m)):
                if i == j:
                    self.assertEqual(m[i][j], 1.0, f"row {i} col {j}")
                else:
                    self.assertEqual(m[i][j], 0.0, f"row {i} col {j}")
        self.assertTrue(is_identity(m))

    def test_diagonal_matrix(self):
        m = matrix_diagonal([1, 2, 3])
        self.assertTrue(is_diagonal(m))
        self.assertEqual(matrix_row(m), 3)
        self.assertEqual(m[0][0], 1)
        self.assertEqual(m[1][1], 2)
        self.assertEqual(m[2][2], 3)

    def test_matrix_equality(self):
        m = matrix(2, 2)
        n = matrix(2, 3)
        self.assertTrue(matrix_equal(m, m))
        self.assertFalse(matrix_equal(m, n))

    def test_elementwise_product(self):
        m = [[1, 2],  [3,   4]]
        n = [[5, 6],  [7,   8]]
        o1 = [[5, 12], [21, 32]]
        o2 = elementwise_product(m, n)
        self.assertTrue(matrix_equal(o1, o2))

    def test_matrix_symmetric(self):
        m = [[1, 3],
             [3, 1]]
        self.assertTrue(matrix_is_symmetric(m))

        n = [[1, 3],
             [2, 1]]
        self.assertFalse(matrix_is_symmetric(n))

if __name__ == '__main__':
    unittest.main()
