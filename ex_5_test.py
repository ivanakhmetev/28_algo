from ex_5 import Queue

qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
# qu.queue.print_all_nodes()
while qu.size() > 0:
    print(qu.dequeue())

class Circle():

    def __init__(self):
        self.sectors = []

    def append(self, value):
        self.sectors.append(value)

    def __getitem__(self, i):
        if len(self.sectors) == 0:
            return None
        return self.sectors[i % len(self.sectors)]
    
circle = Circle()
for i in range(20):
    circle.append(i)

qu = Queue()
start_pos = 5
for i in range(start_pos):
    qu.enqueue(circle[i])

def round(shift: int):
    i = 0
    while i < shift:
        qu.dequeue()
        qu.enqueue(circle[start_pos + i])
        i += 1

print('original queue')        
qu.queue.print_all_nodes()
round(19)
print('aftershift queue')  
qu.queue.print_all_nodes()

