import heapq

# 1. Create a heap from an existing list
data = [5, 1, 9, 3]
heapq.heapify(data)  # Modifies the list in-place into a min-heap
print("Min-Heap:", data)  # The first element will be 1

# 2. Push a new element
heapq.heappush(data, 2)

# 3. Pop the smallest element
smallest = heapq.heappop(data)
print("Popped Smallest:", smallest)  # Outputs 1
print("Remaining Heap:", data)       # 2 is now at the root
