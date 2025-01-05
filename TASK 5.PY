import requests
from bs4 import BeautifulSoup
import pandas as pd

class ProductScraper:
    def __init__(self, base_url, max_products=50):
        self.base_url = base_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        }
        self.max_products = max_products
        self.products = []

    def get_soup(self, page_number):
        url = f"{self.base_url}?page={page_number}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return BeautifulSoup(response.content, "html.parser")
        raise Exception(f"Failed to retrieve page {page_number}")

    def extract_product_data(self, soup):
        product_items = soup.find_all("div", class_="product-item")
        for product in product_items:
            if len(self.products) >= self.max_products:
                return False
            name = product.find("a", class_="product-title")
            price = product.find("span", class_="price")
            rating = product.find("div", class_="star-rating")
            self.products.append([
                name.get_text(strip=True) if name else "N/A",
                price.get_text(strip=True) if price else "N/A",
                rating.get_text(strip=True) if rating else "N/A"
            ])
        return True

    def save_to_csv(self):
        df = pd.DataFrame(self.products, columns=["Name", "Price", "Rating"])
        df.to_csv("products.csv", index=False)

    def scrape(self):
        page_number = 1
        while len(self.products) < self.max_products:
            soup = self.get_soup(page_number)
            if not self.extract_product_data(soup):
                break
            page_number += 1
        self.save_to_csv()

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
scraper = ProductScraper(url, max_products=20)
scraper.scrape()
