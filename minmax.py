#def set_min  (A):
    #mini = float('inf')
    #for num in A:
        #if num < mini:
            #mini = num 
        #return mini
    
#def set_max (A):
        #maxi = float('-inf')
        #for num in A:
            #if num > maxi:
                #maxi = num 
        #return maxi

#if __name__ == "__main__":
    #A = [4, 9, 6, 5, 2, 3]
    #N = len(A)
    #print("Minimum element is:", set_min(A))
    #print("Maximum element is:", set_max(A))


A = [4, 9, 6, 5, 2, 3]
A.sort()

print ("Minimum element is:", A[0])
print ("Maximum element is:", A[-1])

def getminmax (arr):
    arr.sort()
    minmax = {"min":arr[0], "max":arr[-1]}
    return minmax
arr = [1000, 11, 445, 1, 330, 3000]
minmax = getminmax(arr)

print("Minimum element is", minmax["min"])
print("Maximum element is", minmax["max"])