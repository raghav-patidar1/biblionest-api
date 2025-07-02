from rest_framework import serializers

from .models import Book, LibraryBranch, LibraryMember, IssuedBook


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    
    Serializes:
    - title
    - author's name (flattened via source)
    - genre's name (flattened via source)
    - is_available (computed via @property)
    """

    author = serializers.CharField(source='author.author_name')
    genre = serializers.CharField(source='genre.genre_name')

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'is_available')


class IssuedBookSerializer(serializers.ModelSerializer):
    """
    Serializer for IssuedBook model.
    
    Provides:
    - title of the issued book
    - issued_on date
    """

    title = serializers.CharField(source='book.title')
    
    class Meta:
        model = IssuedBook
        fields = ('title', 'issued_on')


class MemberSerializer(serializers.ModelSerializer):
    """
    Serializer for LibraryMember model.
    
    Includes:
    - member name
    - borrowed_books: list of books issued via the related IssuedBook model
    """

    borrowed_books = IssuedBookSerializer(source='issued_books', many=True)

    class Meta:
        model = LibraryMember
        fields = ('name', 'borrowed_books')


class LibraryBranchListSerializer(serializers.ModelSerializer):
    """
    Serializer for LibraryBranch model.
    
    Provides:
    - branch name
    - total number of books (via SerializerMethodField)
    - serialized list of books in the branch
    - serialized list of members registered at the branch
    """

    books = BookSerializer(many=True)
    members = MemberSerializer(many=True)
    total_books = serializers.SerializerMethodField()

    def get_total_books(self, obj):
        """Returns the count of books available in the branch."""
        return obj.books.count()
         
    class Meta:
        model = LibraryBranch
        fields = ('branch_name', 'total_books', 'books', 'members')
