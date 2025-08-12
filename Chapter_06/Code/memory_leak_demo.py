
import time
def memory_leak():
    leaks = []
    while True:
        leaks.append("Memory leak!")  # Unbounded memory growth
        time.sleep(1)
