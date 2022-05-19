from timeit import default_timer

def is_palindrome(s):
    s = str(s)
    return len(s) < 2 or ( s[0] == s[-1] and is_palindrome(s[1: -1]))

def rev(x):
    return int("".join(reversed(str(x))))

def is_not_lychrel(x):
    count = 0
    while count < 50:
        newsum = x + rev(x)
        if is_palindrome(newsum):
            return True
        x = newsum
        count += 1

    return False

def compute():
    #for all numbers less 10000, if its not a lychrel number, add it to the list
    #so the ans is 10000 - how many aren't lychrel numbers
    return 10000 - len([i for i in range(1, 10001) if is_not_lychrel(i)])

if __name__ == "__main__":

    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
