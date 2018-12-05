"""Solution to the Krypton 2018 problem, link here: https://app.codility.com/programmers/challenges/krypton2018/
Short version: Find a path in given matrix, such that the product of all the numbers on the path has the minimal number of trailing zeros.

We have a very strong optimal sub-structure: Suppose we have an optimal path. We know that the last element in our path is A[n-1][n-1], where
n is the height of our matrix, but the second last can be either A[n-2][n-1] or A[n-1][n-2]. If it is the first, our optimal path is the optimal path 
from A[0][0] to A[n-2][n-1], then to A[n-1][n-1], otherwise it is the optimal path from A[0][0] to A[n-1][n-2], then to A[n-1][n-1].

So we just need to compute this recursively. Note since we are in the dynammic programming paradigm, as to avoid overlapping subproblems, for each i, j in range(0, n-1),
we will calculate the answer for the sub-matrix of size ixj, using the reasoning above, proceeding in a a converging manner (i.e. we first work out the answer for the edges of the matrix, which is easy, as there is only one route.
Then we work outwards to inwards, for each row. 

Note the optimal substructure is far easier than in problems like Gallium 2018, because we just want to find the minimum of either the power of 2, or power of 5 over all paths.

This is described in the code below: """


"""First we need a function to work out the highest power of 2 and 5 dividing x"""
import numpy as np

def factor(x):
  pow2, pow5 = 0, 0
    
    if x == 0:
        return 1, 1
    while x and x % 2 == 0:
        x = x/2
        pow2 = pow2 + 1

    while x and x % 5 == 0:
        x = x/5 
        pow5 = pow5 + 1
    return np.array([pow2, pow5]) 
  
  """first we check if 0 is in our array: if it is, we can just pick a path containing 0 to guarantee an answer of at most 1, so if our final answer is >=1, and we have a 0 in our array, the answer is in fact 1.
  If the answer is <1, and there is an array, then 0 is the correct answer"""

  zero = False
  for i in range(0, len(A)):
    for j in range(0, len(A)):
      if A[i][j] == 0:
        zero = True
    
  """Now we work out the edge cases"""
  n = len(A)
  B = A.copy()
  for i in range(0, n):
    B[0][i] = B[0][i-1] + factor(A[0][i])
    B[i][0] = B[i-1][0] + factor(A[i][0])
  
  """now to finish the recursion"""
  for i in range(1, n):
    for j in range(1, n):
      B[i][j][0] = min(B[i-1][j][0] + factor(A[i][1])[0], B[i][j-1][0] + factor(A[i][1])[0])
      B[i][j][1] = min(B[i-1][j][1] + factor(A[i][j])[1], B[1][j-1][1] + factor(A[i][1])[1])
      
  if (1 - zero):
    return min(B[-1][-1][0], B[-1][-1][1])
  else:
    return min(min(B[-1][-1][0], B[-1][-1][1]), 1)
    
"""Temporal complexity: O(N^2), as we are building up the array B element by element.
Spatial Complexity: again O(N^2). 
  
