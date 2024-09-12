# The Movie Recommendation System
## by Halil Ibrahim Celikel and Mai Tran

![Movies](https://www.reliancedigital.in/wp-content/uploads/2019/02/netflix_movies_cover.jpg)


## Summary of the Project

This is a project I implemented with my classmate Mai Tran at Wild Code School, where i learnt to become a data analyst. Our target is to create the  MRF - Movie Recommendation System which will recommend similar titles to user's given title according to Genres, popularity, Duration, etc.
There were 10.73 million titles in the dataset that we explored. After cleaning, removing missing values and filtering with criterias that we chose, we got a dataset of 430k titles.  

![The funnel](photos/home_page_filtering.png)

About the creation of the recommendation system, we first convert all the text values into numeric values by using LabelEncoder for column 'Type' and method which converted each category of column 'Genres' into a label with binary values.
Since this is a non-supervised model, we passed the step 'model traning' by going directly to the prediction of NearestNeighbors, an unsupervised machine learning model for implementing neighbor searches.
We then tried to change the hyperparameter to get our model better but we didn't see much improvement so we sorted values by setting the weight on Votes and Genres.

![The Feature Engineering](photos/home2.png)

## The dataset of the project

We used the files in the following link:

https://datasets.imdbws.com/

## Dashboard of the Project

We created a dashboard on Tableau Public Software which explains the content of the seven datasets of the project. The screenshots of the dashboard are as follows:

***1. Home Page***

![Home Page](photos/Home_Page.png)

***2. Basic Indicators***

![Basic Ind.](photos/Basic_Indicators.png)

***3. The Crew Analysis***

![The crew](photos/The_crew_analysis.png)

***4. The Movies List***

![The movies](photos/The_Movie_Analysis.png)

The link of dashboard of the project : 'https://public.tableau.com/app/profile/halil.ibrahim.celikel/viz/Projet2_tableau/Pagedaccueil'

## Streamlit application

We've created a streamlit application in which users can type in their favorite movie, and which recommends 10 similar movies based on users' entry. I am adding the screenshots of the application here:

![The entry](photos/The_Movie_Analysis.png)

![The recommendation](photos/The_Movie_Analysis.png)

## Files of the project

~~~~~
- poster.csv : Contains the links of the film posters.
- return_movies.csv : Contains the data of the project.
- ml.py : Contains the codes of the research.
- requirements.txt : Contains the versions of the modules used for the project. I have to add this file to publish it on streamlit.
- 
~~~~~

The link of streamlit page of the recommendation system: '(https://projectfilmreccom-dk3ib5yqhynkce3bc6igfd.streamlit.app/)'

