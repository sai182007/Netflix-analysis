# final project:-

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df=pd.read_csv('m11/netflix_titles.csv')

# cleaning the data
# print(df.info()) 
df.dropna(subset=["type","release_year","rating","country","duration"],inplace=True,ignore_index=True)
# print(df.info()) 
# print(df.isnull().sum())

types=df['type'].value_counts()
plt.figure(figsize=(8,5))
plt.bar(types.index,types.values,color=['red','orange'],width=0.3)
plt.title('Distribution of Content Types on Netflix')
plt.xlabel('Content Type')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.savefig('m11/netflix_content_types.png')
plt.show()


ratings=df['rating'].value_counts()
top_ratingd=ratings[:6]
others=pd.Series([ratings[6:].sum()],index=['Others'])
ratings_mod=pd.concat([top_ratingd,others])
plt.figure(figsize=(8,5))
plt.pie(ratings_mod,labels=ratings_mod.index,autopct='%1.1f%%',startangle=90,colors=plt.cm.Paired.colors)
plt.title('Percentage Distribution of Content Ratings on Netflix')
plt.tight_layout()
plt.savefig('m11/netflix_content_rating.png')
plt.show()


release_years=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.plot(release_years.index,release_years.values,marker='o',color='blue')
plt.title('Number of Titles Released Each Year on Netflix')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.grid()
plt.tight_layout()
plt.savefig('m11/netflix_release_years.png')
plt.show()


movie_durations=df[df['type']=='Movie'].copy()
movie_durations['duration_int']=movie_durations['duration'].str.replace('min','').astype(int)
plt.figure(figsize=(10,6))
plt.hist(movie_durations['duration_int'],bins=30,color='yellow',edgecolor='black')
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('m11/netflix_movie_durations.png')
plt.show()


countries=df['country'].value_counts().head(10)
plt.figure(figsize=(10,6))
plt.bar(countries.index,countries.values,color=plt.cm.viridis.colors)
plt.title('Top 10 Countries by Number of Titles on Netflix')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('m11/netflix_top_countries.png')
plt.show()


content_by_year=df.groupby(['release_year','type']).size().unstack().fillna(0)

fig,ax=plt.subplots(1,2,figsize=(14,6))

ax[0].plot(content_by_year.index,content_by_year['Movie'],marker='o',color='blue')
ax[0].set_title('Number of Movies Released Each Year on Netflix')
ax[0].set_xlabel('Release Year')
ax[0].set_ylabel('Number of Movies')
ax[0].grid()

ax[1].plot(content_by_year.index,content_by_year['TV Show'],marker='o',color='green')
ax[1].set_title('Number of TV Shows Released Each Year on Netflix')
ax[1].set_xlabel('Release Year')
ax[1].set_ylabel('Number of TV Shows')
ax[1].grid()

plt.tight_layout()
plt.savefig('m11/netflix_content_trends.png')
plt.show()


top_directors = df['director'].value_counts().head(10)

plt.figure(figsize=(10,6))
bars = plt.bar(top_directors.index, top_directors.values, color='teal')
plt.xticks(rotation=45)
plt.title('Top 10 Directors on Netflix')
plt.xlabel('Director')
plt.ylabel('Number of Titles')
plt.bar_label(bars, padding=3)
plt.tight_layout()
plt.savefig('m11/netflix_top_directors.png')
plt.show()
