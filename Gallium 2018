""" The link to the Gallium 2018 problem can be found here: https://app.codility.com/programmers/task/max_zero_product/
The short version: Given an array of integers, compute the maximum number of zeroes at the end of the product of some three elements of the array.

Note if the highest power of 10 dividing a number M is x, then we have that either 2^x divides M and x is the highest power of 5 dividing M,
or 5^x divides M and x is the highest power of 2 dividing M. This is because 2 and 5 are prime, and are the divisors of 10.

This is very complicated, and altough has some aspects of dynamic programming, it is not simply a matter of travelling through the array once,
we need some storage, and some nice structures to keep hold of specific data, and dynamically update them.

Note first we must define a (simple) function that takes a number n, and outputs the highest powers of 2 and 5 dividing it, which isn't too hard.

We will use 3 dictionaries: Dict1 records the highest power of 5 dividing any number x seen 'so far' given that 2^i divides x, where i is the key of the item.
                            Example: in the first step of our loop, for i in range(1, a+1), we let Dict1[i] = b, where a and b are the highest powers of 2 and 5 dividing x, the first element in the array.
Then Dict2 records the highest power of 5 dividing xy, where x and y are 2 different numbers, and they have 'been seen' by our loop, given that 2^i divides xy, and i is the key of our item.
Dict3 is similar, but for xyz.
To finish up, we cycle through the third dictionary Dict 3, looking at min of i, and Dict3[i], and take the max of all these numbers. Code is below:"""

#First we define our power function:

def power(n):
  pow2 = 0
    while n and n % 2 == 0:
      n = n/2
      pow2 += 1

  pow5 = 0
  while n and n % 5 == 0:
    n = n/5
      five += 1

  return (pow2, pow5)

def solution(A):

#a defaultdict is a standard python dictionary, but with all key values automatically initialized to 0; it is a cheap way of just incrementing any key value without setting it to 0 first

  from collections import defaultdict      
  Dict1 = defaultdict(int)
  Dict2 = defaultdict(int)
  Dict3 = defaultdict(int)


  #line below just turns our array A into the pairs of the form (a,b), where a and b are the highest powers of 2 and 5 dividing the element of A
  for a, b in map(power, A):
    for i, v in Dict2.items():
      Dict3[i + a] = max(Dict3[i + a], Dict2[i] + b)
    for i, v in Dict1.items():
      Dict2[i + a] = max(Dict2[i + a], Dict1[i] + b)
    for i in range(a+1):
      Dict1[i] = max(Dict1[i], b)

  answer = 0
  for i, v in Dict3.items():
    answer = max(answer, min(i, v))
  return answer  

"""In the question, N is limited by 1000,000,000, so the maximum powers of 2 and 5 dividing it are bounded above (29 and 9), so each line in the for loop
(i.e. the one starting 'for a, b in map(power, A):') is done in constant time, so this algorithm has Temporal complexity O(N).
It has spatial complexity O(N): the storage is the 3 dictionaries (each O(N), since there are at most N keys in Dict1, so at most 2N keys in Dict2, so at most 3N keys in Dict2), as well as answer, and the power mapped form of A, which are O(1) and O(N) respectively.
