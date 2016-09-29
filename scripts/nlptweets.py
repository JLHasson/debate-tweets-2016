import sys
import codecs
import spacy
from math import sqrt
from numpy import dot
from numpy.linalg import norm


def handle_tweet(spacy, tweet_data, query, out):
    # text = tweet_data.get('text', '')
    match_tweet(spacy, text.decode('utf8', errors="ignore"), query, out)

def match_tweet(spacy, text, query, out):
    def get_vector(word):
        return spacy.vocab[word].repvec

    tweet = spacy(text)
    tweet = [w.repvec for w in tweet if w.is_alpha and w.lower_ != query]
    if tweet:
        accept = map(get_vector, 'health care healthcare'.split())
        reject = map(get_vector, 'garden Reggie hairy'.split())
        y = sum(max(cos(w1, w2), 0) for w1 in tweet for w2 in accept)
        n = sum(max(cos(w1, w2), 0) for w1 in tweet for w2 in reject)
        
        if (y / (y + n)) >= 0.5 or True:
            out.append(text)

def main():

    filename, outfile = sys.argv[1], sys.argv[2]
    nlp = spacy.load('en')

    accepted = []

    # text = codecs.open(str(filename), "r", encoding='utf-8', errors='ignore').read() 
    # doc = nlp(text)

    with codecs.open(str(filename), "r", encoding='utf-8', errors='ignore') as f:
        for line in f:
            # s = line.split('"')[1]
            match_tweet(nlp, line, line, accepted)


    outf = open(str(outfile), "w")
    for tweet in accepted:
        outf.write(tweet + ",\n")

    outf.close()


def cos(v1, v2):
    return dot(v1, v2) / (norm(v1) * norm(v2))


if __name__ == "__main__":
    main()