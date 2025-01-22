def main():
    arr3 = [8, 1, 10, 13, 2 , 3, 12, 5, 9, 11, 4, 7, 6]
    print(merge_sort(arr3))
    # prints : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def combine(arr1, arr2): #combines two sorted arrays in one sorted array
    res = []
    i,j = 0, 0
    #sorts every value one by one in the two arrays
    while i<len(arr1) and j<len(arr2) :
        if arr1[i]<=arr2[j] :
            res.append(arr1[i])
            i+=1
        else :
            res.append(arr2[j])
            j+=1
    #add the leftovers if there is
    if i<=len(arr1)+1 :
        for x in range (i, len(arr1)):
            res.append(arr1[x])
    if j<=len(arr2)+1 :
        for x in range (j, len(arr2)):
            res.append(arr2[x])
    return res

def merge_sort(arr): #recursively splits the array into single elements [*], then combine them recursively into a sorted array
    if len(arr) <=1:
        return arr
    mid = len(arr)//2 
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])
    return combine(left, right)

main()