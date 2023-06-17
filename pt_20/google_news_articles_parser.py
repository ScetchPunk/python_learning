import urllib.request
from bs4 import BeautifulSoup
import os


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        newstxtfilename = "google_news_links.txt"
        if os.path.exists(os.path.abspath(newstxtfilename)):
            os.remove(os.path.abspath(newstxtfilename))
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "./articles" in url:
                with open(newstxtfilename, "a") as newstxtfile:
                    newstxtfile.write(f"https://news.google.com{url[1:]}\n")
                    print("\n" + "https://news.google.com" + url[1:])

news = "https://news.google.ru"
Scraper(news).scrape()
