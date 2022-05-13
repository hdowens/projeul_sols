from timeit import default_timer

def decrypt(text, key):
    #this function decrypts the text given the key. It XOR's the current character at text[i] with the ascii value
    #of whatever character is at key[i % 3] (just key[0,1,2] over and over again.) for all the characters in the encrypted
    #message.
    return "".join(chr(text[i]^ord(key[i % 3])) for i in range(len(text)))

def compute():

    bestkey = ""

    with open('p059_cipher.txt') as f:
        vals = [int(val) for val in f.readline().strip().split(",")]

    #iterate over all possibilites, 97 to 123 is the range of lower case letters in decimal in the ASCII table
    for x in range(97, 123):
        for y in range(97, 123):
            for z in range(97, 123):
                #key is made from chr(x) + chr(y) + chr(z)
                message = decrypt(vals,chr(x) + chr(y) + chr(z))
                #guessed these words, "and" and "the" are obvious ones, but I got lucky
                #and guessed the encrypted text would have been taken from one of euler's (project euler..) papers, hence "series".
                if "and" in message and "the" in message and "series" in message:
                    bestkey = chr(x) + chr(y) + chr(z)
                
    return sum(ord(i) for i in decrypt(vals, bestkey))


if __name__ == "__main__":
    
    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
