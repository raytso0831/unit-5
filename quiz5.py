#Ray Tso
#5/7/18
#quiz.py

def penultimate(A):
    return(A[len(A)-1])
    
def plusEquals(B,C):
    for i in range(0,len(B)):
        B[i] += C
    return C


    
def smallest(D):
    D1 = D[0]
    for i in D:
        if i<D1:
            D1 = i
    return D1
    
    
print(penultimate(['clock','table','computers']))
print(plusEquals([1,2,3,4],10))
print(smallest([3,-1,5,-2,7,-4,1]))
