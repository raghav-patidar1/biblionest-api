from rest_framework.generics import ListAPIView

from .models import LibraryBranch
from .serializers import LibraryBranchListSerializer


class LibraryBranchListAPIView(ListAPIView):
    """
    API view to retrieve a read-only list of all library branches. Including:
    
    - Branch name
    - Total number of books in the branch
    - Nested list of books (title, author, genre, availability)
    - Nested list of members registered at the branch
    - For each member, a list of borrowed books and issue dates
    """

    queryset = LibraryBranch.objects.prefetch_related(
        'books',
        'members'
    )
    serializer_class = LibraryBranchListSerializer
    