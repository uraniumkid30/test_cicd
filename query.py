from datetime import datetime
import random
from apps.bookstore.models import Book, Author

authors_data = [
    {
        "name": "Jane Austen",
        "email": "janeausten@example.com",
        "date_of_birth": datetime(year=1990, month=1, day=1).date(),
        "gender": "female",
        "number_of_awards": 10,
    },
    {
        "name": "Charles Dickens",
        "email": "charlesdickens@example.com",
        "date_of_birth": datetime(year=1980, month=4, day=1).date(),
        "gender": "male",
        "number_of_awards": 5,
    },
    {
        "name": "Mark Twaine",
        "email": "marktwaine@example.com",
        "date_of_birth": datetime(year=1980, month=4, day=1).date(),
        "gender": "male",
        "number_of_awards": 25,
    },
    {
        "name": "Virginia Wolf",
        "email": "vwolf@example.com",
        "date_of_birth": datetime(year=1994, month=11, day=22).date(),
        "gender": "female",
        "number_of_awards": 13,
    },
]


Author.objects.all().delete()
Book.objects.all().delete()
authors = []

for data in authors_data:
    authors.append(Author.objects.create(**data))

books_data = [
    {
        "title": "Pride and Prejudice",
        "description": "fun adventure",
        "author": authors[0],
        "category": "Art",
    },
    {
        "title": "Great Expectations",
        "description": "deep read",
        "author": authors[0],
        "category": "General",
    },
    {
        "title": "Adventures of Hulkland",
        "description": "adventure with some thrill",
        "author": authors[1],
        "category": "Science",
    },
    {
        "title": "Jayne Eyre",
        "description": "fantastic read",
        "author": authors[1],
        "category": "General",
    },
    {
        "title": "impulse Jet",
        "description": "wonder read",
        "author": authors[2],
        "category": "Science",
    },
    {
        "title": "Apologies",
        "description": "mind blowing",
        "author": authors[3],
        "category": "General",
    },
    {
        "title": "Vendetta",
        "description": "fantastic read",
        "author": authors[0],
        "category": "Art",
    },
    {
        "title": "No one is an Island",
        "description": "great read",
        "author": authors[2],
        "category": "General",
    }
]
for item in books_data:
    chosen_author = random.choice(authors)
    Book.objects.create(**item)

print("Done")