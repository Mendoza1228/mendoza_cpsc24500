from word import Word

class WordCollection:
    def __init__(self):
        self._words = []

    @classmethod
    def from_file(cls, filepath):
        collection = cls()
        try:
            with open(filepath, 'r') as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) == 2:
                        try:
                            collection.add(Word(parts[0], parts[1]))
                        except ValueError:
                            continue
        except FileNotFoundError:
            print(f"Error: {filepath} not found.")
        return collection

    def add(self, word):
        if not isinstance(word, Word):
            raise TypeError("Only Word objects can be added.")
        self._words.append(word)

    def filter_by_pos(self, part_of_speech):
        new_col = WordCollection()
        for w in self._words:
            if w.part_of_speech == part_of_speech:
                new_col.add(w)
        return new_col

    def sorted_words(self, reverse=False):
        new_col = WordCollection()
        # Uses Word.__lt__ automatically
        sorted_list = sorted(self._words, reverse=reverse)
        for w in sorted_list:
            new_col.add(w)
        return new_col

    def __len__(self):
        return len(self._words)

    def __getitem__(self, index):
        return self._words[index]

    def __contains__(self, item):
        return item in self._words

    def __iter__(self):
        return iter(self._words)

    def __repr__(self):
        return f"WordCollection({len(self._words)} words)"