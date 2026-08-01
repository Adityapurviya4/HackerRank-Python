if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sorted = list(set(arr))
    sorted.sort() 
    
    print(sorted[-2])