# Name: Ganesh Kumar
# Date: 03/13/2025
# Instructor: Professor Andres Calle
# Course ID: CIST-005B-34571
# Project Description:
# This week, you'll practice implementing and using three fundamental data structures:
# Stacks, Queues, and Priority Queues.
# You will create a simplified theme park ride management simulation to better understand
# how these structures manage data.

# Implement a Stack (LIFO) to simulate guests using an elevator-style ride (loading and unloading guests).
# Implement a Queue (FIFO) to manage guests waiting in line for a popular roller coaster.
# Implement a Priority Queue to manage guests based on VIP status or Fast Pass holders.
# Demonstrate the practical use of stacks, queues, and priority queues through interactive simulation.
# Sets the LOW_PRIORITY, MEDIUM_PRIORITY, AND HIGH_PRIORITY.
LOW_PRIORITY = 10
MEDIUM_PRIORITY = 5
HIGH_PRIORITY = 1

# Create a Node class for the linked list.
class Node:
  def __init__(self, data):
      self.data = data

# Create a LinkedListStack class.
class LinkedListStack:
  # Initialize an empty stack by setting head to None.
  # Constructor
  def __init__(self):
      self.head = None


  # Add element to the top of the stack.
  def push(self, data):
      # Creating a new node object.
      newNode = Node(data)

      # If list is empty, insert the node at the beginning.
      if (self.head == None):
          self.head = newNode
          newNode.next = None
          return
      else:
          # Insert the node and adjust the head.
          newNode.next = self.head
          self.head = newNode
          return


  # Remove element from the top of the stack.
  def pop(self):
      # If stack is empty, return none.
      if (self.head == None):
          print("Stack is empty.")
          return None
      else:
          # Get the first node and adjust the head to point to the next node.
          currNode = self.head
          self.head = currNode.next
          return currNode.data

  # Checks to see if the stack is empty.
  def isEmpty(self):
      return self.head == None


# Create a class for a linked-list based queue.
class LinkedQueue:
  # Constructor
  def __init__(self):
      # Set head to none.
      self.head = None


  # Enqueue adds an element to the end of the queue.
  def enqueue(self, data):
      # Create a new node object.
      newNode = Node(data)
      # If the queue is empty, add the new node to the head.
      if self.head == None:
          self.head = newNode
          newNode.next = None
          return
      else:
          # Otherwise, add it to the end of the queue.
          curNode = self.head
          while curNode.next:
              curNode = curNode.next
      curNode.next = newNode
      newNode.next = None
      return

  # Dequeue removes an element from the front of the queue.
  def dequeue(self):
      # Check if the queue is empty and return None.
      if self.isQueueEmpty():
          print("Queue is empty")
          return None
      else:
          # Remove the first node from the head and adjust the head to point to the next node.
          curNode = self.head
          self.head = curNode.next
          return curNode.data

  # Check if the queue is empty.
  def isQueueEmpty(self):
      return self.head == None

# Derived node class for the priority queue.
class PriorityQueueNode(Node):
  # Constructor
  def __init__(self, data, priority):
      super().__init__(data)
      self.priority = priority

# Linked list based priority queue class.
class LinkedPriorityQueue:
   # Constructor
   def __init__(self):
       self.head = None

  # Enqueue based on the priority. Time complexity of enqueue is O(n) since we search and insert the element at the
  # end of the priority list.
   def priority_queue_enqueue(self, data, priority):
       # Create a new node object with data and priority.
       newNode = PriorityQueueNode(data, priority)
       # If queue is empty, enqueue it to the front of the queue.
       if self.priority_queue_isQueueEmpty():
           newNode.next = self.head
           self.head = newNode
           return
       # If queue is not empty and new node priority is less than the priority of the front of the queue,
       # insert it at the head and move the head.
       elif priority < self.head.priority:
           newNode.next = self.head
           self.head = newNode
           return
       else:
           curNode = self.head
           # New node priority is greater than or equal to the next node priority.
           while curNode.next and curNode.next.priority <= priority:
               curNode = curNode.next
           # Insert the new node at the end of the node with current priority.
           newNode.next = curNode.next
           curNode.next = newNode

   # Remove an element from the priority queue.
   def priority_queue_dequeue(self):
       # If the queue is empty, then return none.
       if self.priority_queue_isQueueEmpty():
           print("The queue is empty.")
           return None
       # Remove the head (highest-priority item)
       highest_priority_node = self.head
       self.head = self.head.next
       return highest_priority_node.data

   # Check if the priority queue is empty.
   def priority_queue_isQueueEmpty(self):
       return self.head == None

# Use a stack to simulate guests entering an elevator ride.
# Guests board one at a time and exit in reverse order (the last person in is the first out).
# board_guest(guest_name) adds a guest.
# start_ride(capacity) simulates the ride, displaying guest names as the guests exit the ride.
class ElevatorRide:
  # Constructor intializes the stack with an empty list.
  def __init__(self):
      self.rideStack = LinkedListStack() # Ride stack is a LIFO data structure. The last guest in comes out first.
      self.rideCapacity = 5 # Maximum number of elements in the stack.
      self.availableSpots = 5 # Keeps track of the available spots.


  # Boards guest on the elevator ride.
  def board_guest(self, guest):
      # Push operation of the elevator ride.
      if (self.availableSpots > 0):
          self.rideStack.push(guest)
          self.availableSpots -= 1


  # Begin the elevator ride.
  def start_ride(self, capacity):
      # Pop operation of the elevator ride.
      while (not self.isElevatorEmpty()):
          print(self.removeGuests(), end=' ')
      print()

  # Remove guests from the elevator ride.
  def removeGuests(self):
      if (self.isElevatorEmpty()):
          self.availableSpots = self.rideCapacity
          return None
      else:
          self.availableSpots += 1
          return self.rideStack.pop()

  # Checks if the elevator is empty.
  def isElevatorEmpty(self):
      return self.rideStack.head == None

# Use a queue to manage guests waiting for the roller coaster.
# Guests enter the queue and exit in the same order they arrived (first in, first out).
# join_queue(guest_name) adds a guest to the line.
# start_ride(capacity) - simulates loading and running the coaster, displaying guest names as they board.

# Create RollerCoasterRide class.
class RollerCoasterRide:
  # Constructor initializes the stack with an empty list.
  def __init__(self):
      # Creates a queue for roller coaster ride.
      self.rideQueue = LinkedQueue()
      # Maximum capacity of the roller coaster ride.
      self.rideCapacity = 5
      # Keeps track of the available spot.
      self.availableSpots = 5

  # Add guests to the roller coaster ride.
  def join_queue(self, guest):
      # If the available spots is greater than 0, enqueue the guest to the roller coaster ride.
      if (self.availableSpots > 0):
          self.rideQueue.enqueue(guest)
          # Decrement the available spots.
          self.availableSpots -= 1

  # Start the roller coaster ride.
  def start_ride(self):
      # Dequeue the guests.
      while (not self.isCoasterEmpty()):
          print(self.removeGuests(), end=' ')
      print()

  # Remove guests from the roller coaster ride.
  def removeGuests(self):
      # If roller coaster is empty, return none.
      if (self.isCoasterEmpty()):
          self.availableSpots = self.rideCapacity
          return None
      # Otherwise, add the available spots.
      else:
          self.availableSpots += 1
          return self.rideQueue.dequeue()

  # If roller coaster is empty, return the queue.
  def isCoasterEmpty(self):
      return self.rideQueue.isQueueEmpty()

# Use a priority queue to manage guests based on priority levels (e.g., VIP or Fast Pass holders).
# Guests with higher priority board the ride before others.
# add_guest(guest_name, priority) adds a guest with their priority (lower number indicates higher priority).
# start_ride(capacity) simulates the ride, displaying guest names as they board based on priority.
class VIPRide:
   # Constructor initializes the queue with an empty list.
   def __init__(self):
       self.rideQueue = LinkedPriorityQueue() # VIPRide uses a priority queue to maintain the priority of guests.


   # Enqueue the guests to the roller coaster ride based on the priority of the guests.
   def add_guest(self, guest, priority):
       self.rideQueue.priority_queue_enqueue(guest, priority)


   # Dequeue the guests from the priority queue.
   def remove_guests(self):
       if (self.rideQueue.priority_queue_isQueueEmpty()):
           return None
       else:
           return self.rideQueue.priority_queue_dequeue()

   # Checks if the priority queue is empty.
   def isEmpty(self):
       return self.rideQueue.priority_queue_isQueueEmpty()


# Test method for elevator ride takes the guest list and capacity.
# Pushes the guests and pops the guests in order.
def elevator_ride_test(guest_list, capacity):
  eRide = ElevatorRide()
  print()
  print("************************************************")
  print("*               Elevator Ride Test              *")
  print("************************************************")
  eRide.availableSpots = capacity
  print("Now boarding guests: ", end=' ')
  for index in range(len(guest_list) - 1):
      if (eRide.availableSpots > 0 and index <= len(guest_list) - 1):
          print(guest_list[index], end=' ')
          eRide.board_guest(guest_list[index])
      else:
          # Empty the ride.
          print()
          print("Guests exiting: ", end=' ')
          eRide.start_ride(capacity)
          print()
          print("Now boarding guests: ", guest_list[index], end=' ')
          eRide.board_guest(guest_list[index])
  # Finally, empty the ride of all the guests.
  print()
  print("Guests exiting: ", end=' ')
  eRide.start_ride(capacity)


# Roller coaster ride enqueues and dequeues the guests based on the capacity of the roller coaster ride.
def roller_coaster_ride_test(guest_list, capacity):
  cRide = RollerCoasterRide()
  cRide.availableSpots = capacity
  print()
  print("*******************************************************")
  print("*               Roller Coaster Ride Test              *")
  print("*******************************************************")
  print("Now boarding guests: ", end=' ')
  for index in range(len(guest_list) - 1):
      if (cRide.availableSpots > 0 and index <= len(guest_list) - 1):
          print(guest_list[index], end=' ')
          cRide.join_queue(guest_list[index])
      else:
          # Empty the ride.
          print()
          print("Guests exiting: ", end=' ')
          cRide.start_ride()
          print("Now boarding guests: ", guest_list[index], end=' ')
          cRide.join_queue(guest_list[index])
  # Finally, empty the ride of all the guests.
  print()
  print("Guests exiting: ", end=' ')
  cRide.start_ride()


# Creates a priority list of guests and uses the elevator ride and roller coaster ride objects to enqueue
# and dequeue the guests.
def priority_ride_test(guest_list):
   listOfGuests = []
   ride_name = ["Elevator Ride", "Roller Coaster Ride"]
   # create ride objects
   cRide = RollerCoasterRide()
   eRide = ElevatorRide()
   # create priority queue for the rides
   priority_guest_queue = VIPRide()
   # create a priority guest list for VIPRide.
   # Use guest name list and guest priority list to separate the names and priorities from the tuple guest_list.
   guest_names = [guests[0] for guests in guest_list]
   guest_priorities = [guests[1] for guests in guest_list]
   for index in range(len(guest_names)):
       name = guest_names[index]
       prio = guest_priorities[index]
       priority_guest_queue.add_guest(name, prio)
   # priority_guest_queue.guest_dump()
   while not priority_guest_queue.isEmpty():
       name = priority_guest_queue.remove_guests()
       # Create a list of guest names based on the priority.
       listOfGuests.append(name)
   # Ask the user to choose a ride
   ride_type = int(input("Please enter 1. Elevator Ride or 2. Roller Coaster Ride: "))
   print("Please enter the capacity of ",  ride_name[ride_type - 1], end=' ')
   capacity = int(input())
   cRide.availableSpots = capacity

   print("*******************************************************")
   print("*               VIP Ride Test                         *")
   print("*******************************************************")
   if ride_type == 1:
       elevator_ride_test(listOfGuests, capacity)
   else:
       roller_coaster_ride_test(listOfGuests, capacity)



def main():
   # guests with priority tuple to use for priority queue
   guest_tuple = [("Abe", LOW_PRIORITY), ("Bob", LOW_PRIORITY), ("Cory", LOW_PRIORITY), ("Dave", HIGH_PRIORITY),
                  ("Emma", LOW_PRIORITY), ("Frank", MEDIUM_PRIORITY), ("Ganesh", LOW_PRIORITY),
                  ("Harry", HIGH_PRIORITY), ("Izzac", HIGH_PRIORITY), ("Jack", MEDIUM_PRIORITY),
                  ("Katy", LOW_PRIORITY), ("Larry", MEDIUM_PRIORITY), ("Mom", HIGH_PRIORITY),
                  ("Nanna", HIGH_PRIORITY)]
   # Guest list for non-priority test.
   guest_list = ["Abe", "Bob", "Cory", "Dave", "Emma", "Frank", "Ganesh", "Harry", "Izzac", "Jack", "Katy", "Larry", "Mom", "Nanna"]
   capacity = int(input("Please enter the capacity of elevator rides:"))
   # Non priority elevator ride test
   elevator_ride_test(guest_list, capacity)
   ride_on_rollercoaster = str(input("Do you want to ride on roller coaster(y/n): "))
   # Test the non-priority roller coaster test.
   if ((ride_on_rollercoaster == 'y' or ride_on_rollercoaster == 'Y') or
       (ride_on_rollercoaster == 'yes' or ride_on_rollercoaster == 'Yes')):
       roller_coaster_ride_test(guest_list, capacity)
   # Create the priority guest list from the guest tuples and test the elevator ride and roller coaster ride test.
   priority_ride_test(guest_tuple)

if __name__ == "__main__":
  main()
# Result:
# C:\AdvancedPython\ADVANCEDPYTHON-2025\.venv\Scripts\python.exe C:\AdvancedPython\ADVANCEDPYTHON-2025\Week7Lab-V2.py
# Please enter the capacity of elevator rides:4
#
# ************************************************
# *               Elevator Ride Test              *
# ************************************************
# Now boarding guests:  Abe Bob Cory Dave
# Guests exiting:  Dave Cory Bob Abe
#
# Now boarding guests:  Emma Frank Ganesh Harry
# Guests exiting:  Harry Ganesh Frank Emma
#
# Now boarding guests:  Izzac Jack Katy Larry
# Guests exiting:  Larry Katy Jack Izzac
#
# Now boarding guests:  Mom
# Guests exiting:  Mom
# Do you want to ride on roller coaster(y/n): y
#
# *******************************************************
# *               Roller Coaster Ride Test              *
# *******************************************************
# Now boarding guests:  Abe Bob Cory Dave
# Guests exiting:  Abe Bob Cory Dave
# Now boarding guests:  Emma Frank Ganesh Harry
# Guests exiting:  Emma Frank Ganesh Harry
# Now boarding guests:  Izzac Jack Katy Larry
# Guests exiting:  Izzac Jack Katy Larry
# Now boarding guests:  Mom
# Guests exiting:  Mom
# Please enter 1. Elevator Ride or 2. Roller Coaster Ride: 2
# Please enter the capacity of  Roller Coaster Ride 4
# *******************************************************
# *               VIP Ride Test                         *
# *******************************************************
#
# *******************************************************
# *               Roller Coaster Ride Test              *
# *******************************************************
# Now boarding guests:  Dave Harry Izzac Mom
# Guests exiting:  Dave Harry Izzac Mom
# Now boarding guests:  Nanna Frank Jack Larry
# Guests exiting:  Nanna Frank Jack Larry
# Now boarding guests:  Abe Bob Cory Emma
# Guests exiting:  Abe Bob Cory Emma
# Now boarding guests:  Ganesh
# Guests exiting:  Ganesh
#
# Process finished with exit code 0