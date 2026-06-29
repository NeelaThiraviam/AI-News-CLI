def display_articles(articles):

    if len(articles) == 0:
        print("No Articles Found")
        return

    for index, article in enumerate(articles, start=1):

        print("-" * 70)

        print(index)

        print("Title :", article["title"])

        print("Source :", article["source"]["name"])

        print("Date :", article["publishedAt"])

        print("URL :", article["url"])

        print()