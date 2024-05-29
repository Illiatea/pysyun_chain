class Chainable:

    def __init__(self, processor):
        self.processor = processor

    def process(self, data):
        return self.processor.process(data)

    def __or__(self, other):
        return Chainable(ChainedProcessor(self.processor, other.processor))


class ChainedProcessor:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def process(self, data):
        processed = self.first.process(data)
        return self.second.process(processed)


class AsyncChainable:

    def __init__(self, processor):
        self.processor = processor

    async def process(self, data):
        return await self.processor.process(data)

    def __or__(self, other):
        return AsyncChainable(AsyncChainedProcessor(self.processor, other.processor))


class AsyncChainedProcessor:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    async def process(self, data):
        processed = await self.first.process(data)
        return await self.second.process(processed)
