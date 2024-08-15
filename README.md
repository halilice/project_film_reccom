# The Movie Recommendation System
## by Halil Ibrahim Celikel and Mai Tran

![Movies](https://www.reliancedigital.in/wp-content/uploads/2019/02/netflix_movies_cover.jpg)


## Summary of the Project

This is a project I implemented with my classmate Mai Tran at Wild Code School, where i learnt to become a data analyst. Our target is to create the  MRF - Movie Recommendation System which will recommend similar titles to user's given title according to Genres, popularity, Duration, etc. 
We started with 10.73 millions titles that we explored to understand the content of all the given datasets. We filtered to down-size into a dataset of 450k titles. We then clean and remove missing values to get a final one with 430k titles.

![The funnel](home_page_filtering.png)

About the creation of the recommendation system, we first convert all the text values into numeric values by using LabelEncoder for column 'Type' and method which converted each category of column 'Genres' into a label with binary values.
Since this is a non-supervised model, we passed the step 'model traing' by going directly to the prediction of NearestNeighbors, an unsupervised learner for implementing neighbor searches.
We then tried to change the hyperparameter to get our model better but we dont' see much improvement so we sorted values by setting the weight on Votes and Genres.

![The Feature Engineering](home2.png)

## Files of the project

~~~~~
- poster.csv : Contains the links of the film posters.
- return_movies.csv : Contains the data of the project.
- ml.py : Contains the codes of the research.
- requirements.txt : Contains the versions of the modules used for the project. I have to add this file to publish it on streamlit.
- 
~~~~~

The link of streamlit page of the project: '[https://carsanalysis-app-egpuskxsb4ivhqrrddm8at.streamlit.app/](https://projectfilmreccom-dk3ib5yqhynkce3bc6igfd.streamlit.app/)'
