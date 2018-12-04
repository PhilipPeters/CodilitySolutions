"""Solution to the problem Nickel 2018, link can be found here: https://app.codility.com/programmers/task/pascal_triangle/
Short version of the problem: Compute the number of "True" values in an OR-Pascal-triangle structure.

Note it is actually easier to calculuate the number of 'FALSE' values, then subtract it from the total number of nodes.
If the length of the array is n, then we have (n) + (n-1) + (n-2) + ... + 2 + 1 = n(n+1)/2 total nodes.
Now if we just focus on the structure of the and values, we can see that if we look at the array given, i.e. the base of the 
Pascal's Triangle structure, if we have a continuous sub-array of FALSE values, say with length k, then they form exactly a sub-Pascal's triangle
of height = k, i.e. k(k+1)/2 nodes. So we only need to work out how many of these sub-continuous arrays, and what length they are,
then sum the number of False nodes this calculuates, then subtract this from the total number nodes in the tree:

We can calculate the total number of 'FALSE' nodes with an 'online method', all we need to do is record the total sum, and record the 
length of the current sub array we are on, then add it to our total, as seen in the code below:"""

def node_count(arr):
  cur_size = 0
  sum = 0
  for i in range(0, len(arr)):
    if arr[i] == False:
      cur_size = cur_size + 1
      sum = sum + cur_size
    else:
    arr[i] == True:
      cur_size = 0
  return len(arr)*(len(arr) + 1) / 2 - sum    
  
"""Temporal complexity: O(n), as we have n steps in our for loop, and we perform O(1) calculations at each step.
Spatial complexity: O(1), we only store i, the position in the loop, and cur_size and sum."""
