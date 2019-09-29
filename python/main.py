from html.parser import HTMLParser
from urllib.request import urlopen, Request
import os
import gzip
import string

custom_header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chome/71.0.3578.98 Safari/537.36"}

class EinthusanParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movie_title_flag = False
        self.last_page = 0
        self.page_flag = -1
        self.movie_list = []
        self.movie = ""

    def handle_starttag(self, tag, attrs):
        if "div" == tag:
            if ("class", "results-info") in attrs:
                self.page_flag += 1
            if ("class", "block2") in attrs:
                self.movie_title_flag = True
        if 'p' == tag and self.page_flag == 0:
            self.page_flag += 1

        if "span" == tag and ("class", "popular") in attrs:
            self.movie_list.append(self.movie)

    def handle_data(self, data):
        if self.page_flag == 1:
            self.last_page = int(data.split()[-1])
            self.page_flag = -1
        if self.movie_title_flag == True:
            self.movie = data
            self.movie_title_flag = False
    
def main():
    language = "tamil"
    variables_dict = {"Numbers": [""], "Alphabets": list(string.ascii_uppercase)}
    movie_list = []
    for key, values in variables_dict.items():
        for value in values:
            page_number = 1
            last_page = 1
            while page_number <= last_page:
                einthusan_url = f"https://einthusan.ca/movie/results/?lang={language}&page={page_number}&find={key}&alpha={value}"
                print(einthusan_url)
                url_obj = urlopen(Request(einthusan_url, headers=custom_header))
                html_page = gzip.decompress(url_obj.read()).decode('utf-8')
                einth_parser_obj = EinthusanParser()
                einth_parser_obj.feed(html_page)
                page_number += 1
                if einth_parser_obj.last_page > last_page:
                    last_page = einth_parser_obj.last_page
                movie_list += einth_parser_obj.movie_list
                print(einth_parser_obj.movie_list)

    return
    """
    https://einthusan.ca/movie/results/?find=Numbers&lang=tamil&page=2
    https://einthusan.ca/movie/results/?lang=tamil&page=1&find=Alphabets&alpha=A
    """

if __name__ == "__main__":
    main()
