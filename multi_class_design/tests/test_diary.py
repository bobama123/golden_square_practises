from lib.diary import Diary


def test_for_empty_Diary():
    diary = Diary()
    assert diary.all() == []