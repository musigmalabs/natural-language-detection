import urllib.request 
from bs4 import BeautifulSoup


def format_text(unformatted):
    formatted = ''
    for c in unformatted.upper():
        if ord(c) >= 65 and ord(c) <= 90:
            formatted += c
    
    return formatted


def get_feature_blocks(url: str):
    html = urllib.request.urlopen(url)
    parser = BeautifulSoup(html, 'html.parser')

    for paragraph in parser.find_all("p"):
        txt = paragraph.text.strip()
        if len(txt) > 500:
            yield format_text(txt)


if __name__ == '__main__':
    # Put a project Gutenberg book link here
    url = 'https://www.gutenberg.org/cache/epub/16728/pg16728-images.html'

    with open('data.txt', 'at') as file:
        for block in get_feature_blocks(url):
            file.write(block + '\n')
