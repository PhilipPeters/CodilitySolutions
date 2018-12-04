"""As usual, we have an optimal sub-structure, so we proceed with dynamic programming. 
The key observation is to look at each index as having a vector associated with it. This will be explained, but first, we know at each point, we have only 36 (26 letters + 10 digits)
that can possibly be at a point i in the array. 
Then we set f(i) as the vector containing the number of occurences of each letter in the sub-array A[0:i], mod 2. 
Call this the signature. Then if a sub array has an even number of occurences of each character, the signatures at the endpoints are the same.

This will be demonstrated in the code below:"""


import string


LOWERCASE_LETTERS_AND_DIGITS_DICT = {letter: index for index, letter in enumerate(string.ascii_lowercase + string.digits)}


def solution(S):
    # the signatures data structure is a list, and for each index i, signature[i+1] contains the signature at point i
    signatures = [0]+[0]*len(S)
    for index, letter in enumerate(S):
        signatures[index+1] = signatures[index]^(1<<LOWERCASE_LETTERS_AND_DIGITS_DICT[letter])

    longestValidStringLength = 0
    # signature_endpoints_dict keeps track of the maximum and minimum positions where the signature is found
    signature_endpoints_dict = {}
    for index, signature in enumerate(signatures):
        if signature in signature_endpoints_dict:
            signature_endpoints_dict[signature] = (signature_endpoints_dict[signature][0], index)
        else:
            signature_endpoints_dict[signature] = (index, index)
    # given a signature, we know now that the longest sub-array, with endpoints both equal to this specific signature, has length = signatureExtremaDict[signature][1] - signatureExtremaDict[signature][0]
    # now given every signature, we just cycle through, and take the maximum length over all signatures
    for signature, endpoints in signature_endpoints_dict.items():
        length = max(length, max(endpoints)-min(endpoints))
    return length
    
"""Temporal complexity: O(N): each for loop  (there are 3) has at most N steps, and each step takes O(1) time.
Spatial complexity: O(N): keypoint to note is that each signature vector is only constant size (dimension 36), so signatures list is O(N) size,
and signature_endpoints_dict is again O(N)."""
