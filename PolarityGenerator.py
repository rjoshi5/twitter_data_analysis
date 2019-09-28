# Python program for Sentiment Analysis from csv file

# importing all necessery modules
from textblob import TextBlob	
import sys
import matplotlib.pyplot as plt
import csv
import pandas

# Calculation of Polarity %
def percentage(part, whole):
	return(100 * (float(part)/float(whole)))

# Initiation of vars
positive=0
negative=0
neutral=0
polarity=0
totalTweets=0


# Open csv file, read each row and execute the polarity
with open('tweets_facebook_append.csv', encoding="utf8") as csv_file:
	row_reader=csv.reader(csv_file)
		
	for row in row_reader:
		row = str([cell.encode('utf-8') for cell in row])
		analysis = TextBlob(row)
		print(analysis)

		# polartity for each row
		row_polarity = analysis.sentiment.polarity			
		totalTweets += 1

		# counting the tweets in the file
		print('value of total keywords is:', totalTweets)
		print(row_polarity)

		# counting neutral tweets
		if (analysis.sentiment.polarity ==0):		
			neutral +=1

		# counting negative tweets
		elif (analysis.sentiment.polarity < 0.00):		
			negative += 1

		# counting positive tweets
		elif (analysis.sentiment.polarity > 0.00):		
			positive +=1


# Calculation of Polarity percentage			
			
positive = percentage(positive, totalTweets)
negative = percentage(negative, totalTweets)
neutral = percentage(neutral, totalTweets)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print('value of total positive is:', positive)
print('value of total negative is:', negative)
print('value of total neutral is:', neutral)

if (row_polarity == 0):
	print("Neutral")
elif (row_polarity < 0):
	print("Negative")
elif (row_polarity > 0):
	print("Positive")

# Building the pie chart for visualization

labels = ['Positive ['+str(positive)+'%]','Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%']
sizes = [positive, neutral, negative]
colors = ['yellowgreen','green','red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on the breach by analyzing ' + str(totalTweets) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()