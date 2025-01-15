import matplotlib.pyplot as plt
import time

def sample_algorithm(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

# Collect data for plotting
input_sizes = [100, 200, 400, 800, 1600]
times = []

for size in input_sizes:
    start = time.time()
    sample_algorithm(size)
    end = time.time()
    times.append(end - start)

# Plot results
plt.plot(input_sizes, times, marker='o')
plt.title('Algorithm Performance')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.show()
