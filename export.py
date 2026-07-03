import csv
import os
import platform
import subprocess


def export_csv(articles):
    os.makedirs("exports", exist_ok=True)

    filename = "exports/articles.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Title",
            "Source",
            "Published Date",
            "URL"
        ])

        for article in articles:
            writer.writerow([
                article.get("title", ""),
                article.get("source", {}).get("name", ""),
                article.get("publishedAt", ""),
                article.get("url", "")
            ])

    print("✅ CSV Exported Successfully!")

    system = platform.system()

    if system == "Darwin":          # macOS
        subprocess.run(["open", filename])

    elif system == "Windows":
        os.startfile(filename)

    elif system == "Linux":
        subprocess.run(["xdg-open", filename])