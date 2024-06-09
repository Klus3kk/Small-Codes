import requests
from bs4 import BeautifulSoup
import feedparser
from newspaper import Article

def news_chooser(categories, n, language):
    news = []
    for category in categories:
        if category == 'world':
            if language == 'pl':
                url = 'https://wiadomosci.wp.pl/rss.xml'  # Wirtualna Polska (PL)
            else:
                url = 'https://feeds.bbci.co.uk/news/world/rss.xml'  # BBC News (EN)

        elif category == 'music':
            if language == 'pl':
                url = 'https://muzyka.interia.pl/feed'  # Interia Muzyka (PL)
            else:
                url = 'https://pitchfork.com/rss/news/'  # Pitchfork (EN)

        elif category == 'films':
            if language == 'pl':
                url = 'https://www.filmweb.pl/news'  # Filmweb (PL)
            else:
                url = 'https://www.hollywoodreporter.com/rss/feed/movies'  # Hollywood Reporter (EN)

        elif category == 'ecology':
            if language == 'pl':
                url = 'https://naukaoklimacie.pl/feed'  # Nauka o klimacie (PL)
            else:
                url = 'https://www.nationalgeographic.com/environment/rss'  # National Geographic (EN)

        elif category == 'economy':
            if language == 'pl':
                url = 'https://www.bankier.pl/rss/wiadomosci'  # Bankier.pl (PL)
            else:
                url = 'https://www.economist.com/finance-and-economics/rss.xml'  # The Economist (EN)

        elif category == 'arts':
            if language == 'pl':
                url = 'https://culture.pl/en/rss'  # Culture.pl (PL - wersja angielska)
            else:
                url = 'https://www.artnews.com/feed/'  # ARTnews (EN)

        elif category == 'games':
            if language == 'pl':
                url = 'https://www.gry-online.pl/rss/news.xml'  # Gry-Online (PL)
            else:
                url = 'https://www.polygon.com/rss/index.xml'  # Polygon (EN)

        elif category == 'sport':
            if language == 'pl':
                url = 'https://www.sport.pl/rss/sport'  # Sport.pl (PL)
            else:
                url = 'https://www.espn.com/espn/rss/news'  # ESPN (EN)

        elif category == 'tech':
            if language == 'pl':
                url = 'https://spidersweb.pl/feed'  # Spidersweb (PL)
            else:
                url = 'https://www.theverge.com/rss/index.xml'  # The Verge (EN)

        # Parsowanie RSS lub stron bez RSS
        if category != 'films':
            feed = feedparser.parse(url)
            for entry in feed.entries[:n]:
                article = Article(entry.link)
                article.download()
                article.parse()
                first_three_sentences = '.'.join(article.text.split('.')[:3]) + '.'
                news.append({
                    'title': article.title,
                    'summary': first_three_sentences,
                    'link': entry.link,
                    'image': article.top_image, 
                    'category': category
                })
        else:  # Parsowanie Filmweb (PL)
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            news_items = soup.find_all('div', class_='newsPreview__card')[:n]
            for item in news_items:
                title = item.find('h2', class_='newsPreview__title').text.strip()
                summary = item.find('div', class_='newsPreview__description').text.strip()
                link = 'https://www.filmweb.pl' + item.find('a')['href']
                image = item.find('img')['data-src']
                news.append({
                    'title': title,
                    'summary': summary,
                    'link': link,
                    'image': image,
                    'category': category
                })

    return news

while True:
    categories_input = input("Choose categories (comma-separated): world, music, films, ecology, economy, arts, games, sport, tech, or q to quit: ")
    if categories_input.lower() == 'q':
        break
    categories = [c.strip() for c in categories_input.split(',')]

    language = input("Choose language (pl or en): ")

    n = int(input("How many news do you want? "))

    news = news_chooser(categories, n, language)
    for i, news1 in enumerate(news, start=1):
        print(f"{i}. {news1['title']}")
        print(news1['summary'])
        print()  # Pusta linia dla lepszej czytelności
