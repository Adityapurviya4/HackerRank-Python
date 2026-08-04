import numpy



n ,m = map(int, input().split())

my_aaray = []
for _ in range(n):
    my_aaray.append(list(map(int, input().split())))
    
arr = numpy.array(my_aaray)
print(numpy.max(numpy.min(arr,axis=1)))