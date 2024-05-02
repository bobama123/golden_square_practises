from lib.diary_entry import DiaryEntry

def test_for_diary_entry_title_and_contents():
    diary_entry = DiaryEntry("Monday", "I ate food.")
    assert diary_entry.title == "Monday"
    assert diary_entry.contents == "I ate food."