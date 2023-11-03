import time
import math
import matplotlib.pyplot as plt

# Naive iterative method to compute n^k
def naive(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

# Divide and conquer method to compute n^k
def helper(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_power = helper(base, exponent // 2)
        time.sleep(0.1)
        return half_power * half_power
    else:
        half_power = helper(base, (exponent - 1) // 2)
        time.sleep(0.1)
        return base * half_power * half_power
# Measure execution times for different input sizes
input_sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
naive_times = []
helper_times = []

for size in input_sizes:
    start_time = time.time()
    naive(2, size)
    naive_times.append(time.time() - start_time)
    
    start_time = time.time()
    helper(2, size)
    helper_times.append(time.time() - start_time)

plt.figure(figsize=(8, 6))
plt.plot(input_sizes, naive_times, marker='o', label='Naive Iterative')
plt.plot(input_sizes, helper_times, marker='o', label='Divide and Conquer')
plt.yscale('log')  # Use logarithmic scale for y-axis
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds, log scale)')
plt.title('Algorithm Performance')
plt.legend()
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.show()
