
import requests
import json
from bs4 import BeautifulSoup
import os
import threading
import time


url = 'https://en.wikipedia.org/wiki/List_of_best-selling_books'
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MyScraper/1.0; +https://example.com/mybot)'
}

page = requests.get(url, headers=headers)
books = []
print(page.status_code)
if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    book_tables = soup.find_all(class_='wikitable')
    print(soup)
    for table in book_tables:
        rows = table.find_all('tr')
        for row in rows:
            data = row.find_all('td')
            if(len(data) != 6):
                continue
            book_name = data[0].get_text()
            author = data[1].get_text()
            published_date = data[3].get_text()
            approximate_sales = data[4].get_text()
            if "–" in approximate_sales:
                approximate_sales = data[5].get_text()
            approximate_sales = approximate_sales.split("[")[0]
            books.append({
                "name":book_name,
                "author":author,
                "published_date":published_date,
                "approximate_sales":approximate_sales
            })
    with open("book_data",'w+') as f:
        f.write(json.dumps(books))


f= open("book_data","r")
queue = json.loads(f.read())


directory_path = "books"

os.makedirs(directory_path, exist_ok=True) #can also do it with if os.path.exists("books") -> os.mdkir("books")

os.chdir("books")

authors_dictionary = {}

def write_book(book):
    author = book["author"]

    if author not in authors_dictionary:
        authors_dictionary[author] = threading.Lock()   # lock per author

    with authors_dictionary[author]:   
        if not os.path.exists(author):
            os.mkdir(author)

    
        lock_file = os.path.join(author, ".lock")
        while True:
            try:
                fd = os.open(lock_file, os.O_CREAT | os.O_EXCL | os.O_RDWR) #try to create file, if it already exists -> fail and open with read write permission 
                break
            except FileExistsError:
                time.sleep(0.1) #wait for another priocess to release

        book_name = book["name"].replace("/", "")
        file_name = os.path.join(author, f"{book_name}.json")
        with open(file_name, "w+") as f:
            f.write(json.dumps(book))

for book in queue:
    write_book(book)



