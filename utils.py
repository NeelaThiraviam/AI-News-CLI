import webbrowser


def display_articles(articles):

    if len(articles) == 0:
        print("No Articles Found")
        return

    for index, article in enumerate(articles, start=1):

        print("-" * 70)
        print(index)
        star = "⭐" if article.get("favorite", False) else " "
        print(f"{star} {article['title']}")
        print("Source :", article["source"]["name"])
        print("Date :", article["publishedAt"])
        print("URL :", article["url"])
        print()


def open_article(article):
    """Open the selected article in the default web browser."""
    webbrowser.open(article["url"])


def filter_by_source(articles, source):
    """Filter articles by source name."""
    return [
        article
        for article in articles
        if article.get("source", {}).get("name", "").lower() == source.lower()
    ]


def filter_by_date(articles, date):
    """Filter articles by published date (YYYY-MM-DD)."""
    return [
        article
        for article in articles
        if article.get("publishedAt", "").startswith(date)
    ]

def mark_favorite(saved_articles, index):

    if 0 <= index < len(saved_articles):

        saved_articles[index]["favorite"] = True

        return True

    return False