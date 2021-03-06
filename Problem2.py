#gather information about the matrix to be generated
def gather_input():
    dimension = input('Enter the dimension of the matrix: ')
    matrix = [] #start an empyt matrix
    for i in range(int(dimension)):
        row = []
        for j in range (int(dimension)):
            row.append(int(input('enter a number')))
        matrix.append(row)
    return matrix, dimension

#calculate the absolute difference between the main diagonal and the secundary diagonal of a given matrix
def absolute_difference(matrix, dimension):
    sum_main_diag = 0
    sum_sec_diag = 0
    index = 0
    length = int(dimension)-1 #without the '-1' it would result on an 'array out of bounds'
    while index<=(length):
        sum_main_diag += matrix[index][index]
        sum_sec_diag += matrix[index][length-index]
        index += 1
    return abs(sum_main_diag - sum_sec_diag)
    

matrix,dimension = gather_input()
result = absolute_difference(matrix, dimension)
print(result)

