# PySyun Chain
This library is for chaining processors into linear pipelines.

# Pipeline Class

The `Pipeline` class allows you to create data processing pipelines using different processors. It provides an easy way to combine and perform sequential data processing using multiple processors.

## Initialization

To create a `Pipeline` object, you need to pass a processor to it:

```python
processor = SomeProcessor()
pipeline = Pipeline(processor)
```

## Methods

### process(data)

The `process` method processes the `data` using the processor that was passed during the initialization of the `Pipeline` object. It returns the result of the data processing.

```python
result = pipeline.process(data)
```

### \_\_or\_\_(other)

The `__or__` method allows you to combine two `Pipeline` objects into a single data processing pipeline. It creates a new `Pipeline` object that contains a `ChainedProcessor`, which sequentially processes the data first by the first processor and then by the second processor.

```python
pipeline1 = Pipeline(Processor1())
pipeline2 = Pipeline(Processor2())
chained_pipeline = pipeline1 | pipeline2
```

## Usage Examples

Suppose we have two simple processors:

```python
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

pipeline = Pipeline(random_processor) | Pipeline(print_processor)
```

Now, when we call the `process` method on the `pipeline` object, it will generate a random array using the `RandomArrayProcessor` and then print it using the `PrintProcessor`:

```python
result = pipeline.process(None)
# Output the generated random array, for example:
# [42, 68, 35, 1, 70, 25, 79, 59, 63, 65]
```

Thus, the `Pipeline` class allows you to conveniently create data processing pipelines and combine different processors for sequential data processing.