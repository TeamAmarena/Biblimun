from ninja import NinjaAPI
from ninja.orm import create_schema

from domain.models import Book

api = NinjaAPI()


class BookSchema(create_schema(Book)):
    pass

@api.get("/books/", response=list[BookSchema])
def list_order(
    request,
):
    return Book.objects.all()
