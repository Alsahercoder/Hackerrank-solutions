    # source : https://www.hackerearth.com/submission/53007462/
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())
     
    for i in range(0, n):
    	if arr[i] == key:
    		print(i)
    		break
    	else:
    		continue
