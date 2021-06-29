# Source: https://www.hackerearth.com/problem/algorithm/monk-and-the-collision/
# Author: Shaik Faizan Roshan Ali
# Date: 13th April 2021

if __name__ == "__main__":

    tt = int(input())

    for i in range(0, tt):

        size = int(input())
        ll = list(map(int, input().split()))
        hashmap = {}
        collisons = 0
        for val in ll:
            
            key = val % 10
            if hashmap.get(key) == None:
                hashmap[key] = val
            else:
                collisons += 1
        print(collisons)
