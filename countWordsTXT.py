from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from crawlText import BSobj, getTitle, getText

url = input('Insert Link (The Jakarta Post) : ')

target = BSobj(url)

title_txt = getTitle(target)

one_text = getText(target)

# convert to lowercase

low_text = one_text.lower()

# split into tokens

tokens = word_tokenize(low_text)

# removing punctuation from tokens

words = [word for word in tokens if word.isalpha()]

# removing stopwords

stopwrd_set = set(stopwords.words('english'))

cleaned_words = [w for w in words if not w in stopwrd_set] 

# count words

count_words = Counter(cleaned_words)
