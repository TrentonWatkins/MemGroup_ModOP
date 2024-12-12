import heapq

memory_heap1 = []
memory_heap2 = []
memory_heap3 = []

def addMemBlock(memory_heap, fileName):
    heapq.heappush(memory_heap, fileName)
    print(f"Added memory block of size {fileName}.")

def allocateMem(memory_heap, file):
    for i, block in enumerate(memory_heap):
        if block == "emptyBlock":
            allocated_block =  memory_heap.pop(i)
            heapq.heapify(memory_heap)
            print(f"Allocated memory block of size {allocated_block} for request of {file}.")
            return allocated_block
    print(f"No memory block available for request of {file}.")
    return None


def replaceMemBlock(memory_heap, fileName):
    for i, block in enumerate(memory_heap):
        if block == "emptyBlock":
            memory_heap.pop(i)
            addMemBlock(memory_heap, fileName)


def release_memory(memory_heap, file):
    heapq.heappush(memory_heap, file)
    heapq.heapify(memory_heap)
    print(f"Released memory block of {file} back to the pool.")
    for i, block in enumerate(memory_heap):
        if block == file:
            memory_heap.pop(i)
            addMemBlock(memory_heap, "emptyBlock")

def display_memory_pool(memory_heap):
    """Displays the current state of the memory pool."""
    print(f"Current memory pool: {memory_heap}")
    
if __name__ == "__main__":
    try:
        # Run the scripts in the specified order
        addMemBlock(memory_heap1, "emptyBlock")
        addMemBlock(memory_heap1, "emptyBlock")
        addMemBlock(memory_heap1, "emptyBlock")
        addMemBlock(memory_heap1, "emptyBlock")
        addMemBlock(memory_heap1, "emptyBlock")
        print("Page one ")
        display_memory_pool(memory_heap1)
        allocateMem(memory_heap1, "File 1")
        display_memory_pool(memory_heap1)
        release_memory(memory_heap1, "File 1")
        display_memory_pool(memory_heap1)
    except Exception as e:
        print(f"An error occurred while running the scripts: {e}")
