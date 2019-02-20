from bs4 import BeautifulSoup
from collections import Counter
from nltk.tokenize import word_tokenize
import requests
import string

url = input('Insert Link (The Jakarta Post) : ')

r = requests.get(url, timeout=5)

soup = BeautifulSoup(r.content, "lxml")

all_text = []

title = soup.find('h1', {'class' : 'title-large'}).text

# detect the right category of the article

cat1 = soup.find_all('div', {'class' : 'col-md-10 col-xs-12 detailNews'}) #news
cat2 = soup.find_all('div', {'class' : 'col-md-10 col-xs-12 detailNews wdsk wtbl'}) #multimedia
cat3 = soup.find_all('div', {'class' : 'show-define-text'}) #lifestyle, travel
cat4 = soup.find_all('div', {'id' : 'show-define-text'})

if len(cat1) == 1:
    cat = cat1
elif len(cat2) == 1:
    cat = cat2
elif len(cat3) == 1:
    cat = cat3
elif len(cat4) == 1:
    cat = cat4
    
# take all text with "p" tag under specific tag and class
    
for article in cat:
    for n in article.descendants:
        if n.name == 'p':
            paragraphs = n.text
            all_text.append(paragraphs)

# joining all_text strings
            
one_text = ' '.join(all_text)

# removing punctuation from one_text

rem_punc = str.maketrans('', '', string.punctuation)
one_rem = one_text.translate(rem_punc)

# split words in one_rem

split_one = one_rem.split()

# count words

hitung = Counter(split_one)

## coba tokenize

tokens = word_tokenize(one_text)