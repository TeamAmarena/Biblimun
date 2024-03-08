from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Author, User, Book
from .serializers import UserSerializer, AuthorSerializer, BookSerializer


# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class BookViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
