import sys
from wordcloud import WordCloud
import codecs

stopwords = set(["a", "able", "about", "across", "after", "all", "almost",
                 "also", "am", "among", "an", "and", "any", "are", "as", "at",
                 "be", "because", "been", "but", "by", "can", "cannot",
                 "could", "dear", "did", "do", "does", "either", "else",
                 "ever", "every", "for", "from", "get", "got", "had", "has",
                 "have", "he", "her", "hers", "him", "his", "how", "however",
                 "i", "if", "in", "into", "is", "it", "its", "just", "least",
                 "let", "like", "likely", "may", "me", "might", "most",
                 "must", "my", "neither", "no", "nor", "not", "of", "off",
                 "often", "on", "only", "or", "other", "our", "own", "rather",
                 "said", "say", "says", "she", "should", "since", "so",
                 "some", "than", "that", "the", "their", "them", "then",
                 "there", "these", "they", "this", "tis", "to", "too", "twas",
                 "us", "wants", "was", "we", "were", "what", "when", "where",
                 "which", "while", "who", "whom", "why", "will", "with",
                 "would", "yet", "you", "your", "you're'"])

#random words that showed up alot
stopwords.update(['rt', 'trump', 'hillary', 'co', 'com', 'www', 'twitter',
                  'donald', 'clinton', 'hillaryclinton', 'debatenight', 'presidentialdebate',
                  'debates2016', 'retweet', 'follow', 'thebriefing2016', 
                  'realdonaldtrump', 'debate', 'tonight\'s', 'poll', 'status', 'tonight', 'vote'
                  'american', 'america', 'during', 'media', 'presidential',
                  'watch', 'cnn', 'foxnews', 'i\'ve', 'can\'t', 'breaking', 'vote', 'debates', 
                  'ahead', 'one','polls', 'clinton\'s', 'debate2016', 'trump\'', 'trump\'s'])
#questionable words to filter
stopwords.update(['teamtrump', 'president', 'good', 'hilary', 'keep', 'never',
                  'think', 'first', 'time', 'make', 'take', 'more', 'keep'])
stopwords.update(['https', 'http', 'deleted', 'gt'])
stopwords.update(map(str, range(10)  ))

filename = sys.argv[1]

# text = codecs.open(str(filename), "r", encoding='utf-8', errors='ignore').read()
text = open(str(filename), "r").read()


# cloud = WordCloud().generate(text)

import matplotlib.pyplot as plt
# plt.imshow(cloud)
# plt.axis("off")

# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(width=1600, 
                      height=1000, 
                      max_words=200,
                      max_font_size=None, 
                      relative_scaling=.5,
                      stopwords=stopwords).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()