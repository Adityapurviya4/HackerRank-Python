N = int(input())
a = set(map(int, input().split()))

M = int(input())

for _ in range(M):
    command = input().split()

    if command[0] == "pop":
        a.pop()
    elif command[0] == "remove":
        a.remove(int(command[1]))
    else:
        a.discard(int(command[1]))

print(sum(a))