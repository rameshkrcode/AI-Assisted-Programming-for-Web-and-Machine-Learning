
import gc
def process_large_data():
    large_list = []
    for i in range(10**6):
        large_list.append(str(i))  # Simulate memory-intensive operation
    # Manually delete the large object if it's no longer needed
    del large_list
    # Explicitly invoke garbage collection to free memory
    gc.collect()
