# Importing the modules
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

 #title:
st.title('Movie recommender system')

# Loading data
movies_data = pd.read_csv(r'C:\Users\Rashi\OneDrive\Desktop\PROJECT-01\tmdb_5000_movies.csv')
bollywood_movies_data= pd.read_csv(r'C:\Users\Rashi\OneDrive\Desktop\PROJECT-01\IMDB-Movie-Dataset(2023-1951).csv')

for col in movies_data.columns:
    if col not in bollywood_movies_data.columns:
        bollywood_movies_data[col] = None  
        
bollywood_movies_data = bollywood_movies_data[movies_data.columns]

#concatenating both the datasets.
combined_data = pd.concat([movies_data, bollywood_movies_data], ignore_index=True)

        
# # Show basic info
# print(combined_data.head())
# print(combined_data.columns)  
# //you can view the columns in the output terminal if you wish to, by un-commenting this part. 


# Check columns — useful ones: 'genres', 'tagline', 'title', 'overview'
# Fill missing values
features = ['genres', 'tagline', 'overview', 'title']
for feature in features:
    combined_data[feature] = combined_data[feature].fillna('').astype(str)
   
    
    

# Combine features into one string
combined_data['combined_features'] = (combined_data['genres'] + ' ' + combined_data['tagline'] + ' ' + combined_data['overview']+ ' '+ combined_data['title'])
combined_data['combined_features'] = combined_data['combined_features'].astype(str)



# Convert text to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform( combined_data['combined_features'])

# Compute cosine similarity
similarity = cosine_similarity(feature_vectors)

# Get user input
movie_name = st.text_input("Enter a movie name: ")

# Get list of all movie titles
list_of_all_titles = combined_data['title'].tolist()

# Find closest match
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print("Close matches:", find_close_match)

if find_close_match:
    close_match = find_close_match[0]

    # Get index of the movie with title
    index_of_movie = combined_data[combined_data.title == close_match].index[0]

    # Get similarity scores
    similarity_score = list(enumerate(similarity[index_of_movie]))

    # Sort similar movies
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    st.subheader("\nMovies suggested for you:\n")

    i = 0
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = combined_data[combined_data.index == index]['title'].values[0]
        if i < 30:
            st.write(i, '.', title_from_index)
            i += 1
        else:
            break
    if i==0:    
        st.write("Sorry, no close match found.")
