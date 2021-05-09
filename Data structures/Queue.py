class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)
        return "Added " + str(val)

    def dequeue(self):
        if len(self.queue)!=0:
            return self.queue.pop(0)
        return "Queue is empty"

    def front(self):
        if len(self.queue)!=0:
            return self.queue[0]
        return "Queue is empty"

    def read(self):
        if len(self.queue)!=0:
            return self.queue[-1]
        return "Queue is empty"

queue = Queue()

print(queue.enqueue(1))
print(queue.enqueue(2))
print(queue.enqueue(3))
print(queue.dequeue())
print(queue.front())
print(queue.dequeue())