import requests
import bs4
import re


class ParserHabr:

    def __init__(self):
        self.base_url = 'https://habr.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

    def __connect_bs4(self, url):
        self.response = requests.get(self.base_url + url, headers=self.headers)
        self.text = self.response.text
        self.soup = bs4.BeautifulSoup(self.text, features="html.parser")
        return self.soup

    def search_preview_text(self, words):
        articles = self.__connect_bs4('/ru/all/').find_all('article')
        for article in articles:
            word_list = re.findall(r'\w+', article.find(class_="tm-article-body tm-article-snippet__lead").text, re.I)
            if set(word_list) & set(words):
                date_article = article.find(class_="tm-article-snippet__datetime-published").find("time").attrs['title']
                title = article.find("h2").find("span").text
                href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                result = f'<{date_article}>-<{title}>-<{self.base_url + href}>'
                print(result)

    def search_text_article(self, words):
        articles = self.__connect_bs4('/ru/all/').find_all('article')
        for article in articles:
            href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
            text_articles = re.findall(r'\w+', self.__connect_bs4(href).find(id="post-content-body").text, re.I)
            if set(text_articles) & set(words):
                date_article = article.find(class_="tm-article-snippet__datetime-published").find("time").attrs['title']
                title = article.find("h2").find("span").text
                result = f'<{date_article}>-<{title}>-<{self.base_url + href}>'
                print(result)
