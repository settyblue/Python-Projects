__author__ = 'rakshith'
import math

print 'Hello World'
array = [1,2,1,3,4,2,3]
hashmap = {}
window = 2
sum = 0
print range(window)
for i in range(window):
    if hashmap.has_key(array[i]) == False:
        hashmap[array[i]] = 0
    hashmap[array[i]] = hashmap[array[i]]+ 1
    if hashmap[array[i]]==1:
        sum += array[i]

print hashmap
for i in range(window,len(array)):
    j = i - window
    tempsum = sum
    #print j," ",i,"  ",array[i]," ",tempsum," ",hashmap
    if hashmap[array[j]] == 1:
        hashmap.pop(array[j])
        tempsum -= array[j]
    else:
        hashmap[array[j]]-=1

    if hashmap.has_key(array[i]):
        hashmap[array[i]]+=1
    else :
        hashmap[array[i]]=1
        tempsum += array[i]
    sum = max(sum,tempsum)

print sum