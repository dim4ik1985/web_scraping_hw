import parser_habr


if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'я']

    item = parser_habr.ParserHabr()
    # Поиск по ключевым словам в превью статьи
    item.search_preview_text(KEYWORDS)
    print('_________________________________')
    # Поиск по ключевым словам в основном тексте статьи
    item.search_text_article(KEYWORDS)
