import random
from word_collection import WordCollection

class StoryTemplate:
    def __init__(self, name, pattern):
        self._name = name
        self._pattern = pattern

    @property
    def name(self):
        return self._name

    @property
    def pattern(self):
        return self._pattern

    def generate(self, word_collection):
        sentence_parts = []
        for token in self._pattern:
            if token.startswith("{") and token.endswith("}"):
                pos = token.strip("{}").strip()
                choices = word_collection.filter_by_pos(pos)
                if len(choices) > 0:
                    sentence_parts.append(str(random.choice(choices)))
                else:
                    sentence_parts.append(token) # Keep tag if no words found
            else:
                sentence_parts.append(token)
        
        sentence = " ".join(sentence_parts).strip()
        # Clean up spaces before punctuation if any, and capitalize
        sentence = sentence.replace(" .", ".").replace(" ,", ",")
        return sentence.capitalize() + "."

TEMPLATES = [
    StoryTemplate("Adventure", ["The", "{adj}", "{n}", "{v}", "{adv}", "{prep}", "the", "{adj}", "{n}"]),
    StoryTemplate("Mystery", ["A", "{adj}", "{n}", "{adv}", "{v}", "while", "the", "{n}", "{v}", "{prep}", "the", "{n}"]),
    StoryTemplate("Simple", ["The", "{adj}", "{n}", "{v}", "{adv}"])
]