import pandas as pd
import re

data = pd.read_excel('data/Video Games Sales.xlsx').dropna()
data.head()

### Task 1: For Loops with if statements
'''
How many Video Games were released by Nintendo?  

Loop through the publisher list and count the number of occurences.

Assign the final integer count to the variable `count`.
'''

publisher = list(data['Publisher'])

# Replace None with the appropriate value
count = None
# your code here

#__SOLUTION__
count = 0
for p in publisher:
    if p == 'Nintendo':
        count += 1
print(count)

assert count==295
print('You have the correct count for Nintendo')

### Task 2: Zipping
'''
The indices of the two lists `Publisher` and `Year` are aligned.  In other words, we could see that a video game was published by Nintendo in 2006 by running `print(publisher[0], year[0]`.

With a for loop, count how many video games were released by `Electronic Arts` in `2010`.

Use the built in `zip` method to iterate through both lists simultaneously.

'''

publisher = list(data['Publisher'])
year = list(data['Year'].astype(int))

count_ea_2010 = None

#__SOLUTION__
count_ea_2010 = 0

for p,y in zip(publisher, year):
    if p == 'Electronic Arts' and y == 2010:
        count_ea_2010+=1

assert count_ea_2010 == data[(data['Publisher']=='Electronic Arts') &
                             (data['Year']==2010)].shape[0]

print('You have the correct count for EA')

### Task 3: Strings
"""
Count how many Sonic the Hedgehog games are in the dataset.

To do so, use a for loop to see how often the string `Sonic` appears in a title.
"""

titles = list(data['Game Title'])
count = None

#__SOLUTION__
count = 0
for title in titles:
    if 'Sonic' in title:
        count+=1


pattern = '.*Sonic.*'

assert count == len(data['Game Title'][
                     data['Game Title'].apply(
                         lambda x: re.match(pattern, x)!=None)])
print('You found the correct number of Sonic the Hedgehog games')

### Task 4: Dictionaries

'''
Create a dictionary which has Publisher as keys and a second dictionary as values. The second dictionary should have genre as keys and the count of each genre as values.
'''
# Loop over these lists
genres = list(data['Genre'])
publishers = list(data['Publisher'])

publisher_genre_counts = None

#__SOLUTION__
# unique publishers
unique_publishers = set(publishers)

unique_genres = set(genres)
genre_dict = {k:0 for k in unique_genres}


publisher_genre_counts = {k:{k:0 for k in unique_genres}
                          for k in unique_publishers} 

for g, p in zip(genres, publishers):
    publisher_genre_counts[p][g] += 1

assert publisher_genre_counts['Nintendo']['Role-Playing'] == 38
assert publisher_genre_counts['Electronic Arts']['Action'] == 22
print('You have the correct counts for genres per platform')
