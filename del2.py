# solution adapted from  https://personal.utdallas.edu/~daescu/maxsa.pdf

class Sum:
    def __init__(self, cs, ms, msfx, mpfx):
        currentSum = cs
        maxSum = ms
        maxSuffix = msfx
        maxPrefix = mpfx
        
    totalSum = 0    #
    maxSum = 0      #
    maxSuffix = 0   #
    maxPrefix = 0   #
    

def maxSubArray(a, low, high):
    # base case; "list" is length 1, all sums are the current element
    if l==h: 
        return Sum(a[low], a[low], a[low], a[low])

    # recursion step
    mid = (low + high) // 2
    leftChild = maxSubArray(a, low, mid)
    rightChild = maxSubArray(a, mid + 1, high)

    # compare the results of previous sum steps
    nextSum = Sum()
    nextSum.
    return nextSum
    
    
    
    
# Driver function to check the above function
a  = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, 7]
print ("Maximum contiguous sum is", maxSubArray(a, 0, len(a)-1))

