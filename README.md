This project is a content-based movie recommendation system that suggests movies similar to a user’s input based on textual metadata.
The system uses Natural Language Processing (NLP) techniques to analyze movie information and recommend relevant movies.

An interactive Streamlit web application allows users to search for a movie and instantly receive recommendations.

Features:

a)Content-based movie recommendations using TF-IDF and cosine similarity
b)Uses movie metadata such as genres, overview, tagline, and title
c)Supports movies from multiple datasets (Hollywood and Bollywood)
d)Handles approximate user input using string matching
e)Interactive and user-friendly Streamlit interface

How It Works:

a)Movie metadata is cleaned and combined into a single text feature
b)Text data is converted into numerical vectors using TF-IDF Vectorization
c)Cosine similarity is used to compute similarity between movies
d)Based on the user’s input movie, the system recommends the most similar movies

Dataset:

1) TMDB 5000 Movies Dataset
2) IMDB Movies Dataset (Bollywood)
The datasets are combined and aligned to ensure consistent feature usage.

Technologies Used

Programming Language: 
* Python
* Libraries & Frameworks:
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* NLP Techniques:
* TF-IDF Vectorization
* Cosine Similarity

Utilities:
difflib (for approximate string matching)

