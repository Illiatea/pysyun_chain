# PySyun Chain
This library is for chaining processors into linear pipelines.

# Chainable Class

The `Chainable` class allows you to create data processing pipelines using different processors. It provides an easy way to combine and perform sequential data processing using multiple processors.

## Initialization

To create a `Chainable` object, you need to pass a processor to it:

```python
processor = SomeProcessor()
pipeline = Chainable(processor)
```

## Methods

### process(data)

The `process` method processes the `data` using the processor that was passed during the initialization of the `Chainable` object. It returns the result of the data processing.

```python
result = pipeline.process(data)
```

### \_\_or\_\_(other)

The `__or__` method allows you to combine two `Chainable` objects into a single data processing pipeline. It creates a new `Chainable` object that contains a `ChainedProcessor`, which sequentially processes the data first by the first processor and then by the second processor.

```python
pipeline1 = Chainable(Processor1())
pipeline2 = Chainable(Processor2())
chained_pipeline = pipeline1 | pipeline2
```

Or simply:
```python
chained_pipeline = Chainable(Processor1()) | Chainable(Processor2())
```

## Usage Examples

Suppose we have two simple processors:

```python
import

import random

class RandomArrayProcessor:
    def process(self, _):
        return [random.randint(0, 100) for _ in range(10)]

class PrintProcessor:
    def process(self, data):
        print(data)
        return data
```

We can create a pipeline with these processors:

```python
random_processor = RandomArrayProcessor()
print_processor = PrintProcessor()

pipeline = Chainable(random_processor) | Chainable(print_processor)
```

Now, when we call the `process` method on the `Chainable` object, it will generate a random array using the `RandomArrayProcessor` and then print it using the `PrintProcessor`:

```python
result = pipeline.process(None)
# Output the generated random array, for example:
# [42, 68, 35, 1, 70, 25, 79, 59, 63, 65]
```

Thus, the `Chainable` class allows you to conveniently create data processing pipelines and combine different processors for sequential data processing.

# AsyncChainable Class

The `AsyncChainable` class allows you to create asynchronous data processing pipelines using different processors. It provides an easy way to combine and perform sequential asynchronous data processing using multiple processors.

## Initialization

To create an `AsyncChainable` object, you need to pass an asynchronous processor to it:

```python
processor = SomeAsyncProcessor()
pipeline = AsyncChainable(processor)
```

## Methods

### async process(data)

The `process` method processes the `data` using the processor that was passed during the initialization of the `AsyncChainable` object. It returns the result of the data processing.

```python
result = await pipeline.process(data)
```

### \_\_or\_\_(other)

The `__or__` method allows you to combine two `AsyncChainable` objects into a single data processing pipeline. It creates a new `AsyncChainable` object that contains an `AsyncChainedProcessor`, which sequentially processes the data first by the first processor and then by the second processor.

```python
pipeline1 = AsyncChainable(Processor1())
pipeline2 = AsyncChainable(Processor2())
chained_pipeline = pipeline1 | pipeline2
```

Or simply:
```python
chained_pipeline = AsyncChainable(Processor1()) | AsyncChainable(Processor2())
```

## Usage Examples

Suppose we have two simple asynchronous processors:

```python
import asyncio
import random

class AsyncRandomArrayProcessor:
    async def process(self, _):
        await asyncio.sleep(1)  # Simulate asynchronous operation
        return [random.randint(0, 100) for _ in range(10)]

class AsyncPrintProcessor:
    async def process(self, data):
        await asyncio.sleep(1)  # Simulate asynchronous operation
        print(data)
        return data
```

We can create an asynchronous pipeline with these processors:

```python
random_processor = AsyncRandomArrayProcessor()
print_processor = AsyncPrintProcessor()

pipeline = AsyncChainable(random_processor) | AsyncChainable(print_processor)
```

Now, when we call the `process` method on the `AsyncChainable` object, it will generate a random array using the `AsyncRandomArrayProcessor` and then print it using the `AsyncPrintProcessor`:

```python
import asyncio

async def main():
    result = await pipeline.process(None)
    # Output the generated random array, for example:
    # [42, 68, 35, 1, 70, 25, 79, 59, 63, 65]

asyncio.run(main())
```

Thus, the `AsyncChainable` class allows you to conveniently create asynchronous data processing pipelines and combine different processors for sequential asynchronous data processing.