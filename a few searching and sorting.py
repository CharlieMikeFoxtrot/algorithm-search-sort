'''
A sequential search is O(n) for ordered and unordered lists.

A binary search of an ordered list is O(logn) in the worst case.

Hash tables can provide constant time searching.

A bubble sort, a selection sort, and an insertion sort are O(n2) algorithms.

A shell sort improves on the insertion sort by sorting incremental sublists. It falls between O(n) and O(n2).

A merge sort is O(nlogn), but requires additional space for the merging process.

A quick sort is O(nlogn), but may degrade to O(n2) if the split points are not near the middle of the list. It does not require additional space.


'''
#Binary search

def binarySearch(alist, item):
    
    #Set beginning of list
    low = 0
    #set end of list
    high = len(alist) - 1
    #set found flag
    found = False
    
    #While low-end is smaller than high end, and have not found the item
    while low <= high and not found:
        
        #set mid point to middle of low and high end
        midpoint = (low+high) // 2
        
        #if you found the item at your search point set found to true
        if alist[midpoint] == item:
            #alternativly you could just return true and have false return at the end
            found = True
        
        
        #if the item was not found then adjust search area
        else:
            #if the item found is smaller than the item adjust high end of list to midpoint
            if item < alist[midpoint]:
                #move high end to mid point -1 becuase we can exclude midpoint from the search
                #because we already know mid point is not the item we're looking for
                high = midpoint - 1
            
            #if the the item is not too big and we didn't find the item then it must be too small
            else:
                #adjust the search area lower end to midpoint +1
                #because we already know mid poitn is not the item we're looking for we can exclued it by adding + 1
                low = midpoint + 1
                

        
    #return founds, False if item not found True if item was found
    return found
    
    
    

print(binarySearch([0, 1, 2, 8, 13, 17, 19, 32, 42],4))

#binary search RECURSIVE

def RECbinarySearch(alist,item):
    
    if len(alist) == 0:
        return False
    
    else:
        midpoint = len(alist)//2
        
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] > item:
                return RECbinarySearch(alist[0:midpoint-1],item)
            else:
                return RECbinarySearch(alist[midpoint+1:len(alist)],item)
            
        
print(RECbinarySearch([0, 1, 2, 8, 13, 17, 19, 32, 42],2))   
    
    
# BUBBLE SORT

def bubbleSort(alist):
    #iterate over the length of the list-1 backwards
    #remove 1 because we're comparing i+1 and it would be out of range otherwise
    for num in range(len(alist)-1,0,-1):
        #compare to every number leading up to top end
        for pos in range(num):
            #if number to the left is larger than number on right, swap them
            if alist[pos]> alist[pos+1]:
                alist[pos], alist[pos+1] = alist[pos+1], alist[pos]
                
#bubbls sort stop short if no changes
def bubbleShort(alist):
    
    for num in range(len(alist)-1,0,-1):
        swap = False
        for pos in range(num):
            
            if alist[pos]> alist[pos+1]:
                alist[pos], alist[pos+1] = alist[pos+1], alist[pos]
                swap = True
                
        if not swap:
            break
                
                
l = [4,5,6,2,1,2,3,9,9]
bubbleSort(l)
print(l)
bubbleShort(l)
print(l)




# SELECTION SORT

#finds largest value puts it at end of list
def selectionSort(alist):
    
    #find position to fill at end of list and work way towards the beginning
    for fillPos in range(len(alist)-1,0,-1):
        
        #set default max position to 0
        maxPos = 0
        
        #check every position in list excluding 0 because it's our default value
        #fillPos+1 because it wouldn't extend to the end of the list otherwise
        for location in range(1,fillPos+1):
            
            #if number at location is bigger than number at current biggest position
            if alist[location] > alist[maxPos]:
                
                #new biggest equals current location
                maxPos = location
        
        #swap fill position and current max position
        alist[maxPos],alist[fillPos] = alist[fillPos], alist[maxPos]


l = [9,4,5,6,2,1,2,3,9]
selectionSort(l)
print(l)

# INSERT SORT
def insertSort(alist):
    #go over every index in alist excluding 0
    for index in range(1,len(alist)):
        
        #set current value to value at index
        currentValue = alist[index]
        #set current position to index
        pos = index
        
        #while position is > 0 and CurrentValue is Greater than pos-1
        while pos > 0 and alist[pos-1] > currentValue:
            alist[pos] = alist[pos-1]
            pos = pos - 1
            
        alist[pos] = currentValue

l = [9,4,5,6,2,1,2,3,9]
insertSort(l)
print(l)


# MERGE SORT

def mergeSort(alist):
    print('splitting',alist)
    #if the list i longer than 1 number
    if len(alist) >1:
        #find mid point
        mid = len(alist) // 2
        #split list at mid point
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        #recursivly mergesort halves
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        #initalize 3 values for left right and list valuse
        i = 0 
        j = 0
        k = 0
        
        #while i and k are inside the list range
        while i < len(lefthalf) and j < len(righthalf):
            #if left lowest value is smaller than right smallest
            if lefthalf[i] < righthalf[j]:
                #add left to list
                alist[k] = lefthalf[i]
                #increment i
                i+=1
            
            #else aka if right is smaller or they're the same
            else:
                #add right value to list
                alist[k] = righthalf[j]
                #increment j
                j+=1
            #increment place since a value has been added at current place
            k+=1
            
        #while there are still values in left half
        while i < len(lefthalf):
            #add left value to k
            alist[k] = lefthalf[i]
            i+=1
            k+=1
            
        #place remaining righthalf values
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j+=1
            k+=1
            
        print('Merging', alist)

t = [54,26,93,17,77,31,44,55,20]
mergeSort(t)
print(t)







    