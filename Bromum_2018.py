"""Solution for the Bromum 2018 problem, link to the problem can be found here: https://app.codility.com/programmers/task/buckets/
Short version: Given N buckets and M colored balls to put in them, find the earliest moment when some bucket contains Q balls of the same color.

Note that if 2 balls of the same colour are to be put into different buckets, then they have no relation to each other, so they may as well as have different colours.
So we can replace a balls colour c, with (c,b) where b is the bucket it is to be put into.

Then the problem becomes simply checking when the a colour count reaches Q at some point. Code is below:"""

def solution(N, Q, B, C):
  # defaultdict is jus a dictionary with key values initialized to 0; it is just a cheap fix for manually setting new occurrences to 0 (avoids unnecessary if else clauses)
  from collections import defaultdict
  # count is a dictionary that counts the number of occurrences of our 'hybrid colour' found in D, so far
  count = defaultdict
  # the max_depth variable keeps track of the maximal number of occurrences of a 'hybrid colour' there is
  max_depth = 0
  D = B.copy()
  for i in range(0, len(B)):
    D[i] = (B[i], C[i])
  for i in range(0, len(B)):
    count[D[i]] = count[D[i]] + 1
    max_depth = max(max_depth, count[D[i]])
    if max_depth == Q:
    return i
  #Now if the 'return i' statement never gets executed, the problem is impossible, so we return a value of -1
  return -1  
 
"""Temporal complexity: each for loop has M steps, and each step has O(1) complexity, so we have a complexity of O(M)
Spatial complexity: we have a dictionary count, which contains at most MN 'hybrid colours', as there are N buckets, and at most M colours, so 
count has complexity at most O(MN), and D has complexity O(M), like B and C, so we have a total spatial complexity of O(MN)."""
    
