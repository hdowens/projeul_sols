from timeit import default_timer

def compute():
    with open("p067_triangle.txt") as f:
        triangle = [[int(x) for x in f.readline().split(" ")] for i in range (100)] 
    for i in range(len(triangle)-2,-1,-1):
        for j in range(0,i+1):
            if(triangle[i+1][j] > triangle[i+1][j+1]):
                triangle[i][j] += triangle[i+1][j]
            else:
                triangle[i][j] += triangle[i+1][j+1]

    return triangle[0][0]

if __name__ == "__main__":

    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
