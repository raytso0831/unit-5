#Ray Tso
#5/7/18
#quiz.py

def penultimate(A):
    return(A[len(A)-1])
    
def plusEquals(X,Y):
    for i in range(0,len(B)):
        X[i] += Y
    return Y


    
def smallest(B):
    B1 = B[0]
    for i in B:
        if i<B1:
            B1 = i
    return B1
    
    
print(penultimate(['clock','table','computers']))
print(plusEquals([1,2,3,4],10))
print(smallest([3,-1,5,-2,7,-4,1]))
