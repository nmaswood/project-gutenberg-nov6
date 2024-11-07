import requests
from bs4 import BeautifulSoup
from flaskr.custom_exceptions import BookNotFound


def get_book_text(book_id):
    response = requests.get(f'https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt')
    return response.text


def get_book_metadata(book_id):
    response = requests.get(f'https://www.gutenberg.org/ebooks/{book_id}')
    soup = BeautifulSoup(response.content, 'html.parser')
    page_content_found = soup.find('div', {'id': 'page_content'})
    page_not_found = page_content_found and page_content_found.find('h1').text == 'No ebook by that number.'
    if page_not_found:
        raise BookNotFound("could not find book with id: {book_id}")

    return {
        "author": soup.find('a', {'itemprop': 'creator'}).text,
        "title": soup.find('td', {'itemprop': 'headline'}).text,
        "language": soup.find('tr', {'itemprop': 'inLanguage'}).find('td').text,
        "date_published": soup.find('td', {'itemprop': 'datePublished'}).text,
    }


