
import memProc


class priProc(memProc):
    def __init__(self):
        # Min-heap to store memory blocks
        self.memory_heap = []

    def addMemBlock(self, size):
        heapq.heappush(self.memory_heap, size)
        print(f"Added memory block of size {size}.")

    def allocateMem(self, required_size):
        for i, block in enumerate(self.memory_heap):
            if block >= required_size:
                allocated_block = self.memory_heap.pop(i)
                heapq.heapify(self.memory_heap) 
                print(f"Allocated memory block of size {allocated_block} for request of size {required_size}.")
                return allocated_block
        print(f"No memory block available for request of size {required_size}.")
        return None

    def release_memory(self, size):
        heapq.heappush(self.memory_heap, size)
        print(f"Released memory block of size {size} back to the pool.")

    def display_memory_pool(self):
        """Displays the current state of the memory pool."""
        print(f"Current memory pool: {self.memory_heap}")
