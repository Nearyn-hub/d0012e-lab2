# class to hold various sums for current subarray
class Sum:
    def __init__(self, v):
        self.total = v
        self.maxSum = v
        self.maxSuffix = v
        self.maxPrefix = v

def maxSubArray(a, low, high):
    if low == high:
        return Sum(a[low]) # first step; current element is the only
                           # value listed for all sums

    # divide step (standard)
    mid = (low + high) // 2
    left = maxSubArray(a, low, mid)
    right = maxSubArray(a, mid+1, high)

    # combine step
    nextSum = Sum(0) # sums to be passed along

    # next pfx = pfx left, sum left + pfx right
    #            sum left + sum right
    nextSum.maxPrefix = max(left.maxPrefix,
                            left.total + right.maxPrefix,
                            left.total + right.total)

    # next sfx = sfx right, sum right + left sfx
    #           sum left + sum right
    nextSum.maxSuffix = max(right.maxSuffix,
                            right.total + left.maxSuffix,
                            right.total + left.total)

    # next total= left total + right total
    nextSum.total = left.total + right.total

    # next max =
    nextSum.maxSum = 0
    
    return nextSum

    
# Driver function to check the above function
a  = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, 7]
print ("Maximum contiguous sum is", maxSubArray(a, 0, len(a)-1).maxSum)

