from datetime import date

from django.core.management.base import BaseCommand

from api.models import (
    Author, Genre, Book, LibraryBranch, LibraryMember, 
    IssuedBook
)


class Command(BaseCommand):
    help_text = "Populate data for api models."

    def handle(self, *args, **options):
        
        # Create genres
        fantasy = Genre.objects.create(genre_name="Fantasy")
        history = Genre.objects.create(genre_name="History")
        scifi = Genre.objects.create(genre_name="Science Fiction")
        nonfiction = Genre.objects.create(genre_name="Non-Fiction")
        drama = Genre.objects.create(genre_name="Political Drama")
        
        # Create authors
        jk_rowling = Author.objects.create(author_name='J.K. Rowling')
        martin = Author.objects.create(author_name='George R.R. Martin')
        yuval = Author.objects.create(author_name='Yuval Noah Harari')
        sumita = Author.objects.create(author_name='Sumita Arora')
        chetan = Author.objects.create(author_name='Chetan Bhagat')


        # Create Books
        b1 = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            author=jk_rowling,
            genre=fantasy,
            copies_in_stock=10,
            available_copies=5
        )
        b2 = Book.objects.create(
            title="A Game of Thrones",
            author=martin,
            genre=drama,
            copies_in_stock=11,
            available_copies=8
        )
        b3 = Book.objects.create(
            title="Sapiens: A Brief History of Humankind",
            author=yuval,
            genre=history,
            copies_in_stock=7,
            available_copies=0
        )

        # Create library branch
        branch1 = LibraryBranch.objects.create(branch_name="Downtown Library")
        branch2 = LibraryBranch.objects.create(branch_name="Vidyadan Library")
        branch1.books.set([b2, b1])
        branch2.books.set([b3])

        # Create library members
        member1 = LibraryMember.objects.create(name="Alice")
        member2 = LibraryMember.objects.create(name="Bob")
        member3 = LibraryMember.objects.create(name="Charlie")

        # Assign members to branch
        member1.registered_branch.set([branch1])
        member2.registered_branch.set([branch1, branch2])
        member3.registered_branch.set([branch2])

        # Assign books to member
        IssuedBook.objects.create(member=member1, book=b1, issued_on=date(2025, 6, 25))
        IssuedBook.objects.create(member=member2, book=b2, issued_on=date(2025, 6, 28))
        IssuedBook.objects.create(member=member1, book=b3, issued_on=date(2025, 7, 1))
        IssuedBook.objects.create(member=member3, book=b2, issued_on=date(2025, 6, 29)) 