import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Amazon search results page
URL = 'https://www.amazon.in/s?k=books&crid=1CLCDLGQ66CNT&sprefix=books%2Caps%2C276&ref=nb_sb_noss_2'  # Example search for "serum"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}

# Send request and parse page
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# List to store product data
product_list = []

# Find all product containers
products = soup.find_all("div", {"data-component-type": "s-search-result"})  # Amazon search result container

# Extract details for each product
for product in products:
    # Extract Title
    title_tag = product.find("h2", class_="a-size-medium a-spacing-none a-color-base a-text-normal")
    title = title_tag.get_text(strip=True) if title_tag else "Title Not Available"

    # Extract Price
    price_tag = product.find("span", class_="a-price-whole")
    price = price_tag.get_text(strip=True) if price_tag else "Price Not Available"

     # Extract product URL to get individual product page
    product_url = product.find("a", class_="a-link-normal s-line-clamp-2 s-link-style a-text-normal")["href"]
    product_url = f"https://www.amazon.in{product_url}"  # Complete the URL

    # Send request to the individual product page
    product_page = requests.get(product_url, headers=headers)
    product_soup = BeautifulSoup(product_page.content, 'html.parser')

    # Extract Availability from the individual product page
    available_tag = product_soup.find("span", class_="a-size-medium a-color-success")
    available = available_tag.get_text(strip=True) if available_tag else "Availability Not Shown"

    # Extract Reviews
    review_tag = product.find("span", class_="a-icon-alt")
    review = review_tag.get_text(strip=True) if review_tag else "No Reviews"

    # Append extracted data to the list
    product_list.append({
        "Title": title,
        "Price": price,
        "Availability": available,
        "Reviews": review
    })


df = pd.DataFrame(product_list)
df.to_csv("amazon_products.csv", index=False)

print("Data successfully saved to amazon_products.csv")
