from lib.task import Task

def test_for_task_seen():
    task1 = Task("I need to eat")
    assert task1.task == "I need to eat"


def test_for_incomplete_task():
    task1 = Task("I need to eat")
    assert task1.complete == False


def test_for_completed_task():
    task1 = Task("I need to eat")
    task1.mark_complete()
    assert task1.complete == True