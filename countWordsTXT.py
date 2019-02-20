from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from crawlText import bsObj, getTitle, getText

import pandas as pd

url = input('Insert Link (The Jakarta Post) : ')

target = bsObj(url)

title_txt = getTitle(target)
plot_title = '5 Most Frequent Words from Article \n"' + title_txt + '"'

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

# convert count_words to dataframe

df_words = pd.DataFrame(list(count_words.items()), columns=['Words', 'Count'])

# take 5 most frequent words

top_words = df_words.sort_values(['Count'], ascending=False).head(5)

print('\n', plot_title)
print(top_words.to_string(index=False))

# plot the top_words and save figure as png

bar = top_words.plot.bar(x='Words', y='Count', rot=0, title=plot_title, legend=False)

fig = bar.get_figure()
fig.savefig('figure.png')
