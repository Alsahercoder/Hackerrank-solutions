import math
from collections import deque

def downToZero(num):

    memset = set()
    count = 0
    queue = deque([[num, count]])

    while queue:

        num, count = queue.popleft()

        if num <= 1:

            if num == 1:
                count += 1
            break

        if num - 1 not in memset:
            memset.add(num-1)
            queue.append([num-1, count+1])

        ub = int(math.sqrt(num))

        # For finding the highest factor in reverse order
        for i in range(ub, 1, -1):
            if num % i == 0:
                
                factor = num // i
                if factor not in memset:
                    memset.add(factor)
                    queue.append([factor, count+1])
    return count

if __name__ == '__main__':
    
    n = int(input())
    for i in range(0, n):
        
        q = int(input())
        result = downToZero(q)
        print(result)
