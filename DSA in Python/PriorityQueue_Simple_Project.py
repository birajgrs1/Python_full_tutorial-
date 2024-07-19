class Auction:
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


def auction_process(auction):
    while True:
        print("\n1. Add bid\n2. Remove highest bid\n3. Show all bids\n4. Search for a bid\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                priority = int(input("Enter bid amount: "))
                item = input("Enter bidder name: ")
                auction.add(priority, item)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '2':
            auction.remove()

        elif choice == '3':
            auction.show()

        elif choice == '4':
            item = input("Enter bidder name to search: ")
            auction.search(item)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


auction = Auction()
auction_process(auction)
