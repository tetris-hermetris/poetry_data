# Data on poetic and non-poetic fields

```python
from poetry_data.data import getData

# all the data can be accessed
# through the same function and
# structured with the same way

poetry = getData("poetry")
moon = getData("moon")
fireballs = getData("fireballs")
```

## Poetry Dataset

The main part of the collected data contains 10,354 publications (as of 12/05/2023), gathered from Russian (and partly Ukrainian) poetry telegram channels:

1. [метажурнал](https://t.me/metajournal)
2. [поэты первой необходимости](https://t.me/essentialpoetry)
3. [стихотворение не реже раза в неделю](https://t.me/nerejeraza)
4. [вот белены напиток выпей](https://t.me/votbnv)
5. [негромкие стихи](https://t.me/quite_poetry)

At a higher level, it is a list of dictionaries (one per post).

Each entry (publication or post) has 4 keys:

- **"author"** _— author of the text_
- **"date"** _— date of publication in the channel_
- **"channel"** _— telegram adress_
- **"text"** _— text of the publication_

```python
print(poetry[12]["author"])
print(poetry[12]["text"])
print(poetry[12]["channel"])
print(poetry[12]["date"])

# Андрей Гришаев
# * * *
# 
# Не горит ли дом
# Не дымит ли печь
# Не течет ли течь
# Не нейдет ли сон
# Не идет ли сын
# Не стучат ли в дверь
# 
# Мне напрасен дом
# Мне напрасно лечь
# Мне опасна речь
# Мне не сладок сон
# Мне бессилен сын
# Мне не вечен зверь
# 
# Но над всем она
# Над грозой она
# Над чумой она
# Над стеной она
# Над зимой она
# Над землей она
# 
# Вечная весна
# Вечная весна
# Вечная весна
# Вечная весна
# Вечная весна
# Вечная весна
# 
# 09.11.2023
# 
# Источник: авторский блог
# metajournal
# 2023-11-19 16:36:23+00:00
```

## Background Data

Consists of two additional datasets, linked to publications through dates.

### Moon Phases

At a higher level, it is a list of dictionaries, as in the poetry dataset. Each dictionary contains two keys:

- **"date"** _— with dates for every post in the poetry set_
- **"phase"** _— with moon phase from 0.0 to 1.0_

### Fireballs

The second background dataset is collected data on [fireballs (or bolides)](https://cneos.jpl.nasa.gov/fireballs/intro.html), gathered through the NASA CNEOS API.

Like the other data in this repo, it's structured as a list of dictionaries. The keys are:

- **"date"** _— date/time of peak brightness (GMT)_
- **"energy"** _— approximate total radiated energy (1010 joules)_
- **"impact-e"** _— approximate total impact energy (kt)_
- **"lat"** _— latitude at peak brightness (degrees)_
- **"lat-dir"** _— latitude direction (“N” or “S”)_
- **"lon"** _— longitude at peak brightness (degrees)_
- **"lon-dir"** _— latitude direction (“E” or “W”)_
- **"alt"** _— altitude above the geoid at peak brightness (km)_
- **"vel"** _— velocity at peak brightness (km/s)_

**"date"**, **"energy"**, and **"impact-e"** should be present in all entries. The other keys may sometimes be None due to a lack of scientific observations. Also, note that sometimes posts were published on days when no fireballs were observed on Earth, so this dataset should be used with checks via if-conditions.