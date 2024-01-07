import re
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import csv
from urllib.error import HTTPError

def extract_asin(url):
    pattern = r'/dp/([A-Za-z0-9]{10})'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

def get_reviews(asin):
    review_list = []
    base_url = f"https://www.amazon.in/product-reviews/{asin}"
    page = 1

    while True:
        url = f"{base_url}/ref=cm_cr_getr_d_paging_btm_next_{page}?pageNumber={page}"
        print(url)

        headers = {"replace with your user agent"}
        req = Request(url, headers=headers)

        try:
            html = urlopen(req)
        except HTTPError as e:
            if e.code == 404:
                print(f"Page {page} not found. Exiting.")
                break
            else:
                print(f"Error accessing page {page}: {e}")
                continue

        soup = BeautifulSoup(html, 'html.parser')
        review_elements = soup.find_all('span', class_='a-size-base review-text review-text-content')
        review_element_1 = soup.find_all('div', class_="a-row a-spacing-small review-data")

        for review_element in zip(review_elements, review_element_1):
            # print(review_element[0].text.strip() + review_element[1].text.strip())
            review_list.append(review_element[0].text.strip() + review_element[1].text.strip())

        next_button = soup.find('li', class_='a-last')
        if not next_button:
            print(f"No more pages. Exiting.")
            break

        page += 1
        time.sleep(10) 
    return review_list

# amazon_url = "https://www.amazon.in/Samsung-Galaxy-Ultra-Green-Storage/dp/B0BTYWFXKC/ref=sr_1_1?crid=SCY9POQUG62U&keywords=samsung+s23+ultra+5g&qid=1704572312&sprefix=%2Caps%2C181&sr=8-1"
# asin = extract_asin(amazon_url)

# reviews = get_reviews(asin)


# csv_file_path = 'reviews.csv'
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(['Reviews'])
#     for review_text in reviews:
#         csv_writer.writerow([review_text])

# print(f"Reviews have been saved to {csv_file_path}.")
