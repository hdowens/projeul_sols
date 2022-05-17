from timeit import default_timer

def word_to_val(l):
    lst = []
    word = list(l)
    for i in word:
        alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
        lst.append(alphabet.index(i.lower()) + 1)
    return sum(lst)

def generate_triangle_nums(lim):
    return [(int(0.5*n*(n+1))) for n in range(1,lim)]

def get_answer():
    count = 0
    tri_nums = []
    with open('words.txt', encoding='utf-8') as file:
        words = file.read()
        words = words[1: -1].split('","')

    tri_nums =  generate_triangle_nums(len(max(words, key = len)) * 26)
    for item in words:
        if word_to_val(item) in tri_nums:
            count += 1
    return count

if __name__ == "__main__":
    start = default_timer()
    
    print(get_answer())

    stop = default_timer()

    print("Time taken -> ",stop-start)
