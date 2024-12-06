import concurrent.futures
import asyncio


class Chainable:
    def __init__(self, processor):
        self.processor = processor

    def process(self, data):
        return self.processor.process(data)

    def __or__(self, other):
        if isinstance(other, ChainableGroup):
            other.next_processor = self
            return other
        return Chainable(ChainedProcessor(self.processor, other.processor))


class ChainedProcessor:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def process(self, data):
        processed = self.first.process(data)
        return self.second.process(processed)


class ChainableGroup:
    def __init__(self, num_threads=None):
        self.num_threads = num_threads
        self.pipeline = None

    def process(self, data):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            return list(executor.map(self.process_item, data))

    def process_item(self, item):
        items = item if isinstance(item, list) else [item]
        return self.pipeline.process(items)

    def __or__(self, other):
        if self.pipeline is None:
            self.pipeline = other
        else:
            self.pipeline = self.pipeline | other
        return self


class AsyncChainable:
    def __init__(self, processor):
        self.processor = processor

    async def process(self, data):
        return await self.processor.process(data)

    def __or__(self, other):
        if isinstance(other, AsyncChainableGroup):
            other.pipeline = self
            return other
        return AsyncChainable(AsyncChainedProcessor(self.processor, other.processor))


class AsyncChainedProcessor:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    async def process(self, data):
        processed = await self.first.process(data)
        return await self.second.process(processed)


class AsyncChainableGroup:
    def __init__(self, concurrency=None):
        self.concurrency = concurrency
        self.pipeline = None

    async def process(self, data):
        semaphore = asyncio.Semaphore(self.concurrency or len(data))

        async def process_with_semaphore(item):
            async with semaphore:
                return await self.process_item(item)

        return await asyncio.gather(*[process_with_semaphore(item) for item in data])

    async def process_item(self, item):
        items = item if isinstance(item, list) else [item]
        return await self.pipeline.process(items)

    def __or__(self, other):
        if self.pipeline is None:
            self.pipeline = other
        else:
            self.pipeline = self.pipeline | other
        return self
