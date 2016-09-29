import sys
import codecs

filename, outfile = sys.argv[1], sys.argv[2]
tweets = []

with codecs.open(str(filename), "r", encoding='utf-8', errors='ignore') as f:

    for line in f:
        tweet = line.split(',')[0]
        tweets.append(tweet)

    outf = open(str(outfile), "w")
    for tweet in tweets:
        outf.write(tweet + "\n")

    outf.close()