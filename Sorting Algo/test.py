import bs4 as bs
import urllib.request
import re
import nltk
import heapq

#https://en.wikipedia.org/wiki/Artificial_intelligence
# While entering url press space after it and then press enter
url = input("Enter the url of article(add space after url before pressing enter): ")[:-1:]

print('Opening url...')
data = urllib.request.urlopen(url)
article = data.read()
print('Parsing...')
parsed_article = bs.BeautifulSoup(article, 'lxml')

# Fetch all the data inside paragraph tags
paragraphs = parsed_article.find_all('p')

article_text = ""
print('Fetching text...')
for p in paragraphs:
    article_text += p.text

# Removing Square Brackets and Extra Spaces
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

print("Checking for puntk and stopwords...")
nltk.download('punkt')
nltk.download('stopwords')

#Converting text to sentences
sentence_list = nltk.sent_tokenize(article_text)

#Counting frequency of each word which does not occur in stop words
print("Calculating frequency...")
stopwords = nltk.corpus.stopwords.words('english')
word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        word = word.lower()
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1


#Finding weighted frequency
print("Finding weighted frequency...")
maximum_frequncy = max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

#Calculating sentences scores
print("Calculating sentence scores...")
sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

#Finding summary sentences...
print("Finding summary sentences...")
summary_sentences = heapq.nlargest(10, sentence_scores, key= sentence_scores.get)

print("Summary sentences:")
print("")
for i in summary_sentences:
    print(i)
