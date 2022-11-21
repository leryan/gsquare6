# EXAMPLE

class Reminder:
    # User-facing properties:
    #   name: string

Story

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

*We want to look through multiple reminders and see them in a list

My Design (v)
class TaskTracker():
    def add (self, list):
        # Parameters:
        #   Task : string representing a tasks
        pass

    def list_incomplete(self):
        # Returns:
        #   A list of incomplete tasks
        pass

    def mark_complete(self, index):
        # Parameters:
        #   index: on integer representing the task to complete
        # Side-effect:
        #   Removes the task at index from list of tasks
        pass

# EXAMPLE

"""
Initially there are no tasks 
"""
tracker = TaskTracker()
tracker.list_incomplete() # => []

"""
When we add a task
It is reflected in the list of tasks
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.list_incomplete() # => ["Walk the dog"]

"""
When we add multiple task
They are all reflected in the list of tasks
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.add("Walk the cat")
tracker.add("Walk the frog")
tracker.list_incomplete() # => ["Walk the dog", "Walk the cat", "Walk the frog"]

"""
When we add multiple task
Mark one as complete
Disappears from list
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.add("Walk the cat")
tracker.add("Walk the frog")
tracker.mark_complete(1)
tracker.list_incomplete() # => ["Walk the dog", "Walk the frog"]

"""
If we mark a task complete that does not exist (too low)
It raises error
"""

tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.mark_complete(-1) #raises error "No such task to mark complete"
tracker.list_incomplete() # => ["Walk the dog"]

"""
If we mark a task complete that does not exist (too high)
It raises error
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.mark_complete(2) #raises error "No such task to mark complete"
tracker.list_incomplete() # => ["Walk the dog"]