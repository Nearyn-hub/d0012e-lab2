def smallest(a):
    if a[1] < a[0]:                 # c1: 6 * O(1)
        a[0], a[1] = a[1], a[0]     
    if a[2] < a[1]:                 
        a[1], a[2] = a[2], a[1]     
        if a[1] < a[0]:             
            a[0], a[1] = a[1], a[0]
            
    f, s, t = a[0], a[1], a[2]      # c2: 3 * O(1)
    for e in a[3:len(a)]:           # always executes n-3 times
        if e < f:                   # c3: 4 * O(1)
            t = s                   
            s = f                    
            f = e                   
        elif e < s:                 # c4: 3 * O(1)
            t = s                   
            s = e                     
        elif e < t:                 # c5: 2 * O(1)
            t = e                   
    return (f, s, t)                # c6: O(1)

# time complexity: f(n) = c1 + c2 + c6 + (n-3)(c3 + c4 + c5)
# O(f(n)) = O(n-3) = O(n) - O(1) = O(n) 




# c1: 6 * O(1)
def sortSublist(a):                 
    if a[1] < a[0]:                 
        a[0], a[1] = a[1], a[0]     
    if a[2] < a[1]:                 
        a[1], a[2] = a[2], a[1]     
        if a[1] < a[0]:             
            a[0], a[1] = a[1], a[0]
    return a

# c2: using input size 3 for all lists, this function becomes independent of input size
# n and therefore will be linear.
# 6 * O(1) (all elements get sorted)
def merge(l, r):                        
    ret = []                            
    while len(l) > 0 and len(r) > 0:    
        if l[0] > r[0] or l[0] == r[0]: 
            ret.append(r[0])
            del r[0]
        elif r[0] > l[0]:
            ret.append(l[0])
            del l[0]     
    for el in l:
        ret.append(el)
    for er in r:
        ret.append(er)
    return ret

# T(n) = c3 + 2 * T(n/2) + c2
def smallestDAC(a):
    if len(a) == 3:
        return sortSublist(a)   # c3: Base case, 2 * O(1) + c1
    mid = len(a) // 2
    l = smallestDAC(a[mid:])
    r = smallestDAC(a[:mid])
    ret = merge(l, r)[0:3]
    return ret

# time complexity: T(n) = 2*T(n/2) + (c2 + c3)
# M.T: a = 2,  b=2,  f(n) = const = n^0
# log_b(a) = 1 > log_b(f(n)) = 0; case 1 (https://www.programiz.com/dsa/master-theorem)
# T(n) = n^log_b(a) = n^1 = O(n)


print(smallestDAC([2, 3, 1]))
arr = [27, 5, 13,
       28, 25, 48,
       54, 56, 64,
       64, 62, 1]
print(smallestDAC(arr))
