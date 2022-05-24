from timeit import default_timer

def compute():
  
    """
    I implemented a Farey sequence after researching lists of fractions, brute force would
    have taken so long. Each fraction N is just the previous fraction plus some values.
    We have the fractions 2/5 and 3/7, and we know the answer is going to be somewhere in
    between. Given the Farey sequence definition, we know that the next fraction is going to
    be 2 + 3 / 5 + 7. We keep adding 3 and 7 to get the next fraction in between these fracti
    -ions, as per the Farey sequence.
    """
    numer, denom = 2, 5
    while denom < 999_993:
        numer, denom = numer + 3 , denom + 7
    print(numer, denom)

if __name__ == "__main__":

    start = default_timer()

    compute()

    stop = default_timer()

    print("Time taken -> ", stop - start)
