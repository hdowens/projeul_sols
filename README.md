# Project Euler Solutions
My solutions to the online mathematical coding challenges - Project Euler. Written mostly in Python3 and some in C.
my project euler solutions. either in C or Python3.
https://projecteuler.net/archives

## Why do this?
I knew I was interested in mathematical side of the industry, so after researching for projects for a while I came across project euler. I challenged myself to do the first few puzzles, and it went from there. It has taught me a lot about python, and mathematical coding.

## For example, if you look at my later solutions they are much more pythonic and demonstrate the learning curve I have undergone whilst completing these problems

**q97** - However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.
Find the last ten digits of this prime number. Simple one liner in python.

**q92** - A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1

85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
As we know it can end at 89 or 1, just a simple while loop to test these conditions.

**q85** - Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution. Another combinatorics problem. It was easier to reduce the problem size to and n * 1 grid, and you can see for this it grows 1, 3, 6, etc. I.e., n + (n-1) + (n-2) + ... + 1 = n(n + 1) / 2. Adding another dimension m just meant m also followed the same arithmetic progression. So just n(n + 1) / 2 * m(m + 1) / 2. Following that, it was just the case of finding the minimum absolute difference using a simple double loop.

**q81** - Dynamic Programming problem to do with min path sum through a grid. Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt. 

**q79** - Passcode derivation.
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

**q76** - How many different ways can one hundred be written as a sum of at least two positive integers?
          I solved this with dyanmic programming. I noticed the recurrence relation from the example and therefore fit the dynamic programming solution I wrote for q31 - coin sums. Just needed a slight edit. Each num, from 0 < num <= 100, is based on the solutions from the number beneath it, except 1 which is there is only 1 solution obviously.

**q71**- By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7. I used a Farey sequence to get the answer to this.

**q70** - Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum. I brute forced initially, but it was so slow (10ish min) so it needed to be optimised. Explanation of code in comments.

**q69** - Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum. Phi(n) being Euler's totient function.

**q67** - Math path sum II, continuation of problem 18. I had already implemented a DP solution so it was a case of copying and pasting previously written code -> see q018.py as well.
          
**q65** - Find the sum of digits in the numerator of the 100th convergent of the continued fraction for Euler's constant.

**q63** - How many n-digit positive integers exist which are also an nth power?
          
**q62** - Find the smallest cube for which exactly five permutations of its digits are cube.
                    
**q59** - XOR encryption question, using a key with contains 3 lower case letters. The description is very long, find it here -> https://projecteuler.net/problem=59 .

**q58** - Prime spirals, ratio of primes in the diagonals to nonprimes. -> https://projecteuler.net/problem=58. Interestingly, the slowest part of the algorithm is checking to see if a number is prime or not ,as I'd managed to keep the rest of it to additions and a single modulus. Looking at other soltuions ,I stumbled across the Miller-Rabin primality test and implementation which I tried in my code and it brought it down from 2.8 to 0.9. After, I went and researched about it. Note theat implementation is not mine, and I have commented it out for that reason. I saw no problem with leaving this in the file due to the fact I already had solved the problem, and that this is learning exericse.

**q57** - In the first one-thousand expansions of the square root of 2, how many fractions contain a numerator with more digits than the denominator?

**q56** - Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

**q55** - How many Lychrel numbers are there below ten-thousand?

**q54** - Algorithm to interpret and solve poker hands. See whole description -> https://projecteuler.net/problem=54

**q53** - How many, not necessarily distinct, values of (nCr) for 1 <= n <= 100, are greater than one-million? Wrote a function which returns the nCr, combinations, given the formula n! / r! * (n-r)! . I then wrote a one-liner pythonic solution using sequential statements in list comprehension to include a double for loop and control statement ( if our n > 1,000,000)

**q52** - Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

**q50** - Which prime, below one-million, can be written as the sum of the most consecutive primes?

**q49** - The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?

**q48** - Last ten digits of the series 1^1 + 1^2 + ... + 1000^1000

**q47** - Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

**q46** - Proof of Goldbach's weak conjecture, What is the smallest odd composite that cannot be written as the sum of a prime and twice a square? Solved by rearranging the equation and finding the first number that did not satisfy it.

**q45** - Next hexagonal number after 40755 that is also hexagonal, pentagonal and triangular. Since hexagonal nums are a subset of triangular nums, if a number is hexagonal it is therefore triangluar, so you don't need to check it.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

**q44** - Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

Find the sum of all 0 to 9 pandigital numbers with this property

    d8d9d10=289 is divisible by 17
    d7d8d9=728 is divisible by 13
    d6d7d8=572 is divisible by 11
    d5d6d7=357 is divisible by 7
    d4d5d6=635 is divisible by 5
    d3d4d5=063 is divisible by 3
    d2d3d4=406 is divisible by 2

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

**q43** - The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

**q42** - By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word. Find all the triangle words from a list of 16K words. Included some optimisation by finding the biggest possible number and reducing range of triangle numbers to this.


What is the largest n-digit pandigital prime that exists?

**q41** - We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

**q40** - sum of the first, tenth, hundredth, thousandeth, ten thousandeth, hundred thousandeth and millionth digits of champernownes constant.

**q39** - Find the permieter of a right angled triangle below 1000 which maximising the amount of solutions to this triangle 

**q38** - What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

**q37** - sum of all of the left and right truncatable primes

**q36** - palindromic pairs of base 10 and base 2, below one million

**q35** - circular primes, how many below one million, solved with a function I wrote to shift integers by pos

**q34** - sum of all numbers which are equal to the sum of the factorial of each individual digit of that number

**q33** - non-trivial digit cancelling fractions

**q32** - Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

**q31** - coin sums, how many ways to make £2 with all available British coins. Dynamic programming solution used.

**q30** - sum of all the numbers which are themselves a sum of fifth powers of their digits. Solved with a loop and a formula for finding the limit to the loop. I wrote a generic solution for any power, instead of just 5 with two functions.

the diagonal numbers increasing by 2 for every 4 numbers in the diagonal ( the four corners )
**q28** - sum of the diagonals in a 1001 x 1001 number spiral matrix, solved with a few simple observations such as the step of 

**q27** - Find the product of the coefficients, and , for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0. Solved with a half brute force function. If we assume n = 0, b therefore must be prime, so we can reduce problem space from b to just primes.

**q26** - longest recurring decimal in the range 1 / 1 <= n <= 1000 . Solved using multiplicative order principle.

**q25** - fib qu again, first num with 1000 digits

**q24** - millionth lexicographic permutation of the decimal digits, in lexicographical order.

**q23** - all numbers which cannot be written as the sum of two abundant numbers

**q22** - name scores, file handling to produce value of letters in words with respect to position in the list

**q21** - sum of amicable numbers below 10000

**q20** - factorial digit sum of 100!, using recursion

**q19** - how many sundays between 1901 and 2001. Used python's datetime library to get more experience with it.

**q18** - max path sum through a triangle, solved with dynamic programming

how many letters would be used(brute forced with logic)
**q17** - If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,

**q16** -  sum of the digits of the number 2^1000

**q15** - How many route through a 20x20 grid only going right and down ( combinatoric issue, R and D permutations)

**q14** - number under 1,000,000 that produces the longest Collatz sequence

**q13** - first ten digits of the sum of the following one-hundred 50-digit numbers

**q12** - first triangluar number to have more than 500 divisors

**q11** - larget product of any 4 numbers in any direction (up,down,left,right,right diagonal, left diagonal) in a 20x20 grid

**q10** - summation of primes below 2 million (sieve of eratosthenes)

**q9** - pythagorean triplet for which a + b + c = 1000

**q8** - largest product of 13 adjacent digits in a 1000 digit number

**q7** - 10,001st prime number

**q6** - difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

**q5** - smallest positive number that is evenly divisible by all of the numbers from 1 to 20

**q4** - largest palindrome product of two 3-digit numbers

**q3** - largest prime factors

**q2** - sum of even values Fibonacci numbers

**q1** - fizzbuzz
