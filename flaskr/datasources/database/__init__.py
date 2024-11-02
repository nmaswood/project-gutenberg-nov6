from flaskr.datasources.database.sqlite3_function import entry_book, get_book, entry_activity, get_recent_activity
from abc import ABC, abstractmethod


class DBRepository(ABC):
    @staticmethod
    @abstractmethod
    def entry_book(book_id, text, metadata):
        ...

    @staticmethod
    @abstractmethod
    def get_book(book_id):
        ...

    @staticmethod
    @abstractmethod
    def entry_activity(book_id):
        ...

    @staticmethod
    @abstractmethod
    def get_activity():
        ...


class SQLiteRepository(DBRepository):
    @staticmethod
    def entry_book(book_id, text, metadata):
        return entry_book(book_id, text, metadata['author'], metadata['title'], metadata['language'], metadata['date_published'])

    @staticmethod
    def get_book(book_id):
        return get_book(book_id)

    @staticmethod
    def entry_activity(book_id):
        return entry_activity(book_id)

    @staticmethod
    def get_activity():
        return get_recent_activity()


