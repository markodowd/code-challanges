class OrderedStream:

    def __init__(self, n: int):
        self.store = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        self.store[idKey - 1] = value
        chunk = []
        while self.ptr < len(self.store) and self.store[self.ptr] is not None:
            chunk.append(self.store[self.ptr])
            self.ptr += 1
        return chunk
