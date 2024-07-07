
import requests
from bs4 import BeautifulSoup
import queue
import re
import time
import random
import os
import csv
    
urls = queue.PriorityQueue()
urls.put((0.5, "https://www.reddit.com"))
    
visited_urls = []
products = []

while not urls.empty() and len(visited_urls)<2000:
    _, current_url = urls.get()
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, "lxml")
    link_elements = soup.select("a[href]")
    

    product = {}
    product["url"] = current_url
    image_tag = soup.select_one('.wp-post-image')
    if image_tag != None:
        product["image"] = soup.select_one(".wp-post-image")["src"]

    
    products.append(product)
    print(products)
    visited_urls.append(current_url)
    image_tag = soup.find('img', class_='wp-post-image')

    if image_tag and 'src' in image_tag.attrs:
        image_url = image_tag['src']
        print(f"Found image URL: {image_url}")

        response = requests.get(image_url)

        if response.status_code == 200:
            image_name = os.path.basename(image_url)
            save_path = os.path.join('fibo', image_name)

            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            if image_name.find('felix'):
                with open(save_path, 'wb') as file:
                    file.write(response.content)

    link_elements = soup.select("a[href]")
    for link_element in link_elements:
        url = link_element['href']

        if re.match(r"https://(?:.*\.)?reddit\.com", url):
            if url not in visited_urls and url not in [item[1] for item in urls.queue]:
                priority_score = 1
                if re.match(r"^https://reddit\.com/\d+/?$", url):
                    priority_score = 0.5
                urls.put((priority_score, url))
    time.sleep(random.uniform(1, 3))
with open('products.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for product in products:
        writer.writerow(product.values())
