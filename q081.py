from timeit import default_timer
"""
testmatrix = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 53, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [55, 732, 524, 37, 331]
]

"""

with  open("p081_matrix.txt") as f:
    matrix = [ [int(i) for i in line.split(",")] for line in f.read().splitlines()]

def compute():
    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix)-1, -1, -1):
            #min between down and right
            if i + 1 < len(matrix) and j + 1 < len(matrix):
                matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])
            #when you can only go down
            #add the value in the same column but row below
            elif i + 1 < len(matrix):
                matrix[i][j] += matrix[i + 1][j]
            #when you can only go right
            #add the value of the column to your right
            elif j + 1 < len(matrix) :
                matrix[i][j] += matrix[i][j + 1]

    print(matrix[0][0])
    return

if __name__ == "__main__":

    start = default_timer()

    compute()

    stop = default_timer()

    print("Time taken -> ", stop - start)
