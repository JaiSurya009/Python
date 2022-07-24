class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
  
    # for popping an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
  
if __name__ == '__main__':
    myQueue = PriorityQueue()
    print("Is Queue Empty:", myQueue.isEmpty())
    myQueue.insert(22)
    myQueue.insert(10)
    myQueue.insert(14)
    myQueue.insert(17)
    myQueue.insert(16)
    myQueue.insert(20)
    print("Is Queue Empty:", myQueue.isEmpty())
    print(myQueue)
    myQueue.delete()
    myQueue.delete()
    myQueue.delete()
    print(myQueue)
    print("Is Queue Empty:", myQueue.isEmpty())
    while not myQueue.isEmpty():
        print(myQueue.delete())
        