n = int(input())

myset = set()

for _ in range(n):
   country = input().strip()
   myset.add(country)

print(len(myset))
