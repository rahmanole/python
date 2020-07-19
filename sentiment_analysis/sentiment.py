import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(w):
    for x in punctuation_chars:
        w = w.replace(x, '')
    return w


positive_words = []
with open("positive_words.txt") as pos_f:
    pos_ws = pos_f.read().split('\n')[35:]
    positive_words = [w.strip() for w in pos_ws]

negative_words = []

with open('negative_words.txt', 'r') as neg_file:
    neg_ws = neg_file.read().split('\n')[35:]
    negative_words = [w.strip() for w in neg_ws]


def pos_score(tweet):
    t_words = tweet.split()
    fresh_twt_wrds = [strip_punctuation(x) for x in t_words]
    score = 0
    for x in positive_words:
        score += fresh_twt_wrds.count(x)
    return score


def neg_score(tweet):
    t_list = tweet.split()
    fresh_twt = [strip_punctuation(x) for x in t_list]
    score = 0
    for x in negative_words:
        score += fresh_twt.count(x)
    return score


with open('project_twitter_data.csv', 'r') as given_data:
    resulted_data = open('resulting_data.csv', 'w')
    resulted_data.write('Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score')
    resulted_data.write('\n')
    tweets = given_data.readlines()
    tweets.pop(0)
    for line in tweets:
        each_tweet_data = ''
        tweet_data = line.strip().split(',')
        p_score = pos_score(tweet_data[0])
        n_score = neg_score(tweet_data[0])
        net_score = p_score - n_score
        each_tweet_data = '{0}, {1}, {2}, {3}, {4}'.format(tweet_data[1], tweet_data[2], p_score, n_score, net_score)
        resulted_data.write(each_tweet_data)
        resulted_data.write('\n')

given_data.close()
resulted_data.close()

df = pd.read_csv('resulting_data.csv')
x = df['Net Score']
y = df['Number of Retweets']

sns.scatterplot(x,y,edgecolors='black',marker='o',s=100)
plt.xlabel('Net Score')
plt.ylabel('Number of Retweets')
plt.grid(True)
sns.set_style("darkgrid", {'axes.axisbelow': True})
sns.despine(fig=None, ax=None, top=True, right=True, left=True, bottom=True, offset=None, trim=False)
plt.title('Sentiment Analysis of Tweets')
plt.savefig('tweeter_data.jpg',dpi=1000)
plt.show()