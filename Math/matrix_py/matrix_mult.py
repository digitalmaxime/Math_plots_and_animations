def mult(A, B):
    rows_A = len(A)
    rows_B = len(B)
    cols_A = len(A[0])
    cols_B = len(B[0])
    rows_C = rows_A
    cols_C = cols_B
    C = [[None for _ in range(cols_C)] for _ in range(rows_C)] #initialize nxm empty matrix
    for k in range(cols_C):   
        for i in range(rows_A):
            temp = 0
            for j in range(cols_A):
                temp += A[i][j]*B[j][k]
            C[i][k] = temp
    return C


def power(A, exponent):
    C = A
    for i in range(exponent - 1):
       C = mult(A, C) 
    return C


def display(C):
    for i in range(len(C)):
        for j in range(len(C[0])):
            print(C[i][j], end='\t')
        print("")

                
if __name__ == "__main__":
    A = [
        [0, 1],
        [1, 1]
        ]
    B = [
        [3, 1],
        [0, 2]
        ]
    
    display(A)
    print('-' * 30)

    C = mult(A, A) 
    display(C)
    print('-' * 30)
    C = mult(A, C)
    display(C)
    print('-' * 30)
    C = mult(A, C) 
    display(C)
    print('-' * 30)
    C = mult(A, C) 
    display(C)
    print('-' * 30)
    C = mult(A, C) 
    display(C)
    print('-' * 30)
    C = mult(A, C) 
    display(C)
    print('-' * 30)
    C = mult(A, C) 
    display(C)
    print('-' * 30)

M = power(B, 2)
display(M)