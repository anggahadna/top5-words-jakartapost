'''
this file contains functions that will be used for crawling the text :
- getTitle(soup) --> get the title from given soup object
- getText(soup)  --> get the article/paragraph from given soup object
'''

from bs4 import BeautifulSoup
import requests

def bsObj(url):

    r = requests.get(url, timeout=5)
    soup = BeautifulSoup(r.content, "lxml")
    
    return soup

def getTitle(soup):
        
    title = soup.find('h1', {'class' : 'title-large'}).text
    
    return title

def getText(soup):
    
    line_text = []
    
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
                line_text.append(paragraphs)
    
    # joining line_text strings
    
    one_text = ' '.join(line_text)
    
    return one_text
