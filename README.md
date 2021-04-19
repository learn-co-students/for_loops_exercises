
# More For Loop Practice

For this warmup, we will practice for loops by navigating a Video Games data set which is read in via the cell below.


```python
# Run without changes
import pandas as pd

data = pd.read_excel('data/Video Games Sales.xlsx').dropna()
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Game Title</th>
      <th>Platform</th>
      <th>Year</th>
      <th>Genre</th>
      <th>Publisher</th>
      <th>North America</th>
      <th>Europe</th>
      <th>Japan</th>
      <th>Rest of World</th>
      <th>Global</th>
      <th>Review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Wii Sports</td>
      <td>Wii</td>
      <td>2006.0</td>
      <td>Sports</td>
      <td>Nintendo</td>
      <td>40.43</td>
      <td>28.39</td>
      <td>3.77</td>
      <td>8.54</td>
      <td>81.12</td>
      <td>76.28</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Super Mario Bros.</td>
      <td>NES</td>
      <td>1985.0</td>
      <td>Platform</td>
      <td>Nintendo</td>
      <td>29.08</td>
      <td>3.58</td>
      <td>6.81</td>
      <td>0.77</td>
      <td>40.24</td>
      <td>91.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Mario Kart Wii</td>
      <td>Wii</td>
      <td>2008.0</td>
      <td>Racing</td>
      <td>Nintendo</td>
      <td>14.50</td>
      <td>12.22</td>
      <td>3.63</td>
      <td>3.21</td>
      <td>33.55</td>
      <td>82.07</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Wii Sports Resort</td>
      <td>Wii</td>
      <td>2009.0</td>
      <td>Sports</td>
      <td>Nintendo</td>
      <td>14.82</td>
      <td>10.51</td>
      <td>3.18</td>
      <td>3.01</td>
      <td>31.52</td>
      <td>82.65</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Tetris</td>
      <td>GB</td>
      <td>1989.0</td>
      <td>Puzzle</td>
      <td>Nintendo</td>
      <td>23.20</td>
      <td>2.26</td>
      <td>4.22</td>
      <td>0.58</td>
      <td>30.26</td>
      <td>88.00</td>
    </tr>
  </tbody>
</table>
</div>



While there may be more efficient ways to find answers to the following questions, use for loops in this notebook to solve them.

### Task 1: For Loops with if statements

How many Video Games were released by Nintendo?  

Loop through the publisher list and count the number of occurences.

Assign the final integer count to the variable `count`.



```python
publisher = list(data['Publisher'])

# Replace None with the appropriate value
count = None
# your code here
```


```python
# Run cell with no changes
assert count == data['Publisher'].value_counts()['Nintendo']
print('Correct')
```

    Correct


### Task 2: Zipping

The indices of the two lists `Publisher` and `Year` are aligned.  In other words, we could see that a video game was published by Nintendo in 2006 by running `print(publisher[0], year[0]`.

With a for loop, count how many video games were released by `Electronic Arts` in `2010`.

Use the built in `zip` method to iterate through both lists simultaneously.


```python
# Run cell without changes
publisher = list(data['Publisher'])
year = list(data['Year'].astype(int))
```


```python
# Replace None with the appropriate value
count_ea_2010 = None

# your code here
```


```python
# Run cell with no changes
assert count_ea_2010 == data[(data['Publisher']=='Electronic Arts') & (data['Year']==2010)].shape[0]
print('You have the correct count for EA')
```

    You have the correct count for EA


### Task 3: Strings
Count how many Sonic the Hedgehog games are in the dataset.

To do so, use a for loop to see how often the string `Sonic` appears in a title.


```python
# Run cell with no changes
titles = list(data['Game Title'])
```


```python
# Run cell with no changes
import re
pattern = '.*Sonic.*'

assert count == len(data['Game Title'][
                     data['Game Title'].apply(
                         lambda x: re.match(pattern, x)!=None)])
print('You found the correct number of Sonic the Hedgehog games')

```

    You found the correct number of Sonic the Hedgehog games


### Task 4: Dictionaries

Create a dictionary which has Publisher as keys and a second dictionary as values. The second dictionary should have genre as keys and the count of each genre as values.



```python
# Run cell with no changes

# Loop over these lists
genres = list(data['Genre'])
publishers = list(data['Publisher'])


```


```python
# Replace None with the appropriate value

publisher_genre_counts = None

# your code here

```


```python
assert publisher_genre_counts['Nintendo']['Role-Playing'] == 38
assert publisher_genre_counts['Electronic Arts']['Action'] == 22
print('You have the correct counts for genres per platform')
```

    You have the correct counts for genres per platform

