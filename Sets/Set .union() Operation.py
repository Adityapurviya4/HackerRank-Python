# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
A = set(map(int,input().split()))

M = int(input())
B = set(map(int,input().split()))

print(len(A.union(B)))