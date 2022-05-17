from timeit import default_timer
from math import pow
from collections import Counter
from itertools import count

"""
def compare(list1, list2):
    return Counter(list1) == Counter(list2)

def compute_att1():
    cubes = [int(pow(i,3)) for i in range(4000,10000)]
    prim_cnt = 0
    found = False
    while not found:
        lcount = 0
        cur_cube = cubes[prim_cnt]
        cur_cube_list = [int(x) for x in str(cur_cube)]
        for i in cubes:
            if len(str(i)) == len(str(cur_cube)):
                list1 = [int(x) for x in str(i)]
                if compare(cur_cube_list, list1):
                    lcount += 1
        if lcount == 5:
            print("FIRST CUBE IS -> ",cur_cube)
            found = True
        prim_cnt += 1
    return 






Attempt 2.

The first method is a pure brute force with some optimisations I made, such
as only checking other cubes of same length and running it a few times over to manipulate 
the range so it gets it quickly, it is a sub-optimal solution with a run time of O(n^2). It
still runs in about 30s but I knew there would be a better solution.

With some research into dictionaries I was able to write this solution below, which runs in a 
few ms. It is a very basic idea, if the sorted current cube is already in the dictionary, i.e. if 
the current cube is a permutation of another cube in the dictionary, then append the cube root of
the current_cube thus increasing the length of that entry by 1.

E.g. 
cur_cube = 373559126408
the sorted version is 012334556789. Check and see if 012...89 is in the dictionary, if it is,
append the current i to that list corresponding to that value in the list. 
{'012334556789'} = [5027,7061]
cur_cube is a permutation, so append it to the list
{'012334556789'} = [5027,7061, 7202]

If it's not in the list, it becomes a new entry in the dictionary. Keep going until one of the 
entries' lists' length is 5, and if so print out all entries for that integer and the first
cube number is our answer.
"""

def compute_att2():

    cubes = {}

    for i in count(start = 345):
        cur_cube = int(pow(i, 3))
        cur_cube = "".join(sorted(str(cur_cube)))
        if cur_cube in cubes:
            cubes[cur_cube].append(i)
            if len(cubes[cur_cube]) == 5:
                for j in cubes[cur_cube]:
                    print(j, "cubed is", int(pow(j, 3)))
                return
        else:
            cubes[cur_cube] = [i]

if __name__ == "__main__":
      
    start = default_timer()

    compute_att2()

    stop = default_timer()

    print("Time taken -> ", stop - start)
