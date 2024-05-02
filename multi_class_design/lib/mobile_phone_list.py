import re

class MobilePhoneList:
    def __init__(self, diary):
        self.numbers_list = []
        self.diary = diary

    def extract_numbers(self):
        for entry in self.diary.all():
            number = re.findall(r'\b0[0-9]{10}\b', entry.contents)
            print(entry.contents)
            print(number)
            self.numbers_list += number

    def list_numbers(self):
        return self.numbers_list