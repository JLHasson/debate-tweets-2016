import nltk
from wordcloud import WordCloud
import re
import sys
import codecs
import dask.bag as db

filename, outfile = sys.argv[1], sys.argv[2]

isword = re.compile("#(\w+)").search

def to_hashtag(body):
    """Convert a comment to a list of words."""
    if not body:
        return []
    words = [w.lower() for w in nltk.word_tokenize(body)]
    return [w for w in words if isword(w)]

tags = []

with codecs.open(str(filename), "r", encoding='utf-8', errors='ignore') as f:

    for line in f:
        for w in re.findall("#(\w+)", line):
            tags.append(w)

    b = db.from_sequence(tags)

    top_tags = b.frequencies().topk(100, key=1)
    top_tags = top_tags.compute()

    import matplotlib.pyplot as plt
    print(top_tags)
    cloud = WordCloud(width=800, height=600).generate_from_frequencies(top_tags)
    plt.figure()
    plt.imshow(cloud)
    plt.axis("off")
    plt.show()

    outf = open(str(outfile), "w")
    for o in tags:
        outf.write(o + ", ")

    outf.close()