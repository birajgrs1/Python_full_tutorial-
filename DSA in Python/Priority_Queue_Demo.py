class PriorityQueue:
    def __init__(self):
        self.queue = []

    def add(self, priority, item):
        self.queue.append((priority, item))
        self.queue.sort(reverse=True, key=lambda x: x[0])
        print(f"Added: {(priority, item)}")

    def remove(self):
        if self.queue:
            removed_item = self.queue.pop(0)
            print(f"Removed: {removed_item}")
            return removed_item
        else:
            print("Priority queue is empty")
            return None

    def show(self):
        print("Current priority queue:")
        for item in self.queue:
            print(item)

    def search(self, item):
        for priority, element in self.queue:
            if element == item:
                print(f"Found {item} with priority {priority}")
                return (priority, item)
        print(f"{item} not found in the priority queue")
        return None


pq = PriorityQueue()
pq.add(3, 'Task 3')
pq.add(1, 'Task 1')
pq.add(2, 'Task 2')

pq.show()

pq.remove()
pq.show()

pq.search('Task 2')
pq.search('Task 1')
