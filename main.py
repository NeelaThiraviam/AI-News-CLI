from news import latest_news
from news import search_news
from storage import load_articles
from storage import save_articles
from utils import display_articles


saved = load_articles()


while True:

    print("\n========== AI NEWS ==========")

    print("1.Latest News")
    print("2.Search")
    print("3.View Saved")
    print("4.Save Latest Article")
    print("5.Delete Saved")
    print("6.Exit")

    choice = input("Choice : ")

    if choice == "1":

        latest = latest_news()

        display_articles(latest)

    elif choice == "2":

        keyword = input("Keyword : ")

        result = search_news(keyword)

        display_articles(result)

    elif choice == "3":

        display_articles(saved)

    elif choice == "4":

        latest = latest_news()

        display_articles(latest)

        num = int(input("Article Number : "))

        saved.append(latest[num - 1])

        save_articles(saved)

        print("Saved Successfully")

    elif choice == "5":

        display_articles(saved)

        num = int(input("Delete Number : "))

        saved.pop(num - 1)

        save_articles(saved)

        print("Deleted")

    elif choice == "6":

        print("Goodbye")

        break

    else:

        print("Invalid Choice")