inversions = 0
def mergesort(arr):

    global inversions
    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        lIndex = rIndex = index = 0

        while lIndex < len(left) and rIndex < len(right):

            if left[lIndex] <= right[rIndex]:
                
                arr[index] = left[lIndex]
                index += 1
                lIndex += 1
                
            else:

                arr[index] = right[rIndex]
                index += 1
                rIndex += 1
                # cause all the elements in the left array are inverted
                # from the current left index value. so, all those are inverted
                investions += len(left) - lIndex
        
        while lIndex < len(left):

            arr[index] = left[lIndex]
            lIndex += 1
            index += 1
            
        while rIndex < len(right):

            arr[index] = right[rIndex]
            rIndex += 1
            index += 1

if __name__ == "__main__":

    tt = int(input())
    for i in range(0, tt):

        invertions = 0
        size = int(input())
        arr = list(map(int, input().split()))
        mergesort(arr)
        print(inversions)

