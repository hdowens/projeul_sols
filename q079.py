from timeit import default_timer

"""
This function takes the middle numbers of the passcode, and returns them in position.
It works because it figures out which numbers appear after each one in the 3 digit
login attempts. 

For example, with 3. In the answer, 3 is the second digit. In this function, it determines
that 3 has all the other numbers in the unique numbers after it, len(ret) = 5. This means
we know that it must appear second in the answer. Follow this process for all the unique
nums, sort by ascending values in the dictionary, add them to a string.
"""
def nums_before(u, passc):
    positions = {}
    for x in u:
        x= int(x)
        ret = set()
        for p in passc:
            digits = [int(n) for n in str(p)]
            if x in digits:
                i = digits.index(x)
                if i < 2:
                    if i == 1: ret.add(digits[2])
                    elif i == 0 : 
                        ret.add(digits[2]) 
                        ret.add(digits[1])
     
        positions[x] = len(ret)
        
    sorted_pos = reversed(sorted((value, key) for (key,value) in positions.items()))
    ans = ""
    for p in sorted_pos:
        ans += str(p[1])
    return ans


def compute():
    with open('p079_keylog.txt', 'r') as f:  
        passcodes = set(f.read().splitlines())
        print("Removing", 50 - len(passcodes),"redundant passcodes", )
    
    first_digit = set()
    second_digit = set()
    third_digit = set()

    for p in passcodes:
        first_digit.add(p[0])
        second_digit.add(p[1])
        third_digit.add(p[2])

    unique_nums = first_digit | second_digit | third_digit
    #print("The union of these sets -> ", unique_nums, "passcode length -> ", len(unique_nums))
    #using the debugger I see that 7 appears in first digits only
    #and 0 appears in last digits only
    #making the passcode length 8 and of form 7######0 where # is an integer in the unique nums
    
    unique_nums.remove("0")
    unique_nums.remove("7")
    
    #we now need to figure out what order the rest of the numbers are in
    #we know that numbers are asked in order, so we need to see which numbers 
    #come after which in the passcodes.
    middle_nums = nums_before(unique_nums,passcodes)

    return "7" + middle_nums + "0"


if __name__ == "__main__":

    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
