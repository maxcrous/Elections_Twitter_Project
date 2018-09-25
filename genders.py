"""
genders.py

The script determines the gender of twitter posters. This is done by
by using the gender_guesser library. Make sure to edit the name of the
file to read from appropriately.
"""

import json
from collections import Counter
import gender_guesser.detector as gender
import pickle
import os.path
import matplotlib.pyplot as plt

def preprocess_name(name):
    name = name.split(' ')[0]
    name = name.capitalize()
    return name


if not os.path.exists('gender_counter.pkl'):
    cnt = Counter()
    unique_cnt = Counter()
    d = gender.Detector()
    id_set = set()

    with open('full.json', 'r') as tweets_file:   # EDIT FILENAME
        for idx, line in enumerate(tweets_file):
            try:
                tweet = json.loads(line)
                name = tweet['user']['name']
                id = tweet['user']['id_str']
                name = preprocess_name(name)
                gender = d.get_gender(name)
                cnt[gender] += 1

                if idx % 10000 == 0:
                    print(idx)

                if id not in id_set:
                    id_set.add(id)
                    unique_cnt[gender] += 1

            except Exception as e:
                print (e)
                continue

    # Save the cnt and unique cnt variables to a file
    pickle.dump((cnt,unique_cnt), open('gender_counter.pkl', 'wb'))


(cnt, unique_cnt) = pickle.load(open('gender_counter.pkl', 'rb'))

# We will consider the mostly_female and
# mostly_male names as female and male respectively
male_count = cnt['male'] + cnt['mostly_male']
female_count = cnt['female'] + cnt['mostly_female']

unique_male_count = unique_cnt['male'] + unique_cnt['mostly_male']
unique_female_count = unique_cnt['female'] + unique_cnt['mostly_female']

total_gendered = male_count + female_count
unique_total_gendered = unique_male_count + unique_female_count
total = sum(cnt.values())
unknown = total - total_gendered

gendered_percent = (total_gendered / total) * 100
female_percent = (female_count / total_gendered) * 100
male_percent = (male_count / total_gendered) * 100

unique_female_percent = (unique_female_count / unique_total_gendered) * 100
unique_male_percent = (unique_male_count / unique_total_gendered) * 100

print('\nOut of all {} tweet, {} or {:.2f}% can be assigned a gender.'.format(total, total_gendered, gendered_percent))
print('\nOut of all {} tweet that can be assigned a gender, \
{} are male and {} are female.'.format(total_gendered, male_count, female_count))
print('That is to say, {:.2f}% male and {:.2f}% female '.format(male_percent, female_percent))

print('\nIf instead of tweets, we investigate unique users, there are {} males and {} females,'.format(unique_male_count,
                                                                                                     unique_female_count))
print('That is to say, {:.2f}% male and {:.2f}% female '.format(unique_male_percent, unique_female_percent))

# Pie plot male/female
labels = 'Male', 'Female'
colors = 'lightskyblue', 'lightcoral'
sizes = [male_percent, female_percent]
plt.pie(sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors )
plt.axis('equal')
plt.show()


# Pie plot male/female/unkown
labels = 'Male', 'Female', 'Unknown'
colors = 'lightskyblue', 'lightcoral', 'grey'
sizes = [male_count, female_count, unknown]
plt.pie(sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors )
plt.axis('equal')
plt.show()


# We will also analyse the percentages when only considering
# high confidence gender classification (not counting the
# mostly_male/female counts)
male_count = cnt['male']
female_count = cnt['female']
total_gendered = male_count + female_count
female_percent = (female_count / total_gendered) * 100
male_percent = (male_count / total_gendered) * 100
print("\n\n **** WHEN CONSIDERING ONLY STRONGLY CLASSIFIED NAMES **** ")
print('\nOut of all {} tweet, {} or {:.2f}% can be assigned a gender.'.format(total, total_gendered, gendered_percent))
print('\nOut of all {} tweet that can be assigned a gender, \
{} are male and {} are female.'.format(total_gendered, male_count, female_count))
print('That is to say, {:.2f}% male and {:.2f}% female '.format(male_percent, female_percent))


