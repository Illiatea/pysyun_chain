class Pipeline:
    def __init__(self, processor):
        self.processor = processor

    def process(self, data):
        return self.processor.process(data)

    def __or__(self, other):
        return Pipeline(ChainedProcessor(self.processor, other.processor))


class ChainedProcessor:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def process(self, data):
        processed = self.first.process(data)
        return self.second.process(processed)
