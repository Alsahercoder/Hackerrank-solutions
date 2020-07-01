// https://www.hackerrank.com/challenges/c-tutorial-functions
#include <iostream>
#include <cstdio>
#include <valarray>
using namespace std;

//used the concept of Valarray

int max_of_four(int a, int b, int c, int d)
    {   
        
        int val[]={a, b, c, d};
        valarray<int> valArr (val, 4);
        return valArr.max();
       
    }
int main()
{
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
