import parser_habr


if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'я']

    item = parser_habr.ParserHabr()
    # item.search_previer_text(KEYWORDS)
    item.search_text_article(KEYWORDS)
