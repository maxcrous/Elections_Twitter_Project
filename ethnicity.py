"""
ethnicity.py

This program investigates the ethinicity of twitter users by using
enthnicity name statistics (John: 77% White, 20% Black, 2% Asian, etc).
These ethnicity score are taken to be actual counts instead of percentages
as we are interested in the ethnicity of a whole population of twitter users.
By this we mean that a name like John will not only contribute to the score
of the white counter (0.77), but also contribute 0.20 to the black counter.
This way, 100 tweets by users named John will translate into the statistically
reliable score, instead of 100 white population counts (if we were to go for
highest probability = class).
"""

from ethnicolr import census_ln
import os.path
import pandas as pd
import json
import matplotlib.pyplot as plt
import pickle

def preprocess_name(name):
    name = name.split(' ')[-1]
    name = name.capitalize()
    return name

white = 0
black = 0
asian = 0
hispanic = 0
native_american = 0
two_race = 0
df = []


if not os.path.exists('ethnicity.pkl'):

    with open('full.json', 'r') as tweets_file:

        for idx, line in enumerate(tweets_file):

            try:

                if idx % 10000 == 0 and idx != 0:
                    print(idx)
                    df = pd.DataFrame(df)
                    classed = census_ln(df, 'name')
                    classed = classed.dropna()
                    classed = classed.drop(['name'], axis=1)
                    classed = classed.replace('(S)', 0)
                    classed = classed.astype('float64')
                    classed = classed.divide(100)
                    white += float(classed['pctwhite'].sum())
                    black += float(classed['pctblack'].sum())
                    asian += float(classed['pctapi'].sum())
                    native_american += float(classed['pctaian'].sum())
                    two_race += float(classed['pct2prace'].sum())
                    hispanic += float(classed['pcthispanic'].sum())
                    df = []

                tweet = json.loads(line)
                name = tweet['user']['name']
                country = tweet['place']['country_code']
                if country != 'US':
                    continue
                last_name = preprocess_name(name)
                df.append({'name': last_name})

            except Exception as e:
                continue

        pickle.dump((white, black, asian, native_american, two_race, hispanic), open('ethnicity.pkl','wb'))

(white, black, asian, native_american, two_race, hispanic) = pickle.load(open('ethnicity.pkl','rb'))

print('White: {}, Black: {}, Asian: {}, Native American: {}, Two Races: {}'.format(black, asian, hispanic, native_american, two_race))

# Pie plot
labels = 'White','Two Races', 'Black', 'Asian', 'Hispanic', 'Native Americans'
sizes = [white,two_race, black, asian, hispanic, native_american]
plt.pie(sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=0.8)
plt.axis('equal')
plt.show()
