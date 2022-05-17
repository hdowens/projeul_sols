from timeit import default_timer
from fractions import Fraction

def get_answer():
    result = Fraction(1,1)
    for i in range(11,98):
        numer = str(i)
        for j in range(i+1,99):
            denom = str(j)
            if(numer[0] == denom[1] or numer[1] == denom[0]):
                if not (numer[0] == "0" or numer[1] == "0" or denom[0] == "0" or denom[1] == "0"):
                    if int(numer[0]) / int(denom[1]) == i / j or int(numer[1]) / int(denom[0]) == i / j:
                        result *= Fraction(i , j)

    return result.denominator


if __name__ == "__main__":
    start = default_timer()
    
    print(get_answer())

    stop = default_timer()

    print("Time taken -> ",stop-start)
