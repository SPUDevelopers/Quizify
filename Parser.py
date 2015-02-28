class Parser:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        is_in_list = False
        if word is not None:
            word = word.strip(',.()/\\:;*&^$#@!`~&[]{}|?<>+=-')
            for x in self.words:
                if x.lower() == word.lower() :
                    x.frequency += 1
                    is_in_list = True

            if is_in_list == False :
                self.words.append(Word(word.lower(), 1))
            return True
        else :
            return False

    def clear(self):
        self.words = []

    def get_list(self):
        return self.words
