from html.parser import HTMLParser
from urllib.request import urlopen, Request
import os
import string

custom_header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chome/71.0.3578.98 Safari/537.36"}

class EinthusanTamilParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.div_flag = 0
        self.span_flag = 0

    def handle_starttag(self, tag, attrs):
        if 'div' == tag:
            print(attrs)
    
def main():
    language = "tamil"
    variables_dict = {"Numbers": [""], "Alphabet": list(string.ascii_uppercase)}
    for key, values in variables_dict.items():
        for value in values:
            page_number = 1
            last_page = 1
            while page_number <= last_page:
                einthusan_url = f"https://einthusan.ca/movie/results/?lang={language}&page={page_number}&find={key}&alpha={value}"
                page_number += 1
                print(einthusan_url)

    return
    """
    https://einthusan.ca/movie/results/?find=Numbers&lang=tamil&page=2
    https://einthusan.ca/movie/results/?lang=tamil&page=1&find=Alphabets&alpha=A
    """

if __name__ == "__main__":
    main()
