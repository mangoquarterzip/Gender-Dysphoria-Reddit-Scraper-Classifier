from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import praw

user_agent = "Scraper 1.0 by /u/mangoquarterzip"
reddit = praw.Reddit(
    client_id="bhIgjLRkgva0Cb9GDDpydg",
    client_secret="Zx2rsvN3660ctb-tTZJUeIxEJmNnSw",
    user_agent= user_agent
)

headlines = set()
for submission in reddit.subreddit("GenderDysphoria").new(limit=20):
    #print(submission.title)
    """print(submission.id)
    print(submission.author)
    print(submission.created_utc)
    print(submission.score)
    print(submission.upvote_ratio)
    print(submission.url)
    break"""
    headlines.add(submission.selftext + "\n---------------------------------------------------")

print(len(headlines))

df = pd.DataFrame(headlines)
df.head()
df.to_csv("headlines.csv", header = False, encoding = "utf-8", index = False)

#csv conversion to txt format
text = open("headlines.csv", "r")
text = ' '.join([i for i in text])
text = text.replace(",", " ")
with open('textformat.txt', 'w') as f:
    f.writelines(text)

g = open("textformat.txt", "r")
article = g.read()

from nltk.stem import PorterStemmer
porter = PorterStemmer()
for word in article.split():
    print(porter.stem(word))








"""
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download("vader_lexicon")
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score["headline"] = line
    results.append(pol_score)

pprint(results[:3], width=100)

df = pd.DataFrame.from_records(results)
df.head()

df["label"]=0
df.loc[df["compound"] > 0.2, "label"] = 1
df.loc[df["compound"] > -0.2, "label"] = -1
df.head()

df2 = df[["headline", "label"]]
df2.to_csv("reddit_headlines_labels_csv", encoding="utf-8", index = False)
"""


