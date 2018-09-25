"""
hashtags.py

The script investigates hashtags. Which hashtags were popular? What
is the distribution of hashtag popularity? Can hashtags help in
sentiment analysis? How do hashtags relate to other statistics,
like gender preferences.
"""

import json
from collections import Counter
import pickle
import os.path
import numpy as np
import matplotlib.pyplot as plt



def preprocess_name(name):
    name = name.split(' ')[0]
    name = name.capitalize()
    return name

hashtag_cnt = Counter()
tag_counter = 0


if not os.path.exists('hashtag_cnt.pkl'):
    with open('full.json', 'r') as tweets_file:   # EDIT FILENAME
        for idx, line in enumerate(tweets_file):
            try:
                tweet = json.loads(line)
                hash_tags  = tweet['entities']['hashtags']
                for tag in hash_tags:
                    tag_counter += 1
                    text = tag['text']
                    hashtag_cnt[text] += 1

                if idx % 10000 == 0:
                    print(idx)

            except Exception as e:
                print (e)
                continue

    pickle.dump(hashtag_cnt, open('hashtag_cnt.pkl', 'wb'))

# Plot the 100 most popular tweets to see their popularity distribution.
hashtag_cnt = pickle.load(open('hashtag_cnt.pkl', 'rb'))
total_nr_hashtags = sum(hashtag_cnt.values())
tag_popularities = sorted(hashtag_cnt.values(),reverse=True)
plt.plot(tag_popularities[:100])
plt.title('Hashtags in descending popularity')
plt.xlabel('DIfferent Hashtags')
plt.ylabel('# times used')
plt.show()



print(hashtag_cnt.most_common(100))
# Some general statistics
top_ten = sum(tag_popularities[:10])
top_hundred = sum(tag_popularities[:100])

percentage_ten = (top_ten / total_nr_hashtags) * 100
precentage_hundred = (top_hundred / total_nr_hashtags) * 100

print('The first 10 hashtags account for {:.2f}% of all hashtags used:'.format(percentage_ten))
print('The first 100 hashtags account for {:.2f}% '.format(precentage_hundred))