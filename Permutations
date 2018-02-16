
def permutation(str, C, A):

    for j in range(0, len(C)):
        new = str + C[j]
        D = C[:j]+C[j+1:]
        if len(new)==len(A):
            print (j, " ", new)
        permutation(new, D, A)

    return

A = 'DEFGHIJK'

for i in range(0, len(A)):
    str = A[i]  #initialize string
    C=A[:i]+A[i+1:]  #delete initial letter from remainder
    print (i)
    permutation(str, C, A)
