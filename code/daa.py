# Introduction: Algorithms
"""
Algorithms are the heart of computer science. They are the recipes for solving problems.
They are the building blocks of all modern computing systems.
They take in values or a set of values called inputs and produce a value or a set of values called outputs.
Algorithmic thinking is a way of solving problems that is not limited to computers.
It is a way of thinking that can be applied to any problem-solving situation.
"""
# Analyzing Algorithms
"""
An algorithm is a recipe for solving a problem. It is a set of instructions that specifies how to perform a computation.
The computation might be something mathematical
# such as solving a system of equations or finding the roots of a polynomial.
Or it might be a symbolic computation
# such as searching and replacing text in a document or compiling a program.
Or it might be a physical computation
# such as modeling the weather or finding the best route through a graph.
Or it might be something else.
"""
# Algorithms are not limited to computers.
"""
Algorithms are not limited to computers.
"""
# Complexity of Algorithms
"""
The efficiency of an algorithm is measured by the number of steps it takes to perform the computation.
"""

# Growth of Functions
"""
The growth of a function f(n) is a function that describes how f(n) behaves as the value of n increases.

There are two common ways to describe the growth of a function.

1. Asymptotic notation
2. Order of growth

Asymptotic notation describes the growth of a function as the value of n increases without regard to the constant factors.
Order of growth describes the growth of a function as the value of n increases while ignoring the lower order terms.

Asymptotic notation is a way of describing the growth of a function as the value of n increases without regard to the constant factors.
Order of growth is a way of describing the growth of a function as the value of n increases while ignoring the lower order terms.

The most common asymptotic notations are:

1. O-notation
2. Ω-notation
3. Θ-notation

O-notation describes the set of functions that grow more slowly than a specified function.
Ω-notation describes the set of functions that grow more quickly than a specified function.
Θ-notation describes the set of functions that grow at the same rate as a specified function.

The most common order of growth functions are:

1. Constant
2. Logarithmic
3. Linear
4. N log N
5. Quadratic
6. Cubic
7. Exponential
"""
# Constant
"""
A constant function is a function that has the same value for all inputs.
"""
# Logarithmic
"""
A logarithmic function is a function that has the form log b n.
"""
# Linear
"""
A linear function is a function that has the form n.
"""
# N log N
"""
A n log n function is a function that has the form n log n.
"""
# Quadratic
"""
A quadratic function is a function that has the form n2.
"""
# Cubic
"""
A cubic function is a function that has the form n3.
"""
# Exponential
"""
An exponential function is a function that has the form bn.
"""
# Big-O Notation
"""
Big-O notation describes the set of functions that grow more slowly than a specified function.
"""
# Omega Notation
"""
Omega notation describes the set of functions that grow more quickly than a specified function.
"""
# Theta Notation
"""
Theta notation describes the set of functions that grow at the same rate as a specified function.
"""
# Example
"""
The following table shows the growth of some common functions.

Function    Asymptotic Notation    Order of Growth
n           O(n)                   Linear
n2          O(n2)                  Quadratic
n3          O(n3)                  Cubic
2n          O(2n)                  Exponential
n log n     O(n log n)             N log N
log n       O(log n)               Logarithmic
n!          O(n!)                  Factorial
"""
# Example
"""
The following table shows the growth of some common functions.

Function    Asymptotic Notation    Order of Growth
n           Ω(n)                   Linear
n2          Ω(n2)                  Quadratic
n3          Ω(n3)                  Cubic
2n          Ω(2n)                  Exponential
n log n     Ω(n log n)             N log N
log n       Ω(log n)               Logarithmic
n!          Ω(n!)                  Factorial
"""
# Performance Measurements
"""
The performance of an algorithm can be measured by counting the number of steps it takes to perform the computation.
"""


# Sorting and Order Statistics - Shell Sort
"""
Shell sort is a generalization of insertion sort that allows the exchange of items that are far apart.
"""

# code for shell sort
def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2
        print("After increments of size", sublist_count, "The list is", a_list)


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(test_list)
print(test_list)


# calculating the time taken by the code
import timeit

code_to_test = """
def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
                    print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2
        print("After increments of size", sublist_count, "The list is", a_list)


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):

        current_value = a_list[i]

        position = i

        while position >= gap and a_list[position - gap] > current_value:

            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value
"""

# elapsed_time = timeit.timeit(code_to_test, number=100)/100

# print(elapsed_time)

# output

# --

# Sorting and Order Statistics - Merge Sort
"""
Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
"""

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves
        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

# --

# Quick Sort
"""
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.
Always pick first element as pivot.
Always pick last element as pivot (implemented below)
Pick a random element as pivot.
Pick median as pivot.
The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.
"""

# Python program for implementation of Quicksort Sort
# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = l - 1  # index of smaller element
    x = arr[h]
    for j in range(l, h):
        if arr[j] <= x:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


# Function to do Quick sort
def quickSortIterative(arr, l, h):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
    # initialize top of stack
    top = -1
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    # Keep popping from stack while is not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h)
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]

quickSortIterative(arr, 0, len(arr) - 1)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]),
# --

# Heap Sort
"""
Heap Sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for remaining element.

What is Binary Heap?
Let us first define a Complete Binary Tree. A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible (Source Wikipedia)

A Binary Heap is a Complete Binary Tree where items are stored in a special order such that value in a parent node is greater(or smaller) than the values in its two children nodes. The former is called as max heap and the latter is called min heap. The heap can be represented by binary tree or array.

Why array based representation for Binary Heap?
Since a Binary Heap is a Complete Binary Tree, it can be easily represented as array and array based representation is space efficient. If the parent node is stored at index I, the left child can be calculated by 2 * I + 1 and right child by 2 * I + 2 (assuming the indexing starts at 0).

What is Binary Heap used for?
Heaps are used for priority queue operations, and in graph traversal algorithms like Prim’s and Dijkstra’s.

How to build the heap?

Heapify procedure can be applied to a node only if its children nodes are heapified. So the heapification must be performed in the bottom up order.

Heap Sort Algorithm for sorting in increasing order:
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of tree.

3. Repeat above steps while size of heap is greater than 1.

Heap Sort Algorithm for sorting in decreasing order:
1. Build a min heap from the input data.
2. At this point, the smallest item is stored at the root
of the heap. Replace it with the last item of the heap
followed by reducing the size of heap by 1. Finally,
heapify the root of tree.

"""


# code to implement heap sort
def heapify(arr, n, i):

    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Heap sort
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

        # Driver code to test above


arr = [12, 11, 13, 5, 6, 7]

heapSort(arr)

n = len(arr)

print("Sorted array is")
for i in range(n):
    print("%d" % arr[i])

# --


# Comparison of Sorting Algorithms

# Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Python program for implementation of Selection
# Sort
def selectionSort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Python program for implementation of Insertion Sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Python program for implementation of Shell Sort


def shellSort(arr):
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n // 2
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already
    # in gapped order keep adding one more element
    # until the entire array is gap sorted
    while gap > 0:
        for i in range(gap, n):
            # add a[i] to the elements that have been gap
            # sorted save a[i] in temp and make a hole at
            # position i
            temp = arr[i]
            # shift earlier gap-sorted elements up until
            # the correct location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                # put temp (the original a[i]) in its correct
            # location
            arr[j] = temp
        gap //= 2
    return arr


# Python program for implementation of Merge Sort


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]
        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left  # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


# Python program for implementation of Quicksort Sort


def quickSort(arr):

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)


# Python program for implementation of Heap Sort


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        # Heap Sort
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        return arr


# To heapify a subtree rooted with node i which is # an index in arr[]. n is size of heap


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*

    r = 2 * i + 2  # right = 2* + 1

    # See if left child of root exists and is # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, largest)

        # The main function to sort an array of given size


def heapSort(arr):

    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Heap Sort
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Driver code to test above


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")


# Sorting in Linear Time.
"""
The sorting algorithm is based on counting sort that assumes that the input is composed of k different integers in the range [0, k-1].


The idea is to first create a count array to store the number of occurrences of each element in the input array. Next, we modify the count array such that each element at each index stores the sum of previous counts. This step gives us the position of each element in the output array. Finally, we iterate over the input array, get the count at each index from the count array, and place the element at the correct position in the output array. The overall time complexity of the algorithm is O(n+k) where n is the number of elements in input array and k is the range of input.
"""


def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = arr[i] // exp1
        count[(index) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        countingSort(arr, exp)
        exp *= 10


# Driver code to test above
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Sorted array is: ", end="")
print(arr)
radixSort(arr)
print("Sorted array is: ", end="")
print(arr)


# Advanced Data Structures: Red-Black Trees


# red-black tree properties
"""
1. A node is either red or black.
2. The root is black.
3. All leaves (NIL) are black.
4. Both children of every red node are black.
5. Every simple path from a node to a descendant leaf contains the same number of black nodes.
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = "red"
        self.size = 1

    def __str__(self):
        return str(self.key)


class RedBlackTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def insert(self, key):
        node = Node(key)
        if self.root is None:
            self.root = node
            self.root.color = "black"
            return
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.parent = parent
        if node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        self.fix_insert(node)
        self.root.color = "black"

    def fix_insert(self, node):
        while node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent  # continue
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
                    # node = node.parent.parent
        self.root.color = "black"

    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
            right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        else:
            if node == node.parent.left:
                node.parent.left = right_child
            else:
                node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
            left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        else:
            if node == node.parent.left:
                node.parent.left = left_child
            else:
                node.parent.right = left_child
        left_child.right = node

        node.parent = left_child

    def search(self, key):
        node = self.root
        while node is not None:
            if node.key == key:
                return node
            elif node.key > key:
                node = node.left
            else:
                node = node.right
        return None

    def minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def maximum(self, node):
        while node.right is not None:
            node = node.right
        return node

    def successor(self, node):
        if node.right is not None:
            return self.minimum(node.right)
        else:
            y = node.parent
            while y is not None and node == y.right:
                node = y
                y = y.parent
            return y

    def predecessor(self, node):
        if node.left is not None:
            return self.maximum(node.left)
        else:
            y = node.parent
            while y is not None and node == y.left:
                node = y
                y = y.parent
            return y

    def delete(self, key):
        node = self.search(key)
        if node is None:
            return
            # raise Exception("Key not found")
            # return
        if node.left is None or node.right is None:
            if node.parent is None:
                self.root = None
            else:
                if node == node.parent.left:
                    node.parent.left = (
                        node.left if node.left is not None else node.right
                    )
                else:
                    node.parent.right = (
                        node.left if node.left is not None else node.right
                    )
        else:
            y = self.successor(node)
            node.key = y.key
            node = y

        if node.left is not None:
            node.left.parent = node.parent
        if node.right is not None:
            node.right.parent = node.parent
        if node.parent is not None:
            if node == node.parent.left:
                node.parent.left = node.left if node.left is not None else node.right
            else:
                node.parent.right = node.left if node.left is not None else node.right

        return

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.key)
        self.inorder(node.right)
        return

    def preorder(self, node):
        if node is None:
            return
        print(node.key)
        self.preorder(node.left)
        self.preorder(node.right)
        return

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.key)
        return

    def levelorder(self, node):
        if node is None:
            return
        queue = [node]
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.key)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
                return


# B – Trees
"""
B-Trees are a special type of self-balancing binary search trees.


B-Trees are used in databases and file systems. They are also used in many other applications.

"""


def btree_insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = btree_insert(root.left, key)
    else:
        root.right = btree_insert(root.right, key)
    return root


# Fibonacci Heaps
"""
Fibonacci Heaps are a data structure that are used in many applications.

They are used in the implementation of Dijkstra's algorithm.

the properties of Fibonacci Heaps are:

1. Fibonacci Heaps are self-balancing binary trees.

2. Fibonacci Heaps are used in applications such as Dijkstra's algorithm

3. Fibonacci Heaps are used in applications such as the implementation of the Knapsack problem.


"""


class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.n = 0

    def __len__(self):
        return self.n

    def __bool__(self):
        return self.min is not None

    def insert(self, key):
        node = Node(key)
        if self.min is None:
            self.min = node
        else:
            node.left = self.min
            node.right = self.min.right
            self.min.right.left
            self.min.right = node
            if key < self.min.key:
                self.min = node
        self.n += 1

    def extract_min(self):
        if self.min is None:
            return None
        min = self.min
        if min.child is not None:
            min.child.parent = None
            self.min = min.child
            self.consolidate()
        else:
            self.min = None
        self.n -= 1
        return min

    def decrease_key(self, node, key):
        if key > node.key:
            return
        node.key = key
        parent = node.parent
        if parent is not None and node.key < parent.key:
            self.cut(node, parent)
            self.cascading_cut(parent)

        if node.key < self.min.key:
            self.min = node

    def cut(self, node, parent):
        node.left.right = node.right
        node.right.left = node.left
        if node is parent.child:
            parent.child = node.right
        node.parent = None
        node.mark = False
        self.n -= 1

    def cascading_cut(self, node):
        parent = node.parent
        if parent is not None:
            if node.mark is False:
                node.mark = True
            else:
                self.cut(node, parent)
                self.cascading_cut(parent)

    def consolidate(self):
        A = [None] * self.n
        node = self.min
        while node is not None:
            child = node.child
            while child is not None:
                sibling = child.right
                if A[child.degree] is None:
                    A[child.degree] = child
                else:
                    # merge two nodes
                    y = A[child.degree]
                    if y.mark is True:
                        self.cut(y, node)
                        self.cascading_cut(y)
                        y.mark = False
                    child.right = y.right
                    y.right.left = child
                    y.left = child.left
                    child.left.right = y
                    y.parent = child.parent
                    child.parent = y
                    y.mark = False
                    y.degree += 1
                child = sibling
            node = node.right
            node.child = None
        self.min = None
        for i in range(len(A)):
            if A[i] is not None:
                if self.min is None:
                    self.min = A[i]
                else:
                    self.min = self.merge(self.min, A[i])
                    self.min.parent = None

    def merge(self, x, y):
        if x.key > y.key:
            x, y = y, x
            x.right.left = x.left
            x.left.right = x.right
            x.left = x
            x.right = x
        y.left.right = y.right
        y.right.left = y.left
        x.degree += 1
        y.right = x.child
        y.left = x
        x.child.left = y
        x.child = y
        return x


# # driver code
# if __name__ == '__main__':
#     heap = FibonacciHeap()
#     heap.insert(5)
#     heap.insert(3)
#     heap.insert(17)
#     heap.insert(10)
#     heap.insert(84)
#     heap.insert(19)
#     heap.insert(6)
#     heap.insert(22)

#     print("The minimum value of Fibonacci Heap is " + str(heap.min.key))
#     print("The minimum value of Fibonacci Heap is " + str(heap.extract_min().key))
#     print("The minimum value of Fibonacci Heap is " + str(heap.extract_min().key))

# --

#  Tries


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# driver code
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("appl")
    trie.insert("apples")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.search("appl"))
    print(trie.search("apples"))
    print(trie.starts_with("app"))
    print(trie.starts_with("appl"))
    print(trie.starts_with("apples"))


# Skip List

"""
A skip list is a data structure consisting of a collection of nodes, each of which contains a key and a pointer to the next node in the list.

The nodes are ordered by their keys, and the next node in the list is always located at a level below the current node.

The skip list is a data structure that is used to implement a dictionary.

The skip list is a data structure that is used to implement a set.
"""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = []


class SkipList:
    def __init__(self):
        self.head = Node(0, 0)
        self.max_level = 0

    def search(self, key):
        curr = self.head
        for i in range(self.max_level, -1, -1):
            while curr.next[i] and curr.next[i].key < key:
                curr = curr.next[i]
        return curr.next[0]

    def insert(self, key, val):
        update = [None] * (self.max_level + 1)
        curr = self.head
        for i in range(self.max_level, -1, -1):
            while curr.next[i] and curr.next[i].key < key:
                curr = curr.next[i]
            update[i] = curr
        if not curr.next[0] or curr.next[0].key != key:
            self.max_level = max(self.max_level, random.randint(0, 2))
            node = Node(key, val)
            for i in range(self.max_level + 1):
                node.next.append(update[i].next[i])
                update[i].next[i] = node
        else:
            curr.next[0].val = val

    def delete(self, key):
        update = [None] * (self.max_level + 1)
        curr = self.head
        for i in range(self.max_level, -1, -1):
            while curr.next[i] and curr.next[i].key < key:
                curr = curr.next[i]
            update[i] = curr
        if curr.next[0] and curr.next[0].key == key:
            for i in range(self.max_level + 1):
                if update[i].next[i] and update[i].next[i].key == key:
                    update[i].next[i] = update[i].next[i].next[i]

    def print_list(self):
        curr = self.head
        while curr.next[0]:
            print(curr.next[0].key, end=" ")
            curr = curr.next[0]
        print()


# if __name__ == '__main__':
#     sl = SkipList()
#     sl.insert(1, 1)
#     sl.insert(2, 2)


# --

#  Graphs


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_graph(self):
        for i in range(self.V):
            print(self.graph[i])

    def add_edge(self, src, dest):
        self.graph[src][dest] = 1
        self.graph[dest][src] = 1

    def is_cyclic(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V
        for i in range(self.V):
            if visited[i] is False:
                if self.is_cyclic_util(i, visited, rec_stack) is True:
                    return True
                    break
        return False

    def is_cyclic_util(self, i, visited, rec_stack):
        visited[i] = True
        rec_stack[i] = True
        for j in range(self.V):
            if self.graph[i][j] == 1 and visited[j] is False:
                if self.is_cyclic_util(j, visited, rec_stack) is True:
                    return True
            elif self.graph[i][j] == 1 and rec_stack[j] is True:
                return True
        rec_stack[i] = False
        return False


# driver code
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    if g.is_cyclic() is 1:
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")

# --

#  DFS


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_graph(self):
        for i in range(self.V):
            print(self.graph[i])

    def add_edge(self, src, dest):
        self.graph[src][dest] = 1
        self.graph[dest][src] = 1

    def dfs(self, s):
        visited = [False] * self.V
        self.dfs_util(s, visited)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        for i in range(self.V):
            if self.graph[v][i] == 1 and visited[i] is False:
                self.dfs_util(i, visited)


# driver code
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.dfs(2)

# --


# Divide and Conquer with Examples Such as Sorting


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)

mergeSort(arr, 0, n - 1)

print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])

# --


# Merge Sort with Examples


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)


# --


# Matrix Multiplication


def matrix_multiply(A, B):
    C = [[0 for i in range(len(A))] for j in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C


# driver code to test above
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

if __name__ == "__main__":
    print("Matrix A is:")
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end=" ")
        print()

    print("Matrix B is:")
    for i in range(len(B)):
        for j in range(len(B[0])):
            print(B[i][j], end=" ")
        print()

    C = matrix_multiply(A, B)

    print("Matrix C is: ", end="\n")
    for i in range(len(C)):
        for j in range(len(C[0])):
            print(C[i][j], end=" ")
        print()


# --


# Matrix Multiplication using Strassen's Algorithm


def strassen_matrix_multiply(A, B):
    """
    A: a square matrix
    B: another square matrix with the same size as A
    return value: the product of A and B
    """

    print("Matrix A is:")
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end=" ")
        print()

    print("Matrix B is:")
    for i in range(len(B)):
        for j in range(len(B[0])):
            print(B[i][j], end=" ")
        print()

    # main computation
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        # split the matrix into 4 sub-matrices
        # A11, A12, A21, A22
        # B11, B12, B21, B22
        A11 = [[0 for i in range(n // 2)] for j in range(n // 2)]
        A12 = [[0 for i in range(n // 2)] for j in range(n // 2)]
        A21 = [[0 for i in range(n // 2)] for j in range(n // 2)]
        A22 = [[0 for i in range(n // 2)] for j in range(n // 2)]
        B11 = [[0 for i in range(n // 2)] for j in range(n // 2)]
        B12 = [[0 for i in range(n // 2)] for j in range(n // 2)]
        B21 = [[0 for i in range(n // 2)] for j in range(n // 2)]
        B22 = [[0 for i in range(n // 2)] for j in range(n // 2)]

        for i in range(n // 2):
            for j in range(n // 2):
                A11[i][j] = A[i][j]
                A12[i][j] = A[i][j + n // 2]
                A21[i][j] = A[i + n // 2][j]
                A22[i][j] = A[i + n // 2][j + n // 2]

                B11[i][j] = B[i][j]
                B12[i][j] = B[i][j + n // 2]
                B21[i][j] = B[i + n // 2][j]
                B22[i][j] = B[i + n // 2][j + n // 2]

        # compute P1 to P7
        P1 = strassen_matrix_multiply(A11, matrix_add(B12, B22, -1))
        P2 = strassen_matrix_multiply(A21, matrix_add(B11, B21, -1))
        P3 = strassen_matrix_multiply(A22, matrix_add(B21, B11, 1))
        P4 = strassen_matrix_multiply(A11, matrix_add(B22, B12, 1))
        P5 = strassen_matrix_multiply(A12, matrix_add(B11, B12, -1))
        P6 = strassen_matrix_multiply(A21, matrix_add(B12, B22, 1))
        P7 = strassen_matrix_multiply(A22, matrix_add(B21, B11, -1))
        # compute C11, C12, C21, C22
        C11 = matrix_add(matrix_add(matrix_add(P1, P4, -1), P5, 1), P7, 1)
        C12 = matrix_add(P3, P5, 1)
        C21 = matrix_add(P2, P4, 1)
        C22 = matrix_add(matrix_add(matrix_add(P1, P2, -1), P3, 1), P6, 1)

        # construct C
        C = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                C[i][j] = C11[i][j]
                C[i][j + n // 2] = C12[i][j]
                C[i + n // 2][j] = C21[i][j]
                C[i + n // 2][j + n // 2] = C22[i][j]

        return C


def strassen_matrix_multiply(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def matrix_add(A, B, sign):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + sign * B[i][j]
    return C


def main():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(strassen_matrix_multiply(A, B))


if __name__ == "__main__":
    main()


# --


# Convex Hull and Searching.
"""
Given a set of points in the xy-plane, determine the minimum area rectangle that encl
oses all of the points.

For example, given the set of points [(1,1),(1,3),(3,1),(3,3),(2,2)], return the
smallest rectangle that encloses all five points.

Note:

There are at least 1 and at most 1000000 points.
All points have integer coordinates in the xy-plane.
The answer is guaranteed to be unique.
"""


def find_min_rect(points):

    # sort the points by x-axis
    points.sort(key=lambda x: x[0])
    print(points)

    # find the left-most point
    left = points[0][0]
    right = points[-1][0]
    min_area = float("inf")

    for i in range(len(points)):
        # find the right-most point
        if points[i][0] > right:
            right = points[i][0]

        # find the bottom-most point
        if points[i][1] < points[i - 1][1] or i == 0:
            bottom = points[i][1]

        # find the top-most point
        if points[i][1] > points[i - 1][1] or i == 0:
            top = points[i][1]

        # find the area of the current rectangle
        area = (right - left) * (top - bottom)

        # update the minimum area
        min_area = min(min_area, area)

    return min_area


def main():
    points = [(1, 1), (1, 3), (3, 1), (3, 3), (2, 2)]
    print(find_min_rect(points))


if __name__ == "__main__":
    main()


# --


# Binary Search Tree Iterator.
"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.push_left(root)

    def push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        self.push_left(node.right)
        return node.val

    def hasNext(self):
        return len(self.stack) > 0


# --


# Binary Tree Level Order Traversal II.
"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result[::-1]


# --


# Binary Tree Maximum Path Sum.
"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # The max path sum so far
        self.max_sum = float("-inf")

        # Recursively compute the max gain, which is the max sum of a path
        # starting at this node and going left or right
        def max_gain(node: TreeNode) -> int:
            # Base case: If this is a null node, return 0
            if not node:
                return 0

            # Recursively compute the max gain going left and right
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # The price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain

            # Update max_sum if it's better to start a new path
            self.max_sum = max(self.max_sum, price_newpath)

            # For recursion:
            # Return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum


# Greedy Methods with Examples Such as Optimal Reliability Allocation
"""
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

For example, given 20 items with integer weights 1 through 5 and integer values 1 through 5, determine a collection of 15 items with the maximum value.


"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def intervalIntersection(
        self, A: "List[Interval]", B: "List[Interval]"
    ) -> "List[Interval]":
        # Sort the intervals by start time
        A.sort(key=lambda x: x.start)
        B.sort(key=lambda x: x.start)

        # Initialize result
        result = []

        # Two pointers
        i = j = 0

        # Traverse both lists
        while i < len(A) and j < len(B):
            # Check if there is an intersection
            if A[i].end >= B[j].start:
                # Append intersection interval
                result.append(
                    Interval(max(A[i].start, B[j].start), min(A[i].end, B[j].end))
                )

                # Move the pointer who's end time is earlier
                if A[i].end < B[j].end:
                    i += 1
                else:
                    j += 1
            else:
                # Move the pointer who's start time is earlier
                if A[i].start < B[j].start:
                    i += 1
                else:
                    j += 1

        return result


# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize result
        result = 0

        # Initialize left and right pointers
        left = right = 0

        # Use a dictionary to keep track of characters
        char_dict = {}

        # Traverse the string
        while right < len(s):
            # If the character is already in the dictionary, update left pointer
            if s[right] in char_dict and char_dict[s[right]] >= left:
                left = char_dict[s[right]] + 1
            # Add the current character to the dictionary
            char_dict[s[right]] = right
            # Update the result if current substring is longer
            result = max(result, right - left + 1)
            # Move the right pointer
            right += 1

        return result


# Knapsack
"""
Given a list of items with values and weights, as well as a max weight, find the maximum value you can generate from items where the sum of the weights is less than or equal to the max weight.

For example, given the following list of items:

[
  (60, 20), (100, 50), (120, 30)
]
and max weight 150, you should return 180.

The items you pick should be the maximum value ones, so you shouldn't pick the 100 to 50 pair.

Note: You can't break an item, so the sum of the weights of the items you pick should not exceed the max weight.
"""


class Solution:
    def knapsack(self, items, max_weight):
        # Initialize the table
        table = [[0 for _ in range(max_weight + 1)] for _ in range(len(items) + 1)]

        # Fill the table
        for i in range(1, len(items) + 1):
            for j in range(1, max_weight + 1):
                # If the current item weight is less than or equal to the current max weight
                if items[i - 1][1] <= j:
                    # Add the current item value to the current max weight
                    table[i][j] = max(
                        table[i - 1][j],
                        table[i - 1][j - items[i - 1][1]] + items[i - 1][0],
                    )
                else:
                    # If the current item weight is greater than the current max weight, use the previous max weight
                    table[i][j] = table[i - 1][j]

        return table[-1][-1]


# Longest Increasing Subsequence
"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example, given [10, 9, 2, 5, 3, 7, 101, 18], the longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution:
    def lengthOfLISt(self, nums):
        # Initialize the table
        table = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        # Fill the table
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                # If the current item is less than or equal to the previous item
                if nums[i] <= nums[j]:
                    # Add 1 to the current item
                    table[i][j] = table[i][j - 1] + 1
                else:
                    # If the current item is greater than the   previous item, use the previous item
                    table[i][j] = table[i][j - 1]

        return max(max(row) for row in table)


# Longest Common Subsequence
"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Note: All characters in the given inputs are lowercase letters.

"""


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        # Initialize the table
        table = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        # Fill the table
        for i in range(len(text1) + 1):
            for j in range(len(text2) + 1):
                # If the current item is equal to the previous item
                if i == 0 or j == 0:
                    # Use 0
                    table[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    # If the current item is equal to the previous item, add 1 to the current item
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    # If the current item is not equal to the previous item, use the previous item
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])

        return table[-1][-1]


# Minimum Spanning Trees – Prim's Algorithms
"""
Given an undirected graph with n vertices and m edges, find the minimum spanning tree (MST) using Prim's algorithm.

The graph is given in the following form: graph[i] is a list of all vertices adjacent to the vertex indexed by i.

"""


class Solution:
    def prim(self, graph):
        # Initialize the table
        table = [[float("inf") for _ in range(len(graph))] for _ in range(len(graph))]

        # Fill the table
        for i in range(len(graph)):
            table[i][i] = 0

        for i in range(len(graph)):
            for j in range(len(graph)):
                if i != j:
                    table[i][j] = graph[i][j]

        # Initialize the visited array
        visited = [False for _ in range(len(graph))]

        # Initialize the parent array
        parent = [-1 for _ in range(len(graph))]

        # Initialize the key array
        key = [float("inf") for _ in range(len(graph))]

        # Initialize the min_index
        min_index = 0

        # Initialize the min_key
        min_key = float("inf")

        # Initialize the MST
        MST = []

        # Initialize the MST_weight
        MST_weight = 0

        # Iterate through the table
        for i in range(len(table)):
            # Find the minimum key
            for j in range(len(table)):
                if table[i][j] < min_key and visited[j] is False:
                    min_key = table[i][j]
                    min_index = j

            # Add the minimum key to the MST
            MST.append(min_index)

            # Update the visited array
            visited[min_index] = True

            # Update the parent array
            parent[min_index] = i

            # Update the key array
            key[min_index] = min_key

            # Update the MST_weight
            MST_weight += min_key

            # Reset the min_key
            min_key = float("inf")

        return MST, MST_weight


# Minimum Spanning Trees – Kruskal's  Algorithms
"""
Given an undirected graph with n vertices and m edges, find the minimum spanning tree (MST) using Kruskal's algorithm.

The graph is given in the following form: graph[i] is a list of all vertices adjacent to the vertex indexed by i.

"""


class Solution:
    def kruskal(self, graph):
        # Initialize the table
        table = [[float("inf") for _ in range(len(graph))] for _ in range(len(graph))]

        # Fill the table
        for i in range(len(graph)):
            table[i][i] = 0

        for i in range(len(graph)):
            for j in range(len(graph)):
                if i != j:
                    table[i][j] = graph[i][j]

        # Initialize the parent array
        parent = [-1 for _ in range(len(graph))]

        # Initialize the key array
        key = [float("inf") for _ in range(len(graph))]

        # Initialize the min_index
        min_index = 0

        # Initialize the min_key
        min_key = float("inf")

        # Initialize the MST
        MST = []

        # Initialize the MST_weight
        MST_weight = 0

        # Iterate through the table
        while True:
            # Find the minimum key
            for i in range(len(table)):
                for j in range(len(table)):
                    if table[i][j] < min_key and parent[i] != j:
                        min_key = table[i][j]
                        min_index = j

            # Add the minimum key to the MST
            MST.append(min_index)

            # Update the visited array
            parent[min_index] = i

            # Update the key array
            key[min_index] = min_key

            # Update the MST_weight
            MST_weight += min_key

            # Reset the min_key
            min_key = float("inf")

            # Check if the MST is complete
            if len(MST) == len(graph):
                break

            # Update the table
            for i in range(len(table)):
                for j in range(len(table)):
                    if i != j and i != min_index and j != min_index:
                        table[i][j] = min(
                            table[i][j], table[i][min_index] + table[min_index][j]
                        )

        return MST_weight


# Single Source Shortest Paths - Dijkstra's Algorithm
"""
Given a weighted graph, find the shortest path from a source vertex to all other vertices.

The graph is represented using an adjacency list.

The adjacency list is a dictionary of key value pairs, where the key is a vertex and the value is a list of tuples.

Each tuple contains the vertex it is connected to and the weight of the edge.

Example:

graph = {
    'A': [('B', 2)],
    'B': [('A', 2), ('C', 5)],
    'C': [('B', 5)]
}

The above graph has 3 vertices and 3 edges.

The adjacency list representation of the graph is as follows:

graph = {
    'A': [('B', 2)],
    'B': [('A', 2), ('C', 5)],
    'C': [('B', 5)]
}

The shortest path from 'A' to 'C' is:

['A', 'B', 'C']

The shortest path from 'B' to 'C' is:

['B', 'C']

The shortest path from 'A' to 'B' is:

['A', 'B']

The shortest path from 'B' to 'A' is:

['B', 'A']

The shortest path from 'A' to 'A' is:

['A']

The shortest path from 'C' to 'C' is:

['C']

The shortest path from 'C' to 'A' is:

['C', 'B', 'A']

The shortest path from 'C' to 'B' is:

['C', 'B']

"""


def dijkstra(graph, source):
    """
    :param graph: The graph, represented as an adjacency list
    :param source: The source vertex
    :return: A dictionary containing the shortest path from the source vertex to all other vertices
    """
    # Initialize the distance array
    distance = {vertex: float("inf") for vertex in graph}

    # Initialize the predecessor array
    predecessor = {vertex: None for vertex in graph}

    # Initialize the priority queue
    priority_queue = []

    # Initialize the source vertex distance to 0
    distance[source] = 0

    # define heapq
    heapq = []

    # Add the source vertex to the priority queue
    heapq.append((0, source))

    # While the priority queue is not empty
    while heapq:
        # Pop the vertex with the smallest distance from the priority queue
        current_vertex = heapq.pop(0)[1]

        # For each vertex adjacent to the current vertex
        for adjacent_vertex, weight in graph[current_vertex]:
            # If the distance to the adjacent vertex is greater than the distance to the current vertex plus the weight of the edge
            if distance[adjacent_vertex] > distance[current_vertex] + weight:
                # Update the distance to the adjacent vertex
                distance[adjacent_vertex] = distance[current_vertex] + weight
                # Update the predecessor of the adjacent vertex
                predecessor[adjacent_vertex] = current_vertex
                # Add the adjacent vertex to the priority queue
                heapq.append((distance[adjacent_vertex], adjacent_vertex))

    return distance, predecessor


def shortest_path(graph, source, destination):
    """
    :param graph: The graph, represented as an adjacency list
    :param source: The source vertex
    :param destination: The destination vertex
    :return: A list containing the shortest path from the source vertex to the destination vertex
    """
    # Get the shortest path from the source vertex to all other vertices
    distance, predecessor = dijkstra(graph, source)

    # Initialize the path list
    path = []

    # While the destination vertex has a predecessor
    while destination in predecessor:
        # Append the destination vertex to the path list
        path.append(destination)
        # Update the destination vertex
        destination = predecessor[destination]

    # Append the source vertex to the path list
    path.append(source)

    # Reverse the path list
    path = path[::-1]

    return path


def main():
    # Create the graph
    graph = {
        "A": [("B", 2), ("C", 5)],
        "B": [("A", 2), ("C", 3), ("D", 1)],
        "C": [("A", 5), ("B", 3), ("D", 4), ("E", 2)],
        "D": [("B", 1), ("C", 4), ("E", 1)],
        "E": [("C", 2), ("D", 1)],
    }

    # Get the shortest path from vertex 'A' to vertex 'E'
    path = shortest_path(graph, "A", "E")

    # Print the shortest path
    print(path)


if __name__ == "__main__":
    main()
# Bellman Ford Algorithms.
"""
Given a weighted graph, find the shortest path from a source vertex to all other vertices.

The Bellman-Ford algorithm is an algorithm for finding the shortest path from a source vertex
to all other vertices in a weighted graph.

The Bellman-Ford algorithm is also known as the Negative-Weight Cycle algorithm.

The Bellman-Ford algorithm is also known as the Bellman-Ford-Moore algorithm
(or the Bellman-Ford-Welsh algorithm).

The Bellman-Ford algorithm is not guaranteed to work for all graphs and can be used to detect negative cycles.



"""

# Bellman-Ford Algorithm implementation in Python

from collections import deque

def bellman_ford(graph, source):
    distance, predecessor = {vertex: float("inf") for vertex in graph}, {}
    distance[source] = 0
    predecessor[source] = None

    # Step 1: relax edges repeatedly
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbour in graph[vertex]:
                if distance[neighbour] > distance[vertex] + graph[vertex][neighbour]:
                    distance[neighbour] = distance[vertex] + graph[vertex][neighbour]
                    predecessor[neighbour] = vertex

    # Step 2: check for negative-weight cycles
    for vertex in graph:
        for neighbour in graph[vertex]:
            assert distance[neighbour] <= distance[vertex] + graph[vertex][neighbour]

    return distance, predecessor

if __name__ == "__main__":
    graph = {
        "A": {"B": -1, "C": 4},
        "B": {"C": 3, "D": 2, "E": 2},
        "C": {},
        "D": {"B": 1, "C": 5},
        "E": {"D": -3},
    }

    # Get the shortest path from vertex 'A' to vertex 'E'
    distance, predecessor = bellman_ford(graph, "A")
    print(distance)
    print(predecessor)


# Dynamic Programming with Examples Such as Knapsack.
"""
Given a set of items with weights and values, and a knapsack capacity, find the maximum value you can put in the knapsack.


You can only fit items in the knapsack one at a time.

Example:

Input:

items = [
  (1, 6),
  (2, 10),
  (3, 12),
]
capacity = 5

Output:


Output:

Return the maximum value you can put in the knapsack.

"""

# implementation of 0-1 Knapsack Problem
def knapsack(items, capacity):
    # Create a matrix to hold the values
    matrix = [[0 for x in range(capacity + 1)] for x in range(len(items) + 1)]
    # Fill the first row and column with 0
    for i in range(len(items) + 1):
        matrix[i][0] = 0
    for i in range(capacity + 1):
        matrix[0][i] = 0

    # Fill the rest of the matrix
    for i in range(1, len(items) + 1):
        for j in range(1, capacity + 1):
            # If the weight of the item is less than or equal to the capacity
            if items[i - 1][0] <= j:
                # If the value of the item plus the value of the item in the previous row is greater than the value in the previous row
                if (
                    items[i - 1][1] + matrix[i - 1][j - items[i - 1][0]]
                    > matrix[i - 1][j]
                ):
                    # Set the value to the value of the item plus the value of the item in the previous row
                    matrix[i][j] = items[i - 1][1] + matrix[i - 1][j - items[i - 1][0]]
                else:
                    # Otherwise, set the value to the value in the previous row
                    matrix[i][j] = matrix[i - 1][j]
    return matrix[len(items)][capacity]


# Implementation of 0-1 Knapsack Problem with Dynamic Programming
def knapsack_dp(items, capacity):
    # Create a matrix to hold the values
    matrix = [[0 for x in range(capacity + 1)] for x in range(len(items) + 1)]
    # Fill the first row and column with 0
    for i in range(len(items) + 1):
        matrix[i][0] = 0
    for i in range(capacity + 1):
        matrix[0][i] = 0

    # Fill the rest of the matrix
    for i in range(1, len(items) + 1):
        for j in range(1, capacity + 1):
            # If the weight of the item is less than or equal to the capacity
            if items[i - 1][0] <= j:
                # If the value of the item plus the value of the item in the previous row is greater than the value in the previous row
                if (
                    items[i - 1][1] + matrix[i - 1][j - items[i - 1][0]]
                    > matrix[i - 1][j]
                ):
                    # Set the value to the value of the item plus the value of the item in the previous row
                    matrix[i][j] = items[i - 1][1] + matrix[i - 1][j - items[i - 1][0]]
                else:
                    # Otherwise, set the value to the value in the previous row
                    matrix[i][j] = matrix[i - 1][j]
    return matrix[len(items)][capacity]


# Implementation of 0-1 Knapsack Problem with Greedy Algorithm
def knapsack_greedy(items, capacity):
    # Create a list to hold the items
    items_list = []
    # Create a variable to hold the total value
    total_value = 0
    # Create a variable to hold the total weight
    total_weight = 0
    # Create a variable to hold the current weight
    current_weight = 0
    # Create a variable to hold the current value
    current_value = 0
    # Create a variable to hold the current item
    current_item = 0
    # Create a variable to hold the current index
    current_index = 0
    # Create a variable to hold the current capacity
    current_capacity = capacity
    # Create a variable to hold the current item
    current_item = items[current_index]
    # While the current weight is less than or equal to the capacity
    while current_weight <= current_capacity:
        # If the current item is less than or equal to the current capacity
        if current_item[0] <= current_capacity:
            # Add the current item to the items list
            items_list.append(current_item)
            # Add the current item's weight to the total weight
            total_weight += current_item[0]
            # Add the current item's value to the total value
            total_value += current_item[1]
            # Subtract the current item's weight from the current capacity
            current_capacity -= current_item[0]
            # Increment the current index
            current_index += 1
            # If the current index is less than the length of the items
            if current_index < len(items):
                # Set the current item to the item at the current index
                current_item = items[current_index]
            # Otherwise, set the current item to None
            else:
                current_item = None
        # Otherwise, if the current item is not None
        elif current_item is not None:
            # Increment the current index
            current_index += 1
            # If the current index is less than the length of the items
            if current_index < len(items):
                # Set the  current item to the item at the current index
                current_item = items[current_index]
            # Otherwise, set the current item to None
            else:
                current_item = None
        # Otherwise, if the current item is None
        else:
            # Increment the current index
            current_index += 1
            # If the current index is less than the length of the items
            if current_index < len(items):
                # Set the current item to the item at the current index
                current_item = items[current_index]
            # Otherwise, set the current item to None
            else:
                current_item = None
    # Return the items list and the total weight and value
    return items_list, total_weight, total_value

def knapsack_big(items_list, knapsack_big_capacity):
    """Given a list of items with weights and values,
    and a knapsack capacity, return a list of items with
    weights and values that maximize the value of the
    knapsack without going over the knapsack capacity.
    """
    items_list_len = len(items_list)

    # Create an array of zeros with the number of
    # rows equal to the number of items in the items_list
    # and the number of columns equal to the knapsack capacity
    dp_table = [[0] * (knapsack_big_capacity + 1) for _ in range(items_list_len + 1)]

    # Loop over the items in the items_list
    for i in range(1, items_list_len + 1):
        # Loop over the weights from 0 to the knapsack capacity
        for weight in range(1, knapsack_big_capacity + 1):
            # Get the value and weight of the current item
            item_value = items_list[i - 1][0]
            item_weight = items_list[i - 1][1]

            # If the weight of the current item is less than or equal to
            # the current weight, then we can include the current item
            # in the knapsack
            if item_weight <= weight:
                dp_table[i][weight] = max(
                    # Get the value of the item by adding the value of the
                    # current item plus the value of the item that we can
                    # include if we subtract the weight of the current item
                    # from the current weight
                    item_value + dp_table[i - 1][weight - item_weight],
                    # Get the value of the item that we can include if we
                    # don't include the current item
                    dp_table[i - 1][weight],
                )
            # If the weight of the current item is greater than the current weight,
            # then we can't include the current item, and we should just use
            # the value of the item that we can include if we don't include
            # the current item
            else:
                dp_table[i][weight] = dp_table[i - 1][weight]

    # Create a list to store the items that we will include in the knapsack
    knapsack_big_items_list = []

    # Get the maximum value that can be included in the knapsack
    knapsack_big_total_value = dp_table[-1][-1]

    # Get the weight that corresponds to the maximum value
    knapsack_big_total_weight = knapsack_big_capacity

    # Loop while the knapsack_big_total_value is greater than 0 and
    # knapsack_big_total_weight is greater than 0
    while knapsack_big_total_value > 0 and knapsack_big_total_weight > 0:
        # If the value of the item that we can include if we don't include
        # the current item is the same as the knapsack_big_total_value,
        # then we didn't include the current item, so we should move
        # on to the next item
        if dp_table[items_list_len][knapsack_big_total_weight] == dp_table[items_list_len - 1][knapsack_big_total_weight]:
            items_list_len -= 1
        # If the value of the item that we can include if we don't include
        # the current item is not the same as the knapsack_big_total_value,
        # then we included the current item, so we should add the current item
        # to the knapsack_big_items_list, subtract the weight of the current item
        # from the knapsack_big_total_weight, and subtract the value of the current
        # item from the knapsack_big_total_value
        else:
            knapsack_big_items_list.append(items_list[items_list_len - 1])
            knapsack_big_total_weight -= items_list[items_list_len - 1][1]
            knapsack_big_total_value -= items_list[items_list_len - 1][0]
            items_list_len -= 1

    # Return the list of items in the knapsack, the total weight, and the
    # total value
    return knapsack_big_items_list, knapsack_big_total_weight, knapsack_big_total_value


# Define the knapsack_big function
# This function will fill a knapsack with the most valuable items possible

#  All Pair Shortest Paths – Warshal's Algorithm
"""
The Warshal's Algorithm is an algorithm for finding the shortest paths between all pairs of vertices in a graph.

The algorithm is based on the idea that the shortest path between any two vertices is the shortest path between any vertex in the first set and any vertex in the second set.
"""

# Implementation of Warshal's Algorithm


def warshal(graph):
    # Initialize the distance matrix
    distance_matrix = [[0 for col in range(len(graph))] for row in range(len(graph))]
    # Fill the distance matrix with the values from the graph
    for i in range(len(graph)):
        for j in range(len(graph)):
            distance_matrix[i][j] = graph[i][j]
    # For each vertex
    for k in range(len(graph)):
        # For each vertex
        for i in range(len(graph)):
            # For each vertex
            for j in range(len(graph)):
                # If the distance from the vertex to the vertex plus the distance from the vertex to the vertex is less than the distance from the vertex to the vertex
                if (
                    distance_matrix[i][k] + distance_matrix[k][j]
                    < distance_matrix[i][j]
                ):
                    # Set the distance from the vertex to the vertex to the distance from the vertex to the vertex plus the distance from the vertex to the vertex
                    distance_matrix[i][j] = (
                        distance_matrix[i][k] + distance_matrix[k][j]
                    )
    # Return the distance matrix
    return distance_matrix


# Test the warshal function
graph = [
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

# Print the distance matrix
print("The distance matrix is:")
for row in warshal(graph):
    print(row)

# Floyd's Algorithms
"""
Floyd's algorithm is an algorithm for finding the shortest paths between all pairs of vertices in a graph.
"""


def floyd(graph):
    # Initialize the distance matrix
    distance_matrix = [[0 for col in range(len(graph))] for row in range(len(graph))]
    # Fill the distance matrix with the values from the graph
    for i in range(len(graph)):
        for j in range(len(graph)):
            distance_matrix[i][j] = graph[i][j]
    # For each vertex
    for k in range(len(graph)):
        # For each vertex
        for i in range(len(graph)):
            # For each vertex
            for j in range(len(graph)):
                # If the distance from the vertex to the vertex plus the distance from the vertex to the vertex is less than the distance from the vertex to the vertex
                if (
                    distance_matrix[i][k] + distance_matrix[k][j]
                    < distance_matrix[i][j]
                ):
                    # Set the distance from the vertex to the vertex to the distance from the vertex to the vertex plus the distance from the vertex to the vertex
                    distance_matrix[i][j] = (
                        distance_matrix[i][k] + distance_matrix[k][j]
                    )
                    # If the distance from the vertex to the vertex is less than the distance from the vertex to
                    if distance_matrix[i][j] < distance_matrix[i][k]:
                        # Set the distance from the vertex to the vertex to the distance from the vertex to the vertex
                        distance_matrix[i][j] = distance_matrix[i][k]
    # Return the distance matrix
    return distance_matrix
    # Return the distance matrix


# Test the floyd function
graph = [
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

# Print the distance matrix
print("The distance matrix is:")
for row in floyd(graph):
    print(row)

# Prim's Algorithm
"""
Prim's algorithm is an algorithm for finding the minimum spanning tree of a graph.
"""


def prim(graph):
    # Initialize the spanning tree
    spanning_tree = []
    # Initialize the spanning tree
    spanning_tree_edges = []
    # Initialize the spanning tree
    spanning_tree_weights = []
    # Initialize the visited vertices
    visited_vertices = [0]
    # While the length of the visited vertices is less than the length of the graph
    while len(visited_vertices) < len(graph):
        # Initialize the minimum weight to infinity
        minimum_weight = float("inf")
        # For each vertex in the visited vertices
        for vertex in visited_vertices:
            # For each vertex in the graph
            for i in range(len(graph)):
                # If the vertex is not in the visited vertices and the weight is less than the minimum weight
                if i not in visited_vertices and graph[vertex][i] < minimum_weight:
                    # Set the minimum weight to the weight
                    minimum_weight = graph[vertex][i]
                    # Set the minimum weight vertex to the vertex
                    minimum_weight_vertex = i
                    # Set the minimum weight vertex to the vertex
                    minimum_weight_vertex_from = vertex
        # Append the minimum weight vertex to the visited vertices
        visited_vertices.append(minimum_weight_vertex)
        # Append the minimum weight vertex from and the minimum weight vertex to the spanning tree
        spanning_tree.append([minimum_weight_vertex_from, minimum_weight_vertex])
        # Append the weight to the spanning tree weights
        spanning_tree_weights.append(minimum_weight)
    # Return the spanning tree and the spanning tree weights
    return spanning_tree, spanning_tree_weights


# Print the spanning tree and the spanning tree weights
print("The spanning tree is:")
print(prim(graph))


# Kruskal's Algorithm
"""
Kruskal's algorithm is an algorithm for finding the minimum spanning tree of a graph.
"""


def kruskal(graph):
    # Initialize the spanning tree
    spanning_tree = []
    # Initialize the spanning tree weights
    spanning_tree_weights = []
    # Initialize the visited vertices
    visited_vertices = []
    # Initialize the edges
    edges = []
    # For each vertex in the graph
    for vertex in graph:
        # For each vertex in the graph
        for i in range(len(graph)):
            # If the vertex is not in the visited vertices
            if i not in visited_vertices:
                # Append the vertex to the edges
                edges.append([vertex, i])
    # Sort the edges by weight
    edges.sort(key=lambda x: x[1])
    # For each edge in the edges
    for edge in edges:
        # If the edge is not in the spanning tree
        if edge not in spanning_tree:
            # Append the edge to the spanning tree
            spanning_tree.append(edge)
            # Append the weight of the edge to the spanning tree weights
            spanning_tree_weights.append(edge[1])
            # Append the vertex of the edge to the visited vertices
            visited_vertices.append(edge[0])
            # Append the vertex of the edge to the visited vertices
            visited_vertices.append(edge[1])
    # Return the spanning tree and the spanning tree weights
    return spanning_tree, spanning_tree_weights


# Print the spanning tree and the spanning tree weights
print("The spanning tree is:")
print(kruskal(graph))


# Resource Allocation Problem.
"""
The resource allocation problem is a problem in which a set of resources are allocated to a set of tasks.
"""


def resource_allocation(tasks, resources):
    # Initialize the task allocation
    task_allocation = []
    # Initialize the resource allocation
    resource_allocation = []
    # Initialize the visited vertices
    visited_vertices = []
    # Initialize the edges
    edges = []
    # For each task in the tasks
    for task in tasks:
        # For each resource in the resources
        for i in range(len(resources)):
            # If the resource is not in the visited vertices
            if i not in visited_vertices:
                # Append the resource to the edges
                edges.append([task, i])
    # Sort the edges by weight
    edges.sort(key=lambda x: x[1])
    # For each edge in the edges
    for edge in edges:
        # If the edge is not in the spanning tree
        if edge not in task_allocation:
            # Append the edge to the spanning tree
            task_allocation.append(edge)
            # Append the weight of the edge to the spanning tree weights
            resource_allocation.append(edge[1])
            # Append the vertex of the edge to the visited vertices
            visited_vertices.append(edge[0])
            # Append the vertex of the edge to the visited vertices
            visited_vertices.append(edge[1])
    # Return the spanning tree and the spanning tree weights
    return task_allocation, resource_allocation


# Print the spanning tree and the spanning tree weights
tasks = [0, 1, 2, 3, 4, 5, 6]
resources = [0, 1, 2, 3, 4, 5, 6]
print("The task allocation is:")
print(resource_allocation(tasks, resources))


# Backtracking
"""
Backtracking is a search algorithm that solves problems by trying all possible combinations of values.
"""


def backtracking(domain, assignment, csp):
    # If the assignment is complete
    if len(assignment) == len(domain):
        # Return the assignment
        return assignment
    # Initialize the variable
    var = select_unassigned_variable(assignment, csp)
    # For each value in the domain
    for value in domain[var]:
        # If the value is consistent with the assignment
        if consistent(var, value, assignment, csp):
            # Add the value to the assignment
            assignment[var] = value
            # If the assignment is consistent
            if consistent(var, value, assignment, csp):
                # Call the backtracking
                result = backtracking(domain, assignment, csp)
                # If the result is
                if result is not None:
                    # Return the result
                    return result
            # Remove the value from the assignment
            del assignment[var]
    # Return None
    return None


def select_unassigned_variable(assignment, csp):
    # For each variable in the CSP
    for var in csp.keys():
        # If the variable is not in the assignment
        if var not in assignment:
            # Return the variable
            return var


def consistent(var, value, assignment, csp):
    # For each constraint in the CSP
    for constraint in csp[var]:
        # If the constraint is not satisfied
        if not constraint(var, value, assignment, csp):
            # Return False
            return False
    # Return True
    return True


def binary_constraint(var1, var2, assignment, csp):
    # If the variables are assigned
    if var1 in assignment and var2 in assignment:
        # If the values are equal
        if assignment[var1] == assignment[var2]:
            # Return True
            return True
    # Return False
    return False


# Print the backtracking
domain = {"A": [1, 2, 3], "B": [1, 2, 3], "C": [1, 2, 3]}
assignment = {}
csp = {
    "A": [binary_constraint, binary_constraint],
    "B": [binary_constraint, binary_constraint],
    "C": [binary_constraint, binary_constraint],
}
result = backtracking(domain, assignment, csp)
print(result)

# Branch and Bound with Examples Such as Travelling Salesman Problem


def branch_and_bound(graph, start_vertex):
    # Initialize the visited vertices
    visited_vertices = []
    # Initialize the unvisited vertices
    unvisited_vertices = []
    # For each vertex in the graph
    for vertex in graph:
        # If the vertex is not in the visited vertices
        if vertex not in visited_vertices:
            # Append the vertex to the unvisited vertices
            unvisited_vertices.append(vertex)
    # Initialize the minimum weight
    minimum_weight = float("inf")
    # Initialize the minimum weight vertex
    minimum_weight_vertex = None
    # Initialize the minimum weight vertex from
    minimum_weight_vertex_from = None
    # For each vertex in the unvisited vertices
    for vertex in unvisited_vertices:
        # For each vertex in the graph
        for i in range(len(graph)):
            # If the vertex is not in the visited vertices
            if i not in visited_vertices:
                # If the vertex is not in the unvisited vertices
                if i not in unvisited_vertices:
                    # Append the vertex to the unvisited vertices
                    unvisited_vertices.append(i)
        # Initialize the weight
        weight = 0
        # For each vertex in the unvisited vertices
        for vertex in unvisited_vertices:
            # If the vertex is not in the visited vertices
            if vertex not in visited_vertices:
                # Add the weight of the edge
                weight += graph[start_vertex][vertex]
        # If the weight is less than the minimum weight
        if weight < minimum_weight:
            # Set the minimum weight to the weight
            minimum_weight = weight
            # Set the minimum weight vertex to the vertex
            minimum_weight_vertex = vertex
            # Set the minimum weight vertex from to the start vertex
            minimum_weight_vertex_from = start_vertex
    # Append the minimum weight vertex to the visited vertices
    visited_vertices.append(minimum_weight_vertex)
    # Set the start vertex to the minimum weight vertex
    start_vertex = minimum_weight_vertex
    # If the start vertex is not in the visited vertices
    if start_vertex not in visited_vertices:
        # Recursively call the function
        branch_and_bound(graph, start_vertex)
    # Return the visited vertices
    return visited_vertices

# Initialize the visited vertices
visited_vertices = []
# Initial
unvisited_vertices = []
# For each vertex in the graph
for vertex in range(len(graph)):
    # If the vertex is not in
    if vertex not in visited_vertices:
        # Append the vertex to the unvisited vertices
        unvisited_vertices.append(vertex)
graph = [
    [0, 1, 2, 3, 4, 5, 6],
    [1, 0, 1, 2, 3, 4, 5],
    [2, 1, 0, 1, 2, 3, 4],
    [3, 2, 1, 0, 1, 2, 3],
    [4, 3, 2, 1, 0, 1, 2],
    [5, 4, 3, 2, 1, 0, 1],
    [6, 5, 4, 3, 2, 1, 0],
]
# Call the branch and bound function
# visited_vertices = branch_and_bound(graph, 0)
# Print the visited vertices
print(visited_vertices)



# Graph Coloring
"""
Given a graph, find a way to color it such that no two adjacent vertices have the same color.
"""

# Initialize the graph
graph = [
    [0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0],
]
# Initialize the colors
colors = [0, 1, 2, 3, 4, 5, 6]
# Initialize the color
color = 0
# Initialize the uncolored vertices
uncolored_vertices = [0, 1, 2, 3, 4, 5, 6]
# Initialize the colored vertices
colored_vertices = []


def color_graph(graph, colors, color, uncolored_vertices, colored_vertices):
    # If the uncolored vertices is empty
    if len(uncolored_vertices) == 0:
        # Return the colored vertices
        return colored_vertices
    # Initialize the vertex
    vertex = uncolored_vertices[0]
    # For each color in the colors
    for i in range(len(colors)):
        # If the color is not in the colored vertices
        if colors[i] not in colored_vertices:
            # If the color is consistent with the graph
            if consisdtent(vertex, i, graph, colored_vertices):
                # Append the color to the colored vertices
                colored_vertices.append(colors[i])
                # Append the vertex to the uncolored vertices
                uncolored_vertices.append(vertex)
                # Return the color_graph
                return color_graph(
                    graph, colors, color, uncolored_vertices, colored_vertices
                )
    # Remove the vertex from the uncolored vertices
    uncolored_vertices.remove(vertex)
    # Return the color_graph
    return color_graph(graph, colors, color, uncolored_vertices, colored_vertices)


def consisdtent(vertex, color, graph, colored_vertices):
    # For each vertex in the graph
    for i in range(len(graph)):
        # If the vertex is not the
        if i != vertex:
            # If the vertex is adjacent to the vertex
            if graph[vertex][i] == 1:
                # If the color is in the colored vertices
                if color in colored_vertices:
                    # Return False
                    return False

    # Return True
    return True


# driver code
print(color_graph(graph, colors, color, uncolored_vertices, colored_vertices))


# n-Queen Problem


# Initialize the board
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# Initialize the queens
queens = [0, 1, 2, 3]
# Initialize the queens_placed
queens_placed = []
# Initialize the queens_not_placed
queens_not_placed = [0, 1, 2, 3]
# Initialize the row
row = 0
# Initialize the col and col_index
col = 0
col_index = 0
# Initialize the count
count = 0


def place_queen(
    board, queens, queens_placed, queens_not_placed, row, col, col_index, count
):
    # If the row is greater than or equal to the length of the board
    if row >= len(board):
        # Return the count
        return count
    # If the col is greater than or equal to the length of the board
    if col >= len(board):
        # Set the row to 0
        row = 0
        # Set the col to 0
        col = 0
        # Set the col_index to 0
        col_index = 0
        # Increment the count
        count += 1
        # Return the place_queen
        return place_queen(
            board, queens, queens_placed, queens_not_placed, row, col, col_index, count
        )
    # If the col_index is greater than or equal to the length of the board
    if col_index >= len(board):
        # Set the col_index to 0
        col_index = 0
        # Increment the row
        row += 1
        # Set the col to 0
        col = 0
        # Return the place_queen
        return place_queen(
            board, queens, queens_placed, queens_not_placed, row, col, col_index, count
        )
    # If the board[row][col] is not equal to 0
    if board[row][col] != 0:
        # Increment the col
        col += 1
        # Return the place_queen
        return place_queen(
            board, queens, queens_placed, queens_not_placed, row, col, col_index, count
        )
    # If the board[row][col] is equal to 0
    if board[row][col] == 0:
        # Set the board[row][col] to the queens[col_index]
        board[row][col] = queens[col_index]
        # Increment the col
        col += 1
        # Increment the col_index
        col_index += 1
        # Return the place_queen
        return place_queen(
            board, queens, queens_placed, queens_not_placed, row, col, col_index, count
        )


def print_board(board):
    # Loop through the board
    for row in board:
        # Loop through the row
        for col in row:
            # Print the col
            print(col, end=" ")
            # If the col is equal to the length of the board
            if col == len(board):
                # Print a new line
                print()



def hamiltonian_cycle(graph, start, end):
    # Create a visited list
    visited = []
    # Create a stack
    stack = []
    # Push the start node to the stack
    stack.append(start)
    # While the stack is not empty
    while stack:
        # Pop the last item from the stack
        node = stack.pop()
        # If the node is not in the visited list
        if node not in visited:
            # Append the node to the visited list
            visited.append(node)
            # If the node is equal to the end node
            if node == end:
                # Return True
                return True
            # Loop through the graph
            for neighbor in graph[node]:
                # Push the neighbor to the stack
                stack.append(neighbor)
    # Return False
    return False


# driver code
if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E"],
        "D": ["B", "C", "E", "F"],
        "E": ["C", "D", "F"],
        "F": ["D", "E"],
    }
    # Call the function
    answer = hamiltonian_cycle(graph, "A", "F")
    # Print the answer
    print(answer)


# Sum of Subsets.
"""
Given a set of distinct integers, S, return all possible subsets.


"""

# implementation of sum of subsets


def sum_of_subsets(S, n):
    # Initialize the result
    result = []
    # Initialize the subset
    subset = []
    # Call the helper function
    helper(S, n, 0, subset, result)
    # Return the result
    return result


def helper(S, n, i, subset, result):
    # If the subset sum is equal to the n
    if sum(subset) == n:
        # Append the subset to the result
        result.append(subset[:])
    # If the subset sum is less than the n
    elif sum(subset) < n:
        # Loop through the list
        for j in range(i, len(S)):
            # Append the element to the subset
            subset.append(S[j])
            # Call the helper function
            helper(S, n, j + 1, subset, result)
            # Remove the last element from the subset
            subset.pop()


# driver code
if __name__ == "__main__":
    S = [1, 2, 3]
    n = 3
    # Call the function
    result = sum_of_subsets(S, n)
    # Print the result
    print(result)


# Subset Sum.
"""
Given a set of distinct integers, S, return all possible subsets.


"""

# implementation of subset sum


def subset_sum(S, n):
    # Initialize the result
    result = []
    # Initialize the subset
    subset = []
    # Call the helper function
    helper(S, n, 0, subset, result)
    # Return the result
    return result


def helper(S, n, i, subset, result):
    # If the subset sum is equal to the n
    if sum(subset) == n:
        # Append the subset to the result
        result.append(subset[:])
    # If the subset sum is less than the n
    elif sum(subset) < n:
        # Loop through the list
        for j in range(i, len(S)):
            # Append the element to the subset
            subset.append(S[j])
            # Call the helper function
            helper(S, n, j + 1, subset, result)
            # Remove the last element from the subset
            subset.pop()


# driver code
if __name__ == "__main__":
    S = [1, 2, 3]
    n = 3
    # Call the function
    result = subset_sum(S, n)
    # Print the result
    print(result)


# Selected Topics: Algebraic Computation

# Fast Fourier Transform
"""
Given an array of integers, A, find the length of the longest
subarray that contains at most 2 distinct integers.

"""

# implementation of FFT


def FFT(A):
    # Initialize the result
    result = []
    # Initialize the power
    power = 0
    # Loop through the list
    for i in range(len(A)):
        # If the power is less than the length of the list
        if power < len(A):
            # Append the element to the result
            result.append(A[power])
            # Increment the power
            power += 1
        # If the power is greater than the length of the list
        else:
            # Increment the power
            power += 1
    # Return the result
    return result


# driver code
if __name__ == "__main__":
    A = [1, 2, 3, 1, 2, 3]
    # Call the function
    result = FFT(A)
    # Print the result
    print(result)


# Selected Topics: Algebraic Computation

# Longest Common Subsequence
"""
Given two sequences, find the length of longest subsequence present in both of them.

A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

"""


# implementation of LCS


def LCS(X, Y):
    # Initialize the result
    result = []
    # Initialize the table
    table = [[0 for i in range(len(Y) + 1)] for j in range(len(X) + 1)]
    # Loop through the table
    for i in range(1, len(X) + 1):
        # Loop through the table
        for j in range(1, len(Y) + 1):
            # If the first element is equal to the second element
            if X[i - 1] == Y[j - 1]:
                # Increment the table
                table[i][j] = table[i - 1][j - 1] + 1
            # If the first element is not equal to the second element
            else:
                # Increment the table
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    # Initialize the length
    length = table[len(X)][len(Y)]
    # Initialize the index
    index = length
    # Initialize the first index
    i = len(X)
    # Initialize the second index
    j = len(Y)
    # While the length is greater than 0
    while length > 0:
        # If the first element is equal to the second element
        if X[i - 1] == Y[j - 1]:
            # Append the element to the result
            result.append(X[i - 1])
            # Decrement the length
            length -= 1
            # Decrement the first index
            i -= 1
            # Decrement the second index
            j -= 1
        # If the first element is not equal to the second element
        else:
            # If the first element is greater than the second element
            if table[i - 1][j] > table[i][j - 1]:
                # Decrement the first index
                i -= 1
            # If the first element is less than the second element
            else:
                # Decrement the second index
                j -= 1
                # Append the element to the result
                result.append(X[i - 1])
                # Decrement the length
                length -= 1
    # Reverse the result
    result.reverse()
    # Return the result
    return result


# Driver code
if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(LCS(X, Y))


# String Matching
# Given two strings, write a function to determine if the second string is an anagram of
# the first.


def anagram(s1, s2):
    # Initialize the dictionary
    d = {}
    # Initialize the result
    result = True
    # For each element in the first string
    for i in s1:
        # If the element is not in the dictionary
        if i not in d:
            # Add the element to the dictionary
            d[i] = 1
        # If the element is in the dictionary
        else:
            # Increment the value
            d[i] += 1
    # For each element in the second string
    for i in s2:
        # If the element is not in the dictionary
        if i not in d:
            # Set the result to False
            result = False
            # Break the loop
            break
        # If the element is in the dictionary
        else:
            # Decrement the value
            d[i] -= 1
    # Return the result
    return result


# Driver code
if __name__ == "__main__":
    s1 = "anagram"
    s2 = "nagaram"
    print(anagram(s1, s2))


# Theory of NP-Completeness
# Given a set of positive integers, find the largest subset such that every pair (Si, Sj) of elements in the subset
# satisfies: Si % Sj = 0 or Sj % Si = 0.

# Approximation Algorithms and Randomized Algorithms

# Implementation of Randomized Algorithm


def randomized_algorithm(nums):
    # Initialize the result
    result = []
    # Initialize the list
    list = nums[:]
    # Sort the list
    list.sort()
    # Initialize the index
    index = 0
    # While the index is less than the length of the list
    while index < len(list):
        # Append the element to the result
        result.append(list[index])
        # Increment the index
        index += 1
    # Return the result
    return result

    # Driver code


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(randomized_algorithm(nums))


# Implementation of Approximation Algorithm


def approximation_algorithm(nums):
    # Initialize the result
    result = []
    # Initialize the list
    list = nums[:]
    # Sort the list
    list.sort()
    # Initialize the index
    index = 0
    # While the index is less than the length of the list
    while index < len(list):
        # Append the element to the result
        result.append(list[index])
        # Increment the index
        index += 1
    # Return the result
    return result


# Driver code
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(approximation_algorithm(nums))
