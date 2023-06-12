class queue:
    def __init__(self):
        self.items = []

    def enqueue(self,items):
        self.items.append(items)

    def dequeue(self,n=1):
        counter = 0 
        while not self.is_empty() and counter < n:
            self.items.pop(0)

            counter += 1

    def is_empty(self):
        if not self.items:
            return True
        return False
    
    def __str__(self) :
        res = "start- "
        for s in self.items:
            res += str(s) + " "
        res += " -end"

        return res
    
q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue(2)

print(q)

        

