from flaskr.datasources.third_party import ThirdPartyRepository
from flaskr.datasources.database import DBRepository


# make this singleton
class BookRepository:
    def __init__(self, db: DBRepository, ext_source: ThirdPartyRepository):
        self.db = db
        self.ext_source = ext_source

    def _get_book_from_data_sources(self, book_id):
        book_details = self.db.get_book(book_id)
        if book_details is None:
            book_details = self.ext_source.get_book(book_id)
            self.db.entry_book(book_id, book_details['text'], book_details['metadata'])
        return book_details

    def _get_book_and_update_activity(self, book_id):
        book_details = self._get_book_from_data_sources(book_id)
        self.db.entry_activity(book_id)
        return book_details

    def get_book(self, book_id):
        return self._get_book_and_update_activity(book_id)

    # TODO: separate activity functionality from book repository
    def get_recent_activity(self):
        return self.db.get_activity()