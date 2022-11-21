import pytest
from lib.task_tracker import TaskTracker

"""
Initially there are no tasks 
"""
def test_initially_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []

"""
When we add a task
It is reflected in the list of tasks
"""
def test_add_test_and_is_reflected():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    assert tracker.list_incomplete() == ["Walk the dog"]

"""
When we add multiple task
They are all reflected in the list of tasks
"""
def test_add_multiple_tasks():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the frog")
    assert tracker.list_incomplete() == [
        "Walk the dog", "Walk the cat", "Walk the frog"]

"""
When we add multiple task
Mark one as complete
Disappears from list
"""
def test_multiple_tasks_and_one_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the frog")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() == ["Walk the dog", "Walk the frog"]

"""
If we mark a task complete that does not exist (too low)
It raises error
"""
def test_mark_test_complete_doesnt_exist_too_low():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(-1) 
    assert str(err.value) == "No such task to mark complete" #raises error "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk the dog"]

"""
If we mark a task complete that does not exist (too high)
It raises error
"""
def test_mark_test_complete_doesnt_exist_too_high():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(1) 
    assert str(err.value) == "No such task to mark complete" #raises error "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk the dog"]