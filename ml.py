# importing package

import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors


def get_recom():
    # User's input
    st.title(":blue[Now, it's time for our favorite movies.]")

    st.header(":blue[Please enter a title]")

    title = st.text_input("Movie title", "The Avengers")
    st.write("The current movie title is", title)

    # Importing datasets
    poster = pd.read_csv(r"poster.csv")
    df_return = pd.read_csv(r"return_movies.csv")

    # Combining 2 datasets
    df_return = pd.concat([df_return, poster], axis=1)
   
    # Sorting values for puting weights on selected variables
    df_return = df_return.sort_values(['Type of title', 'Released year',                         
                         'Average Ratings', 'Duration', 'Votes'], 
                        ascending=[
                            True, False,                     
                            True, False, True
                            ] )
    
   # Copy and nomalize all variables for model
    df = df_return.copy()
   

    # Convert genres to list of strings
    df['Genres'] = df['Genres'].str.split(',')

    # Create numeric label for each category of genres
    genres_cat = ['Action', 'Adventure', 'Animation', 'Biography','Comedy', 
                 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 
                 'Horror','Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
                 'Music', 'History', 'War', 'Western', 'Musical']

    for i in genres_cat:
        df[i] = df['Genres'].apply(lambda x:1 if i in x else 0)


    # Create numeric label for each category of titleType
    label_encoder = LabelEncoder()
    df['Type of title'] = label_encoder.fit_transform(df['Type of title'])

    # Drop non-selected columns
    df = df.drop(columns=['Genres'], axis = 1)
    # Lower the title's names
    df['Title']= df['Title'].apply(lambda x: x.lower())

    # Change position of all variables
    df = df[[
                 'Title', 
                  'Type of title',
                 'Action', 'Adventure', 'Animation', 'Biography','Comedy', 
                 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 
                 'Horror','Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
                 'Music', 'History', 'War', 'Western', 'Musical',
                 'Votes', 'Average Ratings', 'Adult title', 'Released year', 'Duration',
                 
                 ]]



    # Set title as index
    df = df.set_index('Title')
    
    df = df.sort_values(['Type of title', 'Released year',                         
                         'Average Ratings', 'Duration', 'Votes'], 
                        ascending=[
                            True, False,                     
                            True, False, True
                            ] )
    
    
    # Initialize variable X
    X = df.select_dtypes("number")

    # Standardize features of X
    scaler = StandardScaler()
    scaler.fit(X)

    X_scaled = pd.DataFrame(scaler.transform(X), index=X.index, columns=X.columns)

    
    # Lower title's name
    title = title.lower()
    
    # To identify the searching film
    # Scale searching value
    input_title_scaled = X_scaled.loc[title].to_frame().T
    
    # Show the KPI of serching film to compare with returned values
    #input_title = X.loc[title].to_frame().T
    


    # Fit model
    modelKNN = NearestNeighbors(n_neighbors=5)
    modelKNN.fit(X_scaled)

    # Identify distance and indeices of similar films
    neigh_dist, neigh_film = modelKNN.kneighbors(input_title_scaled, n_neighbors=11)
    film_similar = neigh_film[0][1:]
    user_film = neigh_film[0][:1]

     # Create df of searched and returned titles

    web_path = "https://image.tmdb.org/t/p/original"

    st.header(":blue[Your favorite title:]")
    search = df_return.iloc[user_film]
    search_poster_path = search["poster_path"].to_string(index=False)
       
    

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(web_path + search_poster_path, width=230)

    with col2:
        st.write(search.to_string(columns=["Title"], header=False, index=False))
        st.write("Released year:", search.to_string(columns=["Released year"], header=False, index=False))
        st.write("Votes:", search.to_string(columns=[ "Votes"], header=False, index=False))
        st.write("Ratings:",search.to_string(columns=["Average Ratings"], header=False, index=False))
        st.write("Duration:",search.to_string(columns=["Duration"], header=False, index=False))
        st.write(search.to_string(columns=["Genres"], header=False, index=False))

    st.header(":blue[We would like to recommend you 10 similar titles below. Hope you will enjoy them!]")
    recom = df_return.iloc[film_similar]
    recom_poster_path = recom["poster_path"].to_string(index=False)
    
    # Loop to return each title

    

    for i, row in recom.iterrows():
        recom_poster_path = row["poster_path"]

        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.image(web_path + recom_poster_path, width=230)

        with col2:
            st.write(row["Title"])
            st.write("Released year:", str(row["Released year"]))
            st.write("Votes:", str(row["Votes"]))
            st.write("Ratings:", str(row["Average Ratings"]))
            st.write("Duration:", str(row["Duration"]))
            st.write(row["Genres"])


get_recom()
   

   
