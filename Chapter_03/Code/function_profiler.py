
import time

def profile_function(func, *args, **kwargs):
    """ Measures function execution time and suggests optimizations """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time:.6f} seconds")
    # Basic optimization suggestion based on execution time
    if execution_time > 1.0:
        print("⚠️ Optimization Needed: Consider using NumPy, parallelization, or algorithm improvements.")
    return result

# Example usage
def sample_function(n):
    return sum(range(n))

profile_function(sample_function, 1000000)
