#User function Template for python3

class Solution:
    def sumOfRowCol(self,N,M,A):
        flag = True
        n = min(N,M)
        
        for i in range(n):
            row_sum, col_sum = 0,0
            for row_index in range(N):
                 row_sum += A[row_index][i]
            for col_index in range(M):
                 col_sum += A[i][col_index]
            if row_sum != col_sum:
               flag = False
        if flag:
            return 1
        else:
            return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.sumOfRowCol(N,M,A))
# } Driver Code Ends