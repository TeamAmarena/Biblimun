from datetime import datetime

from domain.serializers import AuthorSerializer


def test_author_birth_date_should_not_be_set_in_the_past():
    assert (
        AuthorSerializer(
            data={
                "first_name": "John",
                "last_name": "Doe",
                "birth_date": datetime.now(),
            }
        ).is_valid()
        is False
    )
