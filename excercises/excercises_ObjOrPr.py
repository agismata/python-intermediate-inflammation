import numpy as np
from datetime import datetime

class Paper:
    def __init__(self, title, date=None):
        if date is None:
            date = datetime.now().date()

        self.title = title
        self.date = date

    def __str__(self):
        return self.title


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Academic(Person):
    def __init__(self, name):
        super().__init__(name)
        self.papers = []

    def write_paper(self, title, date=None):
        new_paper = Paper(title, date)

        self.papers.append(new_paper)
        return new_paper

    def __str__(self):
        return self.name

    def __getitem__(self, index):
        return self.papers[index]

    def __len__(self):
        return len(self.papers)

    @property
    def last_paper(self):
        return self.papers[-1]


alice = Academic('Alice')
print(alice)

paper = alice.write_paper('A paper')
print(paper)

bob = Person('Bob')
print(bob)

paper = bob.write_paper('A different paper')
print(paper)

# =====================================================


class Book:
    """Model representing an academic."""
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author


book = Book('A Book', 'Me')

print(book)
