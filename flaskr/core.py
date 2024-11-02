from flaskr.datasources import BookRepository
from flaskr.datasources.third_party import GutenbergRepository
from flaskr.datasources.database import SQLiteRepository


def get_gutenberg_repository():
    return BookRepository(SQLiteRepository(), GutenbergRepository())
