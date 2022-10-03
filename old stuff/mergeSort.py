
def merge(arr,left_arr,rigth_arr,mid):
    l = 0
    r = 0
    k = 0
    inv_count = 0
    while l < len(left_arr) and r < len(rigth_arr):
        if rigth_arr[r]>left_arr[l]:
            arr[k]=left_arr[l]
            l+=1
        else:
            arr[k]=rigth_arr[r]
            r+=1
            inv_count += mid-1
        k+=1
    
    while l < len(left_arr):
        arr[k] = left_arr[l]
        l+=1
        k+=1
    
    while r < len(rigth_arr):
        arr[k] = rigth_arr[r]
        r+=1
        k+=1
    print(inv_count)
    return inv_count

def mergeSort(arr):
    if not len(arr)>1:
        return
    #divide array in two halves
    mid = len(arr)//2
    left_arr = arr[:mid]
    rigth_arr = arr[mid:]

    #recursion untill array size is 1 (then its sorted!)
    inv_count = mergeSort(left_arr)
    inv_count += mergeSort(rigth_arr)

    inv_count += merge(arr,left_arr,rigth_arr,mid)

    return inv_count
    #checking left most item from each sorted array
        

x = [4,1,2,3,6,7,8,5]

print(mergeSort(x))
print(x)