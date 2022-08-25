import numpy as np
def cramer(mat, constant): # takes the matrix and the costants
    
    D = np.linalg.det(mat) # calculating the determinant of the original matrix
    print(D)
# substitution of the column with costant and creating new matrix
    # mat1 = np.array([constant, mat[1], mat[2]])
    # mat2 = np.array([mat[0], constant, mat[2]])
    # mat3 = np.array([mat[0], mat[1], constant])
    # print("---------------------------")
    # print(mat1)
    # print(mat2)
    # print(mat3)  
    mat1 = np.array([constant, mat[:,1], mat[:,2]])
    mat2 = np.array([mat[:,0], constant, mat[:,2]])
    mat3 = np.array([mat[:,0], mat[:,1], constant])  
    # print("---------------------------")
    # print(mat1)
    # print(mat2)
    # print(mat3)
#calculatin determinant of the matrix
    D1 = np.linalg.det(mat1)
    D2 = np.linalg.det(mat2)
    D3 = np.linalg.det(mat3)
    print(D1,D2,D3)
#finding the X1, X2, X3
    X1 = D1/D
    X2 = D2/D
    X3 = D3/D
    
    print(X1, X2, X3)

a = np.array([[3, -2, -1],
             [-4, 7, -1],
             [-6, 9, -3]])

b = np.array([12, 0, 0])

cramer(a,b)