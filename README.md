# projeul_sols
My solutions to the online mathematical coding challenges - Project Euler. Written mostly in Python3 and some in C.
my project euler solutions. either in C or Python3.

q1 - fizzbuzz

q2 - sum of even values Fibonacci numbers

q3 - largest prime factors

q4 - largest palindrome product of two 3-digit numbers

q5 - smallest positive number that is evenly divisible by all of the numbers from 1 to 20

q6 - difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

q7 - 10,001st prime number

q8 - largest product of 13 adjacent digits in a 1000 digit number

q9 - pythagorean triplet for which a + b + c = 1000

q10 - summation of primes below 2 million (sieve of eratosthenes)

q11 - larget product of any 4 numbers in any direction (up,down,left,right,right diagonal, left diagonal) in a 20x20 grid

q12 - first triangluar number to have more than 500 divisors

q13 - first ten digits of the sum of the following one-hundred 50-digit numbers

q14 - number under 1,000,000 that produces the longest Collatz sequence

q15 - How many route through a 20x20 grid only going right and down ( combinatoric issue, R and D permutations)

q16 -  sum of the digits of the number 2^1000

q17 - If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used(brute forced with logic)

q18 - max path sum through a triangle, solved with dynamic programming

q19 - how many sundays between 1901 and 2001. Used python's datetime library to get more experience with it.

q20 - factorial digit sum of 100!, using recursion

q21 - sum of amicable numbers below 10000

q22 - name scores, file handling to produce value of letters in words with respect to position in the list

q23 - all numbers which cannot be written as the sum of two abundant numbers

q24 - millionth lexicographic permutation of the decimal digits, in lexicographical order.

q25 - fib qu again, first num with 1000 digits

q26 - longest recurring decimal in the range 1 / 1 <= n <= 1000 . Solved using multiplicative order principle.

q27 - Find the product of the coefficients, and , for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0. Solved with a half brute force function. If we assume n = 0, b therefore must be prime, so we can reduce problem space from b to just primes.

q28 - sum of the diagonals in a 1001 x 1001 number spiral matrix, solved with a few simple observations such as the step of 
the diagonal numbers increasing by 2 for every 4 numbers in the diagonal ( the four corners )

q30 - sum of all the numbers which are themselves a sum of fifth powers of their digits. Solved with a loop and a formula for finding the limit to the loop. I wrote a generic solution for any power, instead of just 5 with two functions.

q31 - coin sums, how many ways to make £2 with all available British coins. Dynamic programming solution used.

q32 - Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

q35 - circular primes, how many below one million, solved with a function I wrote to shift integers by pos

q36 - palindromic pairs of base 10 and base 2, below one million

q37 - sum of all of the left and right truncatable primes

q39 - Find the permieter of a right angled triangle below 1000 which maximising the amount of solutions to this triangle 

q40 - sum of the first, tenth, hundredth, thousandeth, ten thousandeth, hundred thousandeth and millionth digits of champernownes constant. 

q42 - By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word. Find all the triangle words from a list of 16K words. Included some optimisation by finding the biggest possible number and reducing range of triangle numbers to this.
