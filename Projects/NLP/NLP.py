# pip install nltk

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tree import Tree

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


# Tokenization
text = "This is a sample sentence. Tokenization is the first step in NLP."
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Stopword Removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
print("Filtered Tokens:", filtered_tokens)

# Frequency Distribution
fdist = FreqDist(filtered_tokens)
print("Most Common Words:", fdist.most_common(3))

# Sentiment Analysis
sentiment_analyzer = SentimentIntensityAnalyzer()
sentiment_scores = sentiment_analyzer.polarity_scores(text)
print("Sentiment Scores:", sentiment_scores)

# Syntax Parsing
sentence = input("Enter: ")
tokens = word_tokenize(sentence)
tagged_tokens = nltk.pos_tag(tokens)
parse_tree = nltk.ne_chunk(tagged_tokens)

# Draw Syntax Tree
parse_tree.draw()