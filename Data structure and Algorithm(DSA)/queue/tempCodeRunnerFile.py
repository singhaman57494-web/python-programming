def dequeue(self):
        if self.front == None:
            return "queue is empty"

        return self.front = self.front.next