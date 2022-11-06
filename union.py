from mergeSort import mergeSort

def combineArrays(A,B):
    '''Given Two sorted arrays A,B Unions them into Array C removing duplicates and maintaining sorted order (Stable)'''
    C=[None]*(len(A)+len(B))
    c1 = c2 = c3 = 0
    # Copy data to temp arrays A,B
    while c1 < len(A) and c2 < len(B): #O(n)
        try:
            if A[c1]==A[c1+1] and (c1+1)<len(A):
                c1+=1

            if B[c2]==B[c2+1] and (c2+1)<len(B):
                c2+=1

            elif A[c1]>B[c2]: #O(1)
                C[c3]=B[c2]
                c2+=1

            elif A[c1]<B[c2]: #O(1)
                C[c3]=A[c1]
                c1+=1

            elif A[c1]==B[c2]: #O(1)
                if A[c1]==B[c2+1]:
                    c2+=1
                elif A[c1+1]==B[c2]:
                    c1+=1
                else:
                    C[c3]=A[c1]
                    c1+=1
                    c2+=1
        except:
            if A[c1]>B[c2]: #O(1)
                C[c3]=B[c2]
                c2+=1

            elif A[c1]<B[c2]: #O(1)
                C[c3]=A[c1]
                c1+=1

            elif A[c1]==B[c2]: #O(1)
                try:
                    if A[c1]==B[c2+1]:
                        c2+=1
                    elif A[c1+1]==B[c2]:
                        c1+=1
                except:
                    C[c3]=A[c1]
                    c1+=1
                    c2+=1
        c3 += 1
    # If cursor check terminated prematurely, loop over A,B to add missed values
    while c1 < len(A): #O(n)
        C[c3] = A[c1]
        c1 += 1
        c3 += 1

    while c2 < len(B): #O(n)
        C[c3] = B[c2]
        c2+= 1
        c3+= 1

    C=[v for v in C if v is not None] #O(n)

    return C

def mergeNSortedArrays(listOfSets):
    finalArray=combineArrays(listOfSets[0],listOfSets[1]) #O(1)
    incrementer=2 #O(1)
    while incrementer<len(listOfSets): #O(n)
        finalArray=combineArrays(finalArray,listOfSets[incrementer]) #O(n)
        incrementer+=1 #O(1)

    return finalArray

def unionTestFunction(listofSets):
    C=[]
    for set in listofSets:
        for value in set:
            if value not in C:
                C.append(value)
    return sorted(C)


if __name__=="__main__":
    A=[2,10,2,2,4,6,8,10]
    B=[12,2,2,2,8,19]
    C=[11,8]
    D=[19,11,7,4,99,10,7]
    E=[8,6,2,4,7,6,3,1,0,10,2,12,6,4]

    listofArrays=[A,B,C,D,E]
    mergeAll=[mergeSort(x) for x in listofArrays]

    print(unionTestFunction(listofArrays))

    print(mergeNSortedArrays(listofArrays))


