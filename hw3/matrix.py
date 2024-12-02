import numpy as np
np.random.seed(0)
class matrix:
    def __init__(self, data, rows, cols):
        self.data = data
        self.rows = rows
        self.cols = cols

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Invalid matrix shapes for matrix multiplication")
        else:
            return matrix([[ sum(a*b for a,b in zip(row, col)) for col in zip(*other.data)]for row in self.data], self.rows, other.cols)

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Invalid matrix shapes for element-wise addition")
        else:
            return matrix([[a+b for a,b in zip(row, col)]for row, col in zip(self.data, other.data)], self.rows, self.cols)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Invalid matrix shapes for element-wise multiplication")
        else:
            return matrix([[a*b for a,b in zip(row, col)]for row, col in zip(self.data, other.data)],self.rows, self.cols)
    def __hash__(self):
        # hash function that returns a number between 0 and 3 based on the sum of the elements in the matrix
        return int(sum(sum(row) for row in self.data)%4)

def task3():
    dims = 2
    a = matrix(np.random.randint(0, 10, (dims, dims)), dims, dims)
    c = matrix(np.random.randint(0, 10, (dims, dims)), dims, dims)

    # generating new matrix c until hash(a) == hash(c)
    while hash(a) != hash(c):
        c = matrix(np.random.randint(0, 10, (dims, dims)), dims, dims)
    b = d = matrix(np.random.randint(0, 10, (dims, dims)), dims, dims)

    print_matrix(a.data, 'artifacts/3.3/A.txt')
    print_matrix(b.data, 'artifacts/3.3/B.txt')
    print_matrix(c.data, 'artifacts/3.3/C.txt')
    print_matrix(d.data, 'artifacts/3.3/D.txt')
    print_matrix((a @ b).data, 'artifacts/3.3/AB.txt')
    print_matrix((c @ d).data, 'artifacts/3.3/CD.txt')
    with open('artifacts/3.3/hash.txt', 'w') as f:
        f.write("AB hash: "+str(hash(a @ b)))
        f.write('\n')

        f.write("CD hash: "+str(hash(c @ d)))


def print_matrix(matrix,filename):
    with open(filename, 'w') as f:
        for row in matrix:
            for idx, elem in enumerate(row):
                elem = int(elem)
                row[idx] = elem
            f.write(str(row))
            f.write('\n')

task3()

