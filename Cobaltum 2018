"""This definitely seems like a dynammic programming problem, so let's try to find the optimal substructure:
If we go through the integers 1 to n, say we are at position i, and let our arrays be A and B.
Then if we look at the problem up until the i'th column, i.e. how many swaps we need to make A[0:i+1] and B[0:i+1] increasing,
we can look at either swapping A[i] and B[i], or not swapping them. Then compare these to the number of swaps needed to make A[0:i] and 
B[0:i] increasing, conditional on whether we swap the i-1'th column. Then we are keeping track of 2 running 'number of swaps', then at the end,
i.e. when i = n-1, we look at the maximum of these 2 numbers."""

def swaps(A, B):
  """These 2 numbers record how many swaps we have needed to make A[0:i+1] and B[0:i+1] increasing based on whether we swapped the i'th column or not"""
  swapped = 0
  noswapped = 0
  for i in range(0, len(A)):
    """This condition will check if it is actually possible: if not then we immediately break the loop and return -1, to say the problem is impossible"""
    if (A[i] <= A[i-1] and A[i] <= B[i-1]) or (B[i] <= A[i-1] and B[i] <= B[i-1]):
      return -1
    """Now we work out the new value of swapped, i.e. we are assuming we are swapping the i'th column, and the value of noswapped all in one go, 
    by checking if the i'th column is completely bigger than the i-1'th column as is, and whether it would be completely bigger if we swapped one column"""
    else:
      if (A[i] > A[i-1] and B[i] > B[i-1]) and (A[i] > B[i-1] and B[i] > A[i-1]):
        """Now we know that it doesn't matter what you do for the i'th column, so we just take the max value of noswapped and swapped, and add 1"""
        swapped = max(swapped, noswapped) + 1
        noswapped = max(swapped, noswapped)
      elif (A[i] > A[i-1] and B[i] > B[i-1]) and (A[i] <= B[i-1] or B[i] <= A[i-1]):
        """Now we know we have to do the same to the i'th column as the i-1'th column"""
        swapped = swapped + 1
        noswapped = noswapped
      elif (A[i] <= A[i-1] or B[i] <= B[i-1]) and (A[i] > B[i-1] and B[i] > A[i-1]): 
        """Now we know we have to do the opposite to the i'th column as the i-1'th column"""
        swapped = noswapped + 1
        noswapped = swapped
    return max(swapped, noswapped)
    
"""Temporal complexity: O(n), as we are doing O(1) comparisons at each step of the loop, which has n steps.
Spatial complexity: O(1), we only store 2 values: swapped and noswapped (as well as the i in the loop)."""
        
