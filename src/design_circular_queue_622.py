class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.rear = 0
        self.front = 0
        self.capability = k + 1
        self.nums = [0 for _ in range(self.capability)]

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if not self.isFull():
            self.nums[self.rear] = value
            self.rear = (self.rear + 1) % self.capability
            return True
        else:
            return False
        
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capability
            return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.isEmpty():
            return self.nums[self.front]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.isEmpty():
            return self.nums[(self.rear - 1 + self.capability) % self.capability]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return True if self.front == self.rear else False
        
    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return True if (self.rear + 1) % self.capability == self.front else False
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
