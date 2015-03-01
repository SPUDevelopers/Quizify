class Word:
    def __init__(self, name, frequency, definition):
        self.name = name.lower()
        self.frequency = frequency
        self.definition = definition