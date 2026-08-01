if __name__ == '__main__':
    N = int(input())
    
mylist = []

for i in range(0,N):
    comm = input().split()
    
    if(comm[0] == "insert"):
        mylist.insert(int(comm[1]), int(comm[2]))
    elif(comm[0] == "print"):
        print(mylist)
    elif(comm[0] == "remove"):
        mylist.remove(int(comm[1]))
    elif(comm[0] == "append"):
        mylist.append(int(comm[1]))
    elif(comm[0] == "sort"):
        mylist.sort()
    elif(comm[0] == "pop"):
        mylist.pop()
    elif(comm[0] == "reverse"):
        mylist.reverse()
