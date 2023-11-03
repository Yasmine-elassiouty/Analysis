import time
import matplotlib.pyplot as plt

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def binarySearch(a, key, i, j):
    if j >= i:
        mid = (i + j) // 2
        if a[mid] == key:
            return mid
        if a[mid] > key:
            return binarySearch(a, key, i, mid - 1)
        else:
            return binarySearch(a, key, mid + 1, j)
    return -1

def findPairs(arr, sum):
    sorted_arr = mergeSort(arr)
    pairs = []
    for i in range(len(sorted_arr)):
        complement = sum - sorted_arr[i]
        index = binarySearch(sorted_arr, complement, i + 1, len(sorted_arr) - 1)
        if index != -1:
            pairs.append((sorted_arr[i], sorted_arr[index]))
    return pairs


S = [10, 3, 5, 2, 7, 1, 9, 4, 6, 8]
sum = 10
pairs = findPairs(S, sum)
print("Pairs with sum",sum, "are:", pairs)

input_sizes = [10**i for i in range(10)]  # [1, 10, 100, 1000, 10000, 100000, 1000000]
execution_times = []

for size in input_sizes:
    input_array = list(range(size, 0, -1)) 
    start_time = time.time()
    mergeSort(input_array)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

# Plot the experimental results
plt.figure(figsize=(8, 6))
plt.plot(input_sizes, execution_times, marker='o', color='b', label='Experimental Time')
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time (seconds)')
plt.yscale('log')  
plt.title('Merge Sort Algorithm Scalability')
plt.legend()
plt.grid(True)
plt.show()