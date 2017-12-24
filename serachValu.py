import requests
import db
from bs4 import BeautifulSoup

class Category():
    def __init__(self, categoryName, categoryUrl, connector):
        self.categoryName = categoryName
        self.categoryUrl = categoryUrl
        self.db_connector = connector

    def valuSearch(self):
        self.category(self.categoryUrl)

    def category(self, url):
        page = 1
        while 1:
            req2 = requests.get(url + "?type=0&page=" + str(page))
            page += 1
            soup2 = BeautifulSoup(req2.text, 'lxml')

            valuerSection = soup2.find('section', attrs={"class": "ranking_valuer"})
            allValuer = valuerSection.find_all('a')
            if not allValuer:
                break
            for valuer in valuerSection.find_all('a'):
                valuerUrl = valuer.get('href')
                if valuerUrl.find("categories") == -1:
                    self.valuer(valuerUrl)

    def valuer(self, url):
        req3 = requests.get(url)
        soup3 = BeautifulSoup(req3.text, 'lxml')
        valuerName = soup3.find('div', attrs={"class": "user_introduction"}).get_text().strip()
        connectSection = soup3.find('ul', attrs={"class": "prf_list"})
        print(valuerName)
        twitter = ""
        instagram = ""
        facebook = ""
        homepage = ""
        coinprism = ""
        for sns in connectSection.find_all('a'):
            snsUrl = sns.get('href')
            if snsUrl.find("twitter") != -1:
                twitter = snsUrl
            elif snsUrl.find("instagram") != -1:
                instagram = snsUrl
            elif snsUrl.find("facebook") != -1:
                facebook = snsUrl
            elif snsUrl.find("coinprism") != -1:
                coinprism = snsUrl
            else:
                homepage = snsUrl
            info = (valuerName, self.categoryName, twitter, instagram, facebook, homepage, coinprism)
            # self.db_connector.insertUserInfomation(info)

class ValuCollector():
    def __init__(self):
        self.db_connector = db.DB()

    def categoris(self, target_url):
        req = requests.get(target_url)
        soup = BeautifulSoup(req.text, 'lxml')

        categorySection = soup.find('section', attrs={"class": "valuer_category"})
        for category in categorySection.find_all('a'):
            categoryName = category.find('b').get_text()
            categoryUrl = category.get('href')
            c = Category(categoryName, categoryUrl, self.db_connector)
            c.valuSearch()

    def run(self):
        self.categoris('https://valu.is/users/categories/')
        self.categoris('https://valu.is/users/categories?page=2')
        self.categoris('https://valu.is/users/categories?page=3')

if __name__ == '__main__':
      collector = ValuCollector()
      collector.run()