# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

shoes = int(int(input()))
myshop = list(map(int, input().split()))
stock = Counter(myshop)

customer = int(input())

earn = 0

for i in range(customer):
    size, price = map(int, input().split())
    if stock[size] > 0:
        earn += price
        stock[size] -= 1
        
print(earn)