import time
import random
from pysyun_chain import Chainable, ChainableGroup


class C:
    @staticmethod
    def process(item):
        time.sleep(0.01)  # Simulate a heavy operation
        return [item[0] * item[0]]


class D:
    @staticmethod
    def process(item):
        time.sleep(0.01)  # Simulate a heavy operation
        return [item[0] * item[0]]


def generate_large_input(size):
    return [random.randint(1, 100) for _ in range(size)]


def sequential_process(data):
    result = []
    for item in data:
        pipeline = Chainable(C()) | Chainable(D())
        processed = pipeline.process([item])
        result.append(processed)
    return result


def parallel_process(data):
    pipeline = ChainableGroup(4) | Chainable(C()) | Chainable(D())
    return pipeline.process(data)


def run_test(process_func, input_data):
    start_time = time.time()
    result = process_func(input_data)
    end_time = time.time()
    return result, end_time - start_time


# Test
input_size = 1000
input_data = generate_large_input(input_size)

print(f"Testing with {input_size} elements:")
print(f"First 10 elements of input data: {input_data[:10]}")
print(f"...")
print(f"Last 10 elements of input data: {input_data[-10:]}")
print()

sequential_result, sequential_time = run_test(sequential_process, input_data)
print(f"Sequential execution: {sequential_time:.2f} seconds")
print(f"First 10 elements of result: {sequential_result[:10]}")
print(f"...")
print(f"Last 10 elements of result: {sequential_result[-10:]}")
print()

parallel_result, parallel_time = run_test(parallel_process, input_data)
print(f"Parallel execution: {parallel_time:.2f} seconds")
print(f"First 10 elements of result: {parallel_result[:10]}")
print(f"...")
print(f"Last 10 elements of result: {parallel_result[-10:]}")
print()

# Check for correctness of results
assert sequential_result == parallel_result, "Results do not match!"

speedup = sequential_time / parallel_time
print(f"Speedup: {speedup:.2f}x")
