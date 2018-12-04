"""Problem link here: https://app.codility.com/programmers/task/longest_nonnegative_sum_slice/

Short version: Given an array consisting of the integers -1, 0 and 1, find the longest slice with a non-negative sum.

The solution will involve the prefix sum of the array, e.g. say A is the array to be worked on, then B[i] = A[0] + A[1] + ... + A[i]

The solution follows along the lines of dynamic programming: we work through the array element by element:
Say we are at position i. 
Then if B[i] >= 0, then the longest sub-array is 0 : i.
Otherwise, we have 2 cases. 
Suppose there is a j, such that j < i, and B[j] = B[i]. 
Then the longest sub-array is i: j (note this is because the array B is 'continuous', in the sense that as we 
go across the array, elements can increase or decrease by at most 1), or max_slice length we already had, whichever is bigger. 
If there is no such j, then B[i] is the smallest sum seen so far, 
so the maximum sub-array cannot involve position i, i.e. it remains unchanged. We implement this in the code below."""



def max_sub_slice(arr):
  """Note instead of explicitly creating the prefix-sum array, we can just use a running 'sum' variable to replicate B[i], as we only need
  the value of B[i] at step i, not the whole array"""
  sum = 0
  max_slice = 0
  """This records past instances of values of B[i] we want to track. It stores the key as the B[i] value, and the value as its first position"""
  myDict = {}
  for i in range(0, len(arr)):
    sum = sum + arr[i]
    if sum >= 0:
      max_slice = i + 1
    elif sum in myDict.keys():
      max_slice = max(max_slice, i - myDict[sum])
    else:
      myDict[sum] = i
  return max_slice
  
  
"""Temporal Complexity: Worst case, Best case (and therefore amortized) complexity are all O(n), since we do O(1) operations at each step.
Spatial Complexity: O(n), since it is just the dictionary myDict, which has size at most O(n) (only n values of sum can be taken), and the values sum and max_slice."""
