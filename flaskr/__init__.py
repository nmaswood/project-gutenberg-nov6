from flask import Flask
from flaskr.datamodels import create_table_if_not_exists
from flaskr.core import get_gutenberg_repository
from flaskr.text_analysis import get_plot_summary_analysis
import json
from flask_cors import CORS
from flaskr.custom_exceptions import BookNotFound

app = Flask(__name__)
CORS(app)
with app.app_context():
    create_table_if_not_exists()


@app.route('/book/<int:book_id>', methods=['GET'])
def book(book_id):
    try:
        repository = get_gutenberg_repository()
        return json.dumps(repository.get_book(book_id))
    except BookNotFound as e:
        return json.dumps({'error': str(e)}), 404
    # finally:
    #     return json.dumps({'error': 'internal error'}), 500


@app.route('/recent-activity', methods=['GET'])
def recent_activity():
    try:
        repository = get_gutenberg_repository()
        return json.dumps(repository.get_recent_activity())
    except Exception:
        return json.dumps({'error': 'internal error'}), 500


@app.route('/text-analysis/book/<int:book_id>', methods=['GET'])
def text_analysis(book_id):
    try:
        repository = get_gutenberg_repository()
        book_text = repository.get_book(book_id)['text']
        return json.dumps({'text': get_plot_summary_analysis(book_text)})
    except Exception:
        return json.dumps({'error': 'internal error'}), 500



