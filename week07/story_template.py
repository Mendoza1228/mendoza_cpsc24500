
import random

from word_collection import WordCollection

class StoryTemplate:
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern

    @property
    def name(self):
        return self._name
    
    @property
    def pattern(self):
        return self._pattern
    
    def generate(self, word_collection):
        sentence = []
        for token in self.pattern:
            if token.startswith("{") and token.endswith("}"):
                pos = token [1:-1] #remove the curly braces
                filtered = word_collection.filter_by_pos(pos)
                if len(filtered) > 0:
                    sentence.append(random.choice(filtered._words).text)
                else:
                    sentence.append(f"<no {pos} available>")
            else:
                sentence.append(token)


        #join the sentence list into a single string with spaces
        full_sentence = " ".join(sentence).strip()
        return full_sentence.capitalize() + "." #capitalize the first letter and add a period at the end


TEMPLATES = [
    StoryTemplate("Adventure", ["The", "{adjective}", "{noun}", "{verb}", "{preposition}", "the", "{adjective}", "{noun}"]),
        StoryTemplate("Mystery", ["In the", "{adjective}", "{noun}", "was", "{verb}", "by the", "{adjective}", "{noun}"]),
        StoryTemplate("Comedy", ["Why did the", "{adjective}", "{noun}", "{verb}", "the", "{adjective}", "{noun}?"]),
    ]