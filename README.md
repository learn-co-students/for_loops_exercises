
# More For Loop Practice

For this warmup, we will practice for loops by navigating a Video Games data set which is read in via the cell below.

While there may be more efficient ways to find answers to the following questions, use for loops in this notebook to solve them.

### Task 1: For Loops with if statements

How many Video Games were released by Nintendo?  

Loop through the publisher list and count the number of occurences.

Assign the final integer count to the variable `count`.



```python
count = 0
for p in publisher:
    if p == 'Nintendo':
        count += 1
```

    295


### Task 2: Zipping

The indices of the two lists `Publisher` and `Year` are aligned.  In other words, we could see that a video game was published by Nintendo in 2006 by running `print(publisher[0], year[0]`.

With a for loop, count how many video games were released by `Electronic Arts` in `2010`.

Use the built in `zip` method to iterate through both lists simultaneously.


```python
count_ea_2010 = 0

for p,y in zip(publisher, year):
    if p == 'Electronic Arts' and y == 2010:
        count_ea_2010+=1
```

### Task 3: Strings
Count how many Sonic the Hedgehog games are in the dataset.

To do so, use a for loop to see how often the string `Sonic` appears in a title.


```python
count = 0
for title in titles:
    if 'Sonic' in title:
        count+=1
```

### Task 4: Dictionaries

Create a dictionary which has Publisher as keys and a second dictionary as values. The second dictionary should have genre as keys and the count of each genre as values.



```python
# unique publishers
unique_publishers = set(publishers)

unique_genres = set(genres)
genre_dict = {k:0 for k in unique_genres}


publisher_genre_counts = {k:{k:0 for k in unique_genres}
                          for k in unique_publishers} 

for g, p in zip(genres, publishers):
    publisher_genre_counts[p][g] += 1
```
