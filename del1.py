def smallest(a):
    if a[1] < a[0]:                 # c1: O(6)
        a[0], a[1] = a[1], a[0]     
    if a[2] < a[1]:                 
        a[1], a[2] = a[2], a[1]     
        if a[1] < a[0]:             
            a[0], a[1] = a[1], a[0] 
            
    f, s, t = a[0], a[1], a[2]      # c2: O(3)
    for e in a[3:len(a)]:           # always executes n-3 times
        if e < f:                   # c3: O(4)
            t = s                   
            s = f                    
            f = e                   
        elif e < s:                 # c4: O(3)
            t = s                   
            s = e                     
        elif e < t:                 # c5: O(2)
            t = e                   
    return (f, s, t)                # c6: O(1)

# time complexity: f(n) = c1 + c2 + c6 + (n-3)(c3 + c4 + c5)
# O(f(n)) = O(n-3) = O(n) - O(3) = O(n) 

# number of comparisons (best-case): 3 + n
# number of comparisons (worst-case): 3 + 3n



def sortSublist(a):
    if a[1] < a[0]:                 # c1: O(6)
        a[0], a[1] = a[1], a[0]     
    if a[2] < a[1]:                 
        a[1], a[2] = a[2], a[1]     
        if a[1] < a[0]:             
            a[0], a[1] = a[1], a[0]
    return a

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

def smallestDAC(a):
    if len(a) == 3:
        return sortSublist(a)
    mid = len(a) // 2
    l = smallestDAC(a[mid:])
    r = smallestDAC(a[:mid])
    ret = merge(l, r)[0:3]
    return ret

print(smallestDAC([2, 3, 1]))
arr = [27, 5, 13,
       28, 25, 48,
       54, 56, 64,
       64, 62, 1]
print(smallestDAC(arr))
