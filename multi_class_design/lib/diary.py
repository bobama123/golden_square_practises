class Diary:
    # User-facing properties:
    #   diary_entry: list of instances of DiaryEntry

    def __init__(self):
        self.diary_entry_list = []

    def add(self, entry):
        self.diary_entry_list.append(entry)

    def all(self):
        return self.diary_entry_list
    
    def readable_diary_entry(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        for entry in self.diary_entry_list:
            if entry.count_words() <= words_user_can_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        return most_readable