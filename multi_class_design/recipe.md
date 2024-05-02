# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a User
So that i can record my experiences
I want to keep a regular diary

As a User
So that i can reflect on my experiences
I want to read my past diary entries

As a User
So that i can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time i have and my reading speed

As a User
So that i can keep track of my tasks
I want to keep a todo list along with my diary

As a User
So that i can keep track of my contacts
I want to see a list of all the mobile phone numbers in all my diary entries

# Phone number starts with zero and is 11 digits long


Nouns:
Diary
Diary Entries
Experiences
Time
Reading Speed
Tasks
Todo List
Phone Numbers
List of Phone Numbers

Verbs:
Record
Keep
Reflect
Read
Select
See a list


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ MusicPlayer                │
│                            │
│ - tracks                   │
│ - add(track)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Track(title, artist)    │
│                         │
│ - title                 │
│ - artist                │
│ - format()              │
│   => "TITLE by ARTIST"  │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Diary:
    # User-facing properties:
    #   diary_entry: list of instances of DiaryEntry

    def __init__(self):
        pass # No code here yet

    def add(self, diary_entry):
        # Parameters:
        #   diary_entry: an instance of DiaryEntry
        # Side-effects:
        #   Adds the diary_entry to the diary_entry property of the self object
        pass # No code here yet

    def all(self):
        # Returns:
        #   A list of all diary entries
        pass # No code here yet

    def readable_diary_entry(self, wpm, minutes):
        # Parameters:
        #   wpm: words per minute
        #   minutes: minutes given to read
        # Returns:
        #   A list of all diary entries depending on reading speed.
        pass # No code here yet

class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: a string
        #   contents: a string
        # Side-effects:
        #   Sets the diary_entry properties
        pass # No code here yet

class Tasklist:
    # User-facing properties:
    #   task: list of instances of Task

    def __init__(self):
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: an instance of Task
        # Side-effects:
        #   Adds the task to the task property of the self object
        pass # No code here yet

    def list_incomplete(self):
        # Returns:
        #   A list of all incomplete tasks
        pass # No code here yet

    def complete(self):
        # Returns:
        #   A list of all complete tasks
        pass # No code here yet

class Task:
    def __init__(self, task):
        # Parameters:
        #   task: a string
        # Side-effects:
        #   Sets the task properties
        pass # No code here yet

    def mark_complete(self, task):
        # Parameters:
        #   task: an instance of Task
        # Side-effects:
        #   Task is now complete
        pass # No code here yet


class Mobile_Phone_list:

    def __init__(self):
        pass # No code here yet

    def extract_numbers(self):
        # Side-effects:
        #   Extracts numbers from diary and adds the number to a list
        pass # No code here yet

    def list_numbers(self):
        #Returns
        #   list of all numbers in the diary
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a Diary
When we add two diary entries
We see those diary entries reflected in the Diary
"""
diary = Diary()
diary_entry1 = DiaryEntry("Monday", "I ate food.")
diary_entry2 = DiaryEntry("Tuesday", "I slept.")
diary.add(diary_entry1)
diary.add(diary_entry2)
diary.all() # => [diary_entry1, diary_entry2]

"""
Given a Diary
We add three diary entries
We see the best diary entry that can be read in the time with reading speed
"""
diary = Diary()
diary_entry1 = DiaryEntry("Monday", "I ate food.")
diary_entry2 = DiaryEntry("Tuesday", "I slept.")
diary_entry3 = DiaryEntry("Wednesda", "I did not sleep or eat food.")
diary.add(diary_entry1)
diary.add(diary_entry2)
diary.add(diary_entry3)
diary.readable_diary_entry(2, 2) # => [diary_entry1]

"""
Given a TaskList
When we add two tasks
We see those tasks reflected in the incomplete list
"""
task_list = TaskList()
task1 = TaskList("I need to eat")
task2 = TaskList("Omg i need to sleep")
task_list.add(task1)
task_list.add(task2)
task_list.list_incomplete() # => [task1, task2]

"""
Given a TaskList
When we add three tasks
And then mark 2 tasks as complete
We see the tasks reflected in the complete list
"""
task_list = TaskList()
task1 = TaskList("I need to eat")
task2 = TaskList("Omg i need to sleep")
task3 = TaskList("Do some work")
task_list.add(task1)
task_list.add(task2)
task1.mark_complete()
task3.mark_complete()
task_list.list_complete() # => [task1, task3]

"""
Given a Diary
We add three diary entries
We see a list of numbers in all diary entries
"""
diary = Diary()
diary_entry1 = Diary("Monday: I ate food. 07123456789")
diary_entry2 = Diary("Tuesday: I slept. 07123456788")
diary_entry3 = DiaryEntry("Wednesda", "I did not sleep or eat food.")
diary.add(diary_entry1)
diary.add(diary_entry2)
diary.add(diary_entry3)
diary.extracts_numbers()
diary.list_numbers() # => ["07123456789", "07123456788"]



```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a diary entry
We see the diary entry's title and contents
"""
diary_entry = DiaryEntry("Monday", "I ate food.")
diary_entry.title # => "Monday"
diary_entry.contents # => "I ate food."


"""
Given an empty diary
We see the empty list
"""
diary = Diary()
diary.all() # => []

"""
Given a task
We see the task
"""
task1 = Task("I need to eat")
task1.task # => "I need to eat"

"""
Given a task
We see if task is incomplete
"""
task1 = Task("I need to eat")
task1.complete # => False

"""
Given a task
We see if task is complete
"""
task1 = Task("I need to eat")
task1.mark_complete()
task1.complete # => True











```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
