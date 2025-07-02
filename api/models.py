from uuid import uuid4

from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=64)

    def __str__(self):
        return self.author_name
    

class Genre(models.Model):
    genre_name = models.CharField(max_length=50)

    def __str__(self):
        return self.genre_name
    

class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='books'
    )
    copies_in_stock = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)

    @property
    def is_available(self):
        return self.available_copies > 0
    
    def __str__(self):
        return self.title
    

class LibraryBranch(models.Model):
    branch_name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name='branches')

    def __str__(self):
        return self.branch_name
    

class LibraryMember(models.Model):
    name = models.CharField(50)
    registered_branch = models.ManyToManyField(
        LibraryBranch,
        related_name='members'
    )
    books_issued = models.ManyToManyField(
        Book,
        through='IssuedBook',
        related_name='issued_to_members'
    )

    def __str__(self):
        return self.name
    

class IssuedBook(models.Model):
    member = models.ForeignKey(
        LibraryMember,
        on_delete=models.CASCADE,
        related_name='books'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='members'
    )
    issued_on = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.member.name} --> {self.book.title}"