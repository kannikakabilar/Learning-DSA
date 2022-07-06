# Treap (Heap Tree)
"""
In a heap, the highest (or lowest) priority element is always stored at the root. 
However, a heap is not a sorted structure; it can be regarded as being partially ordered. 
A heap is a useful data structure when it is necessary to repeatedly remove the object 
with the highest (or lowest) priority, or when insertions need to be interspersed with removals of the root node.
"""

# Max-Heap data structure in Python
# Heapify is to convert a random binary tree into a max/min heap tree
# Heapify swap elements with parents (if needed) until it reaches root for each leaf node
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)

# Inserting an element, involves inserting at the end of a tree (as a leaf)
# and then working our way upwards using heapify
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum);
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)

# For deleting, select the node to be deleted - and swap it with the last leaf node
# Delete that node and heapify to restore heap tree properties
def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
        
    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)
    
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)
    
arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))