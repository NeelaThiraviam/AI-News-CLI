from news import latest_news, search_news
from storage import load_articles, save_articles
from utils import (
    display_articles,
    open_article,
    filter_by_source,
    filter_by_date,
    mark_favorite,
)
from export import export_csv

saved = load_articles()

categories = {
    "1": "Artificial Intelligence",
    "2": "Machine Learning",
    "3": "Robotics",
    "4": "LLM",
    "5": "Generative AI",
    "6": "Computer Vision",
    "7": "Deep Learning",
    "8": "NLP",
    "9": "OpenAI",
    "10": "Salesforce AI",
}

while True:

    print("\n========== AI NEWS ==========")
    print("1. Latest News")
    print("2. Search News")
    print("3. Search by Category")
    print("4. Filter News")
    print("5. Open Article")
    print("6. Save Article")
    print("7. Delete Saved")
    print("8. View Saved")
    print("9. Mark Favorite ⭐")
    print("10. View Favorites ⭐")
    print("11. Export to CSV")
    print("12. Exit")

    choice = input("Choice: ")

    # ----------------------------
    # Latest News
    # ----------------------------
    if choice == "1":

        latest = latest_news()
        display_articles(latest)

    # ----------------------------
    # Search News
    # ----------------------------
    elif choice == "2":

        keyword = input("Keyword: ")

        result = search_news(keyword)

        display_articles(result)

    # ----------------------------
    # Search by Category
    # ----------------------------
    elif choice == "3":

        print("\nChoose Category\n")

        for key, value in categories.items():
            print(f"{key}. {value}")

        category = input("\nEnter Category Number: ")

        if category in categories:

            keyword = categories[category]

            articles = search_news(keyword)

            display_articles(articles[:10])

        else:

            print("Invalid Category")

    # ----------------------------
    # Filter News
    # ----------------------------
    elif choice == "4":

        latest = latest_news()

        print("\nFilter By")
        print("1. Source")
        print("2. Date")

        option = input("Choose: ")

        if option == "1":

            source = input("Enter Source Name: ")

            filtered = filter_by_source(latest, source)

            display_articles(filtered)

        elif option == "2":

            date = input("Enter Date (YYYY-MM-DD): ")

            filtered = filter_by_date(latest, date)

            display_articles(filtered)

        else:

            print("Invalid Option")

    # ----------------------------
    # Open Article
    # ----------------------------
    elif choice == "5":

        latest = latest_news()

        display_articles(latest)

        try:

            article_number = int(input("Select article number: "))

            if 1 <= article_number <= len(latest):

                open_article(latest[article_number - 1])

            else:

                print("Invalid article number.")

        except ValueError:

            print("Please enter a valid number.")

    # ----------------------------
    # Save Article
    # ----------------------------
    elif choice == "6":

        latest = latest_news()

        display_articles(latest)

        try:

            num = int(input("Article Number: "))

            if 1 <= num <= len(latest):

                article = latest[num - 1]

                article["favorite"] = False

                saved.append(article)

                save_articles(saved)

                print("Saved Successfully")

            else:

                print("Invalid article number.")

        except ValueError:

            print("Please enter a valid number.")

    # ----------------------------
    # Delete Saved Article
    # ----------------------------
    elif choice == "7":

        display_articles(saved)

        try:

            num = int(input("Delete Article Number: "))

            if 1 <= num <= len(saved):

                saved.pop(num - 1)

                save_articles(saved)

                print("Deleted Successfully")

            else:

                print("Invalid article number.")

        except ValueError:

            print("Please enter a valid number.")

    # ----------------------------
    # View Saved Articles
    # ----------------------------
    elif choice == "8":

        display_articles(saved)

    # ----------------------------
    # Mark Favorite
    # ----------------------------
    elif choice == "9":

        if not saved:

            print("No saved articles.")

            continue

        display_articles(saved)

        try:

            article_number = int(input("Enter article number: "))

            if mark_favorite(saved, article_number - 1):

                save_articles(saved)

                print("⭐ Article marked as favorite.")

            else:

                print("Invalid article number.")

        except ValueError:

            print("Please enter a valid number.")

    # ----------------------------
    # View Favorites
    # ----------------------------
    elif choice == "10":

        favorites = [
            article
            for article in saved
            if article.get("favorite", False)
        ]

        if favorites:

            display_articles(favorites)

        else:

            print("No favorite articles found.")

    elif choice == "11":

        export_csv(saved)

    # ----------------------------
    # Exit
    # ----------------------------
    elif choice == "12":

        print("Goodbye!")

        break

    else:

        print("Invalid Choice")