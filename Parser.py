import Word

class Parser:

    def __init__(self):
        self.words = []

    def add_word(self, word, definition):
        is_in_list = False
        if word is not None:
            word = word.strip(',.()/\\:;*&^$#@!`~&[]{}|?<>+=-')
            for x in self.words:
                if x.name == word.lower():
                    x.frequency += 1
                    is_in_list = True

            if is_in_list == False:
                self.words.append(Word.Word(word, 1, definition))
            return True
        else:
            return False

    def clear(self):
        self.words = []

    def get_list(self):
        return self.words
