pip install request
pip install bs4
 
from bs4 import BeautifulSoup
import requests

URL = "https://www.flipkart.com/realme-xt-pearl-blue-64-gb/p/itm731360fdbd273?pid=MOBFJYBE9FHXFEFJ&srno=s_1_1" \
      "&otracker=AS_QueryStore_OrganicAutoSuggest_0_4_na_na_pr&otracker1" \
      "=AS_QueryStore_OrganicAutoSuggest_0_4_na_na_pr&lid=LSTMOBFJYBE9FHXFEFJVA0XQF&fm=SEARCH&iid=a611c9af-350b-423d" \
      "-87d8-df9bcc1987c7.MOBFJYBE9FHXFEFJ.SEARCH&ppt=sp&ppn=sp&ssid=n57aimhb7k0000001573581114720&qH=23f6a0071022557e "
      


    req_data = requests.get(URL)
review_soup = BeautifulSoup(req_data.content, 'html.parser')

all_reviews = review_soup.find_all('div', {'class': 'col _39LH-M'})
all_reviews
     
     
 

baseUrl = "https://www.flipkart.com"
all_reviews_link = review_soup.find('div', {'class': 'swINJg _3nrCtb'})
all_reviews_link
all_reviews_link.find_parent()
data = str(all_reviews_link.find_parent().get('href'))
print(baseUrl)
print(data)

url = baseUrl + data



    
print(user_list)rating_list = []
review_header_list = []
detailed_review_list = []
user_list = []
likes_dislikes_list = []
for review in all_reviews:
    #rating = review.find('div', {'class': 'hGSR34 E_uFuv'}).text
    review_header = review.find_all('p', {'class': '_2xg6Ul'})
    detailed_review = review.find_all('div', {'class': 'qwjRop'})
    detailed_review=[e.get_text() for e in detailed_review]
    user = review.find_all('p', {'class': '_3LYOAd _3sxSiS'})
    user=[e.get_text() for e in user]
    likes_dislikes = review.find_all('span', {'class': '_1_BQL8'})
    likes_dislikes=[e.get_text() for e in likes_dislikes]
    rating = review.find_all('div', {'class': 'hGSR34 E_uFuv'})
    text = [e.get_text() for e in rating]
    rating_list.append(text)
    review_header=[e.get_text() for e in review_header]
    review_header_list.append(review_header)
    detailed_review_list.append(detailed_review)
    user_list.append(user)
    likes_dislikes_list.append(likes_dislikes)
print(review_header_list)


baseUrl = "www.flipkart.com"

all_reviews_link = review_soup.find('div', {'class': 'swINJg _3nrCtb'})
all_reviews_link
all_reviews_link.find_parent()


baseUrl = "https://www.flipkart.com"
all_reviews_link = review_soup.find('div', {'class': 'swINJg _3nrCtb'})
all_reviews_link
all_reviews_link.find_parent()
data = str(all_reviews_link.find_parent().get('href'))
print(baseUrl)
print(data)

url = baseUrl + data


req_data = requests.get(url)
review_soup = BeautifulSoup(req_data.content, 'html.parser')



