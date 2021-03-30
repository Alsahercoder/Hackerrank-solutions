

    # Binary Search
     
    def binarySearch(arr, key):
     
        mid = len(arr) // 2
        lowerbound = 0
        upperbound = len(arr) - 1
        
        flag = 0
        while lowerbound <= upperbound and flag == 0:
     
            mid = (lowerbound + upperbound) // 2
            if arr[mid] == key:
                flag = 1
                break
            
            elif key < arr[mid]:
                upperbound = mid - 1
            elif key > arr[mid]:
                lowerbound = mid + 1
            else:
                pass
     
            
            
        if flag == 1:
            print("YES", key, end = " ")
        else:
            print("NO", end = " ")
            flag = 0
     
        lowerbound = 0
        upperbound = len(arr) - 1
        while upperbound - lowerbound > 1:
     
            mid = (lowerbound + upperbound) // 2
            if arr[mid] > key:
                upperbound = mid
            elif arr[mid] <= key:
                lowerbound = mid + 1
     
        if arr[lowerbound] > key:
            upperbound = arr[lowerbound]
        elif arr[upperbound] > key:
            upperbound = arr[upperbound]
        else:
            upperbound = -1
        if flag == 0:
            print(upperbound, upperbound)
        else:
            print(upperbound)
        
    if __name__ == "__main__":
        
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
     
        tt = int(input())
        while tt > 0:
            
            key = int(input())
            binarySearch(arr, key)
            tt -= 1
            
     

Language: Python 3.8
