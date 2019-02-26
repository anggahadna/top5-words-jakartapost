# Top-5-Words-Counter for The Jakarta Post Article

A simple program to take five most frequent words from an article in The Jakarta Post's site

--------------

## Getting Started

*Before we start,  I want to tell you (again) that this is just for learning purpose only.*

This program is developed from my previous project (check [here](https://github.com/anggahadna/python-crawler-thejakartapost)). The aim of this program is to count five most frequent words that appears in an article in The Jakarta Post's site. There are two python files : [crawlText.py](https://github.com/anggahadna/top5-words-jakartapost/blob/master/crawlText.py) and [countWordsTXT.py](https://github.com/anggahadna/top5-words-jakartapost/blob/master/countWordsTXT.py).

Inside [crawlText.py](https://github.com/anggahadna/top5-words-jakartapost/blob/master/crawlText.py), I placed 3 functions that will be used to crawl the the article from the site. The output from these functions is BeautifulSoup object, the title, and the text/paragraph -- for each function.

The main code is in [countWordsTXT.py](https://github.com/anggahadna/top5-words-jakartapost/blob/master/countWordsTXT.py). In this file, the code preprocesses text that has been crawled using the previous file, and then count how many times each word has been appeared and take the top 5. After getting these top frequent words, the program will plot them into a single figure and save it into a *.png file.

### Prerequisites

For [crawlText.py](https://github.com/anggahadna/top5-words-jakartapost/blob/master/crawlText.py), the code requires :
* BeautifulSoup
* requests

And for [countWordsTXT.py](https://github.com/anggahadna/top5-words-jakartapost/blob/master/countWordsTXT.py), the code requires :
* Counter (from *collections*)
* word_tokenize (from *nltk.tokenize*)
* stopwords (from *nltk.corpus*)
* pandas

Make sure you have installed them on your system. Connection to the internet also required to crawl the text.

## Running the program

Run the program by using

```shell
$ python countWordsTXT.py
```

When the program asks to input the link, insert the url of the article. Make sure you include the *"https://"* in front of the link, because *requests* library needs it to run. For example, 

```shell
Insert Link (The Jakarta Post) : https://www.thejakartapost.com/news/2019/02/26/scavengers-work-under-radar-to-help-reduce-waste.html
```
Then click Enter.

The program will print five most frequent words that appeared in that article. In this case, the program will show :

```
5 Most Frequent Words from Article 
"Scavengers work under radar to help reduce waste"
Words  Count
     waste     17
scavengers      9
   jakarta      9
      city      8
      azis      5
```

A *figure.png* file will generated automatically. In this case, the figure will be like this :

![alt text](https://github.com/anggahadna/top5-words-jakartapost/blob/master/figure.png "Figure")

### Note

To make the code simple, this program doesn't accomodate other cases outside the given above. For example, if you insert url without the protocol, it will result an error.

Feel free to give any criticsm and suggesetion. Thanks!