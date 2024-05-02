from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.task import Task
from lib.task_list import TaskList
from lib.mobile_phone_list import MobilePhoneList

def test_for_two_entries_added_to_diary():
    diary = Diary()
    diary_entry1 = DiaryEntry("Monday", "I ate food.")
    diary_entry2 = DiaryEntry("Tuesday", "I slept.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.all() == [diary_entry1, diary_entry2]

def test_for_best_entry_can_be_read_in_2_minutes_with_2_wpm():
    diary = Diary()
    diary_entry1 = DiaryEntry("Monday", "I ate food.")
    diary_entry2 = DiaryEntry("Tuesday", "I slept.")
    diary_entry3 = DiaryEntry("Wednesda", "I did not sleep or eat food.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    result = diary.readable_diary_entry(2, 2) 
    assert result == diary_entry1

def test_for_two_tasks_in_incomplete_list():
    task_list = TaskList()
    task1 = Task("I need to eat")
    task2 = Task("Omg i need to sleep")
    task_list.add(task1)
    task_list.add(task2)
    result = task_list.list_incomplete()
    assert result == [task1, task2]



def test_for_2_complete_tasks_in_complete_list():
    task_list = TaskList()
    task1 = Task("I need to eat")
    task2 = Task("Omg i need to sleep")
    task3 = Task("Do some work")
    task_list.add(task1)
    task_list.add(task2)
    task_list.add(task3)
    task1.mark_complete()
    task3.mark_complete()
    result = task_list.list_complete() 
    assert result == [task1, task3]



def test_for_all_numbers_extracted_from_diary():
    diary = Diary()
    diary_entry1 = DiaryEntry("Monday", "I ate food. 07123456789")
    diary_entry2 = DiaryEntry("Tuesday", "I slept. 07123456788")
    diary_entry3 = DiaryEntry("Wednesda", "I did not sleep or eat food.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    mobile_phone = MobilePhoneList(diary)
    mobile_phone.extract_numbers()
    assert mobile_phone.list_numbers() == ["07123456789", "07123456788"]