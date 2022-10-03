from operator import le
from turtle import right


def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        mergeSort(left_arr)
        mergeSort(right_arr)
        print(left_arr,right_arr)
        i=0
        j=0
        k=0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1

        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1

x = [1, 4, 7, 5, 6, 10, 9, 3, 8, 2]
mergeSort(x)
print(x)

def quickSort(arr,left,right):
    if left<right:
        pivot = partition(arr,left,right)
        quickSort(arr,left,pivot-1)
        quickSort(arr,pivot+1,right)

def partition(arr,left,right):
    l = left
    r = right -1
    pivot = arr[right]
    while l<r:
        while l<right and arr[l] <pivot:
            l+=1
        while r>left and arr[r]>=pivot:
            r-=1
        if l<r:
            arr[l],arr[r] = arr[r],arr[l]
    if arr[l]>pivot:
        arr[right],arr[l] = arr[l],arr[right]
    
    return l

x = [1, 4, 7, 5, 6, 10, 9, 3, 8, 2]
quickSort(x,0,len(x)-1)
print(x)