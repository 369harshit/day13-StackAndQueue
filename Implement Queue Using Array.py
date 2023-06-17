class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def top(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]


# Example usage
queue = Queue()

print("Is Queue empty?", queue.is_empty())
print("Queue size:", queue.size())

queue.push(4)
queue.push(14)
queue.push(24)
queue.push(34)

print("Queue size after pushing elements:", queue.size())
print("Top element:", queue.top())

popped_item = queue.pop()
print("Popped item:", popped_item)

print("Queue size after popping an element:", queue.size())
print("Top element after popping:", queue.top())
