class Queue(object):
    def __init__(self,limit=5):
        self.que=[]
        self.limit=limit
        self.front=None
        self.rear=None
        self.size=0
    
    def isEmpty(self):
        return self.size<=0

    def enQueue(self,item):
        if self.size >=self.limit:
            print(f"Queue overflow!!")
            return
        else:
            self.que.append(item)

        if self.front is None:
            self.front=self.rear=0
        else:
            self.rear=self.size
        self.size=self.size+1
        
    def deQueue(self):
        if self.size <=0:
            print("Queue underflow!!")
            return 0
        else:
            x=self.que.pop(0)
            self.size-=1
            if self.size ==0:
                self.front = self.rear = None
            else:
                self.rear=self.size-1
            return x
    
    def queueFront(self):
        if self.rear is None:
            print("Sorry queue is empty!!")
            return
        return self.que[self.front]

    def queueRear(self):
        if self.rear is None:
            print("Sorry queue is empty!!")
            return
        return self.que[self.rear]

    def Size(self):
        return self.size


#---------Dry Run---------

Qu = Queue()
Qu.enQueue(1)
Qu.enQueue(2)
Qu.enQueue(3)
Qu.enQueue(4)
Qu.enQueue(5)
Qu.enQueue(6)
print(f"Queue is : {Qu.que}")
print(f"Element at front: {Qu.queueFront()}")
print(f"ELement at reat: {Qu.queueRear()}")
print(f"Element dequeued: {Qu.deQueue()}")
print(f"Element dequeued: {Qu.deQueue()}")
print(f"Element dequeued: {Qu.deQueue()}")
print(f"Queue is : {Qu.que}")

