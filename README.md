# Elections_Twitter_Project
An analysis of tweets written during the presidential elections in the USA. The report for this project can be found at https://www.overleaf.com/19991169vdwgfswrcmkp#/73316941/.


# Main Goal
- **Identifying blue and red states** By combining sentiment analysis and geo-info, can we get an idea of how much a candidate is liked/disliked in a state? How does this compare to election results      
- **Sentiment analysis.** For this project, sentiment analysis is very important. We need to find an appropriate / well performing sentiment analysis library. Try out different libraries that work out of the box (a function that takes a string and returns a pos/neu/neg score). Report which one works best on the first 100 tweets. A good start could be  nltk.sentiment.vader or other sentiment analysers in the nltk library.

**Put more essential stuff here** 

# Raport writing 
- **Write an introduction.** What is our report about, what assignment does it concern, where is our dataset from and what are trying to accomplish. 
- **Abstract.**. Probably only possible to write this one when the rest is done. 



# Interesting Statistics 
- **Who likes to tweet? (Savvina)** ✅ The average number of tweets per inhabitant for each state.
- **Peaks and valleys of activity. (Savvina)** ✅ At what time of the day do people tweet (on an hourly scale and dayly scale). 
- **Which kind of tweets are replied the most? (Albert)** Are neutral tweet more or less likely to be replied than positive and negative tweets?
- **International preferences.** Do other countries tend to side with Hillary, Trump, or both? Which countries engaged most with the elections on twitter, and why. Are first world countries more likely to engage, or is it more dependent on geographical locations?
- **Mexico? (Savvina)** ✅ Are there any interesting patterns involving Mexico. Are there correlations of the number of Mexican tweets and controversial statements corcerning Mexico made by the candidates. 
- **Gender identification. (Max)** ✅ Whose used twitter most during the elections, men or women? What are the differences in candidate preference and twitter behavior between men and women. 
- **Ethinicity.** Are we able to find link a users name to their ethnicity? Is there a significant difference in candidate preference when considering ethnicity? 
- **Nationwide opinion on candidates.** When analyzing the sentiment of all tweets in the data, are there interesting patterns, such as a widespread like or dislike of candidates? Does this correspond to the final aggregated votes.?
- **Visibility (Daphnee)** How visible were the candidates on twitter, i.e., what is the total number of hashtags and @'s that refer to a specific candidate. 
- **Optimists or pessimists? (Albert)** ✅  What is the total amount of positive/negative tweets?
- **Trump or Hillary? (Albert)** ✅  Is Trump or Hillary more popular on Twitter?
- **News Agencies (Elena)**. What is the percentage of tweets that originate from news agencies. How does this compare to the tweets originating from normal users. 
- **Writing style.** Is there a linguistic difference between a Pro Trump and Pro Hillary tweet. Think of sentence lengths and average amount of vowels. Can language models be used to predict whether a tweet is #withher or #maga.
- **###Hashtags. (Max)** ✅ What are the most popular hashtags? Is there a power law distribution (only a very small proportion of hashtags are very popular). Can we use these hashtags in our sentiment analysis?
- **Co-occurence network of hashtags.** ✅ Aka, which hashtags appear together? This can produce some cool networks like the one found [here](https://goo.gl/DEc875). This might also give us some insight into whether the neutral tags #Hillary and #Trump are more often used in a positive or a negative sense. 
- **Topic modelling for Hillary vs Trump.(Albert)** What are the topics that come up from Hillary vs Trump?
- **How faithful are users?** When users posts pro Hillary tweets, do they do this consistently, or do they switch teams and become pro Trump? This could give us insights into changing public opinion (see this [image](https://goo.gl/6ohaXg)). This could be due to different people joining the conversation or due to poeple changing their opinion.   
- **Emojis?** Which emojis are used most, other interesting stats.   


# Files
Tweets with sentiment analysis (Positive, Negative, Neutral) and whether they speak about trump, hillary, both or neither: [Dropbox](https://www.dropbox.com/s/n2ddj9l7m7bahen/customTweetsWithSentiment.jsons?dl=0)



# Literature
[Validation of Twitter opinion trends with national polling aggregates: Hillary Clinton vs Donald Trump](https://goo.gl/FJD73s)

[Demographic Breakdown of Twitter Users:
An analysis based on names](https://pdfs.semanticscholar.org/4d5a/8e25a3c01dd06fb31721f5550e3f8a174298.pdf)
