# Queue implementation using a list
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
            return item
        else:
            print("Dequeue failed: Queue is empty.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Peek failed: Queue is empty.")
            return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self.queue)

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front item:", queue.peek())  
print("Queue size:", queue.size())  
queue.dequeue() 
print("Queue size after dequeue:", queue.size()) 

print("Is queue empty?", queue.is_empty())  
