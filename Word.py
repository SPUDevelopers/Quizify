class Word :
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency

    def lower(self):
        return self.name.lower()
