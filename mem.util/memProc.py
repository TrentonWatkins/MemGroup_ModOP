# Single mem process - one of the three that would run at the same time

# Fully define what memory process needs
#   Page(s), command queue, etc
class MemoryProc:
    def __init__(self,pross):
# netCodesocets ports to listen to 99887 from storage 
#send to process management 
#create impliment interfaces for pages and index so subclasses can inhearet traits

    #TODO:Private Heap:
    #Python manages memory through a private heap, which is a portion of memory dedicated to the Python process.
    # This heap contains all Python objects and data structures -Trenton
    import heapq

    #TODO:The mmap module allows you to map a file or a portion of it directly into memory.
    # This can be useful for working with large files efficiently or for interfacing with shared memory. - Alex 
