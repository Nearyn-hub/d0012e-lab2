# adapted from https://www.geeksforgeeks.org/maximum-sum-subarray-using-divide-and-conquer-set-2/

# class to hold various sums for current subarray
class Sum:
    def __init__(self, v):
        self.total = v      # all elements in subarray summed up
        self.maxSum = v     # largest sum calculated so far
        self.maxSuffix = v  # max suffix (a[max] downto a[k] for some k) so far
        self.maxPrefix = v  # max prefix (a[0] upto a[k] for some k) so far

def maxSubArray(a, low, high): 
    if low == high:
        return Sum(a[low]) # first step; current element is the only
                           # value listed for all sums

    # divide step (standard)
    mid = (low + high) // 2
    left = maxSubArray(a, low, mid)
    right = maxSubArray(a, mid+1, high)


    # combine step; combine left and right into a new list
    # and pass along the combined sums (sort of like merge step)
    nextSum = Sum(0) # sums to be passed along

    # next total= left total + right total
    nextSum.total = left.total + right.total
    
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

    # next max = next pfx, next sfx, next sum
    #            left max, right max,
    #            crossing element (left sfx + right pfx)
    nextSum.maxSum = max(nextSum.maxPrefix,
                         nextSum.maxSuffix,
                         nextSum.total,
                         left.maxSum,
                         right.maxSum,
                         left.maxSuffix + right.maxPrefix)
    return nextSum


# base case (c1) = const O(1)
# divide step = 2*T(n/2)
# combine step (c2) = const O(1)

# T(n) = 2 * T(n/2) + (c1 + c2)
# samam resonemang som 1.DAC
# T(n) = O(n)

    
# Driver function to check the above function
a  = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, 7]
print ("Maximum contiguous sum is", maxSubArray(a, 0, len(a)-1).maxSum)

