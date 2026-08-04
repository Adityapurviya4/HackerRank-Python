# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
a = set(map(int, input().split()))

M = int(input())
b =set(map(int, input().split()))

print(len(a.symmetric_difference(b)))