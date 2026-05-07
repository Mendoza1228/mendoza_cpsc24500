from word import Word

class WordCollection:
    def __init__(self):
        self._words = []

    @classmethod
    def from_file (cls, filepath):
        collection = cls()
        
        try:
            with open(filepath, 'r') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        try:
                            collection.words.append(Word(parts[0], parts[1]))
                        except ValueError:
                            continue #kip lines with invalid word types
        except FileNotFoundError:
            print(f"Error: File {filepath} not found.")     
        return collection
    

    def add(self, word):
        if not isinstance(word, Word):
            raise TypeError("Only Word instances can be added to the collection.")
        self.words.append(word)

    def filter_by_pos(self, part_of_speech):
        new_col = WordCollection()
        for word in self._words:
            if word.part_of_speech == part_of_speech:
                new_col.add(word)
        return new_col
    def __len__ (self):
        return len(self._words)
    
    def __getitem__ (self, index):
        return self._words[index]
    
    def __contains__ (self,time):
        return time in self._words
    
    def __iter__(self):
        return iter(self._words)
    
    def __repr__(self):
        return f"WordCollection ({len(self._words)} words)"
    
           
               

                                

    