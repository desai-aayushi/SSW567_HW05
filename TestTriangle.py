import unittest

from Triangle import classify_triangle

class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
    def testRightTriangleB(self):
       self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
    def testRightTriangleC(self):
       self.assertEqual(classify_triangle(4, 3, 5), 'Right', '4,3,5 is a Right triangle')
    def testEquilateralTriangle(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
    def testScaleneTriangleA(self):
        self.assertEqual(classify_triangle(3, 5, 6), 'Scalene', '3, 5, 6 should be scalene')
    def testScaleneTriangleB(self):
        self.assertEqual(classify_triangle(4, 5, 6), 'Scalene', '3, 5, 6 should be scalene')
    def testIsoscelesA(self):
        self.assertEqual(classify_triangle(5, 5, 3), 'Isoceles', '5,5,3 should be isoceles')
    def testIsoscelesB(self):
        self.assertEqual(classify_triangle(3, 5, 5), 'Isoceles', '3,5,5 should be isoceles')
    def testIsoscelesC(self):
        self.assertEqual(classify_triangle(5, 3, 5), 'Isoceles', '5,3,5 should be isoceles')
    def testInvalidTriangleA(self):
        self.assertEqual(classify_triangle(-1, 2, 3), 'InvalidInput', '-1,2,3 is invalid input')
    def testInvalidTriangleB(self):
        self.assertEqual(classify_triangle(0, 2, 3), 'InvalidInput', '0,2,3 is invalid input')
    def testInvalidTriangleC(self):
        self.assertEqual(classify_triangle(2, 2, 0), 'InvalidInput', '2,2,0 is invalid input')
    def testInvalidTriangleD(self):
        self.assertEqual(classify_triangle(1, 2, 0.20), 'InvalidInput', '1,2,0.20 is invalid input')
    def testInvalidTriangleE(self):
        self.assertEqual(classify_triangle(-1, -1, -1), 'InvalidInput', '-1,-1,-1 is invalid')
    def testNotATriangle(self):
        self.assertEqual(classify_triangle(2, 3, 10), 'NotATriangle', '2,3,10 is not a triangle')

    # add test cases for coverage report:100%

    def testInvalidTriangleF(self):
        self.assertEqual(classify_triangle(300, 300, 300), 'InvalidInput', '300,300,300 is invalid')

    def testRightTriangleD(self):
        self.assertEqual(classify_triangle(3, 5, 4), 'Right', '4,3,5 is a Right triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

