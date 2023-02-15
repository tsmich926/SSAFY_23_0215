def backtrack(a,k,input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if  k == input:
        for i in range(1,k+1):
            print(a[i], end= " ")
        print()
    else:
        k += 1
        ncandidataes = construct_candidates(a,k,input,c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a,k,input)





#부분집합
def f(i, k):
    if i == k:
        print(bit)
    else:
        bit[i] = 1
        f(i+1,k)
        bit[i] = 0
        f(i+1,k)


A = {1,2,3}
N = len(A)
bit = [0] *N
f(0, N)