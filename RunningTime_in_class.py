#Problem: Function that takes a list as input; it returns True if there are any # duplicates and False otherwise.
import time
import matplotlib.pyplot as plt 

# O (n^2)
def dup1(L):
    for i in range(len(L)):
        for j in range(len(L)):
            if i != j and L[i] ==  L[j]:
                return True 
    return False 
    # n(n(3+1))+1 = 4n^2 +1 = O(n^2)

# O(n^2) improved: Eliminating situations where we are repeating, doing unnecessary, and redundant steps.
def dup2(L):

    for i in range(1, len(L)): 
        for j in range(i):
            if L[i] == L[j]:
                return True 
        
        return False
    
# n(n(1+1))+1 = O(n^2)
    
