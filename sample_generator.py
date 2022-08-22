def next_permutation(L):
    '''
    Permute the list L in-place to generate the next lexicographic permutation.
    Return True if such a permutation exists, else return False.
    '''
     
    n = len(L)
    i = n - 2
    while i >= 0 and L[i] >= L[i+1]:
        i -= 1
     
    if i == -1:
        return False
 
    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1
    
    L[i], L[j] = L[j], L[i]
     
    left = i + 1
    right = n - 1
 
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
             
    return True

with open('in.txt', 'w') as f:
    s=['a']*10+['b','b']
    i=1;
    while True:
        f.write(''.join(s)+' '+str(i)+'\n')
        i+=1
        if next_permutation(s) == False:
            break