#Solution Outline
#1. Problem A: KWIC Using Abstract Data Types (ADT)
#In the ADT approach, we’ll identify and encapsulate each concept as a class, such as for KWICSystem, ShiftedLine, and LineStorage.

# KWIC using Abstract Data Types in Python

class LineStorage:
    def __init__(self):
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)

    def get_lines(self):
        return self.lines


class KWICSystem:
    def __init__(self, line_storage):
        self.line_storage = line_storage
        self.shifted_lines = []

    def generate_shifts(self):
        for line in self.line_storage.get_lines():
            words = line.split()
            for i in range(len(words)):
                shifted_line = ' '.join(words[i:] + words[:i])
                self.shifted_lines.append(shifted_line)

    def get_shifted_lines(self):
        return self.shifted_lines


# Sample usage
line_storage = LineStorage()
line_storage.add_line("Design patterns are useful for problem-solving")
line_storage.add_line("Programming paradigms vary across languages")

kwic_system = KWICSystem(line_storage)
kwic_system.generate_shifts()

for shifted in kwic_system.get_shifted_lines():
    print(shifted)
