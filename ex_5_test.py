from ex_5 import Queue

qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
# qu.queue.print_all_nodes()
while qu.size() > 0:
    print(qu.dequeue())