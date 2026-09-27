import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import time


BASE_URL = "https://books.toscrape.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

books_data = []


for page_number in range(1, 51):

    if page_number == 1:
        url = BASE_URL
    else:
        url = urljoin(
            BASE_URL,
            f"catalogue/page-{page_number}.html"
        )

    response = requests.get(
        url,
        headers=HEADERS
    )

    if response.status_code != 200:
        print("Unable to access page:", page_number)
        continue

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    books = soup.select(
        "article.product_pod"
    )

    for book in books:

        # Title
        title_tag = book.select_one("h3 a")
        title = title_tag.get("title")

        # Price
        price_text = book.select_one(
            ".price_color"
        ).get_text(strip=True)

        price = float(
            price_text.replace("Â£", "").replace("£", "")
        )

        # Availability
        availability = book.select_one(
            ".availability"
        ).get_text(" ", strip=True)

        # Rating
        rating_tag = book.select_one(
            ".star-rating"
        )

        rating_word = None

        if rating_tag:
            classes = rating_tag.get("class", [])

            for value in rating_map:
                if value in classes:
                    rating_word = value
                    break

        rating = rating_map.get(rating_word)

        # Product URL
        product_url = urljoin(
            url,
            title_tag.get("href")
        )

        # Store data
        books_data.append({
            "title": title,
            "price_gbp": price,
            "availability": availability,
            "rating": rating,
            "product_url": product_url,
            "page": page_number
        })

    print(
        f"Page {page_number} completed - "
        f"{len(books)} books found"
    )

    time.sleep(0.2)


# Create DataFrame
df = pd.DataFrame(books_data)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save CSV
df.to_csv(
    "books_scraped.csv",
    index=False
)


print("\n--------------------------------")
print("SCRAPING COMPLETED")
print("--------------------------------")

print(
    "Total books scraped:",
    len(df)
)

print("\nFirst 5 records:")
print(df.head())