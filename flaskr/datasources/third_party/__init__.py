from abc import ABC, abstractmethod
from flaskr.datasources.third_party.gutenberg import get_book_text, get_book_metadata


class ThirdPartyRepository(ABC):
    @staticmethod
    @abstractmethod
    def get_book(book_id):
        ...


class GutenbergRepository(ThirdPartyRepository):
    @staticmethod
    def get_book(book_id):
        return {'text': get_book_text(book_id), 'metadata': get_book_metadata(book_id)}
