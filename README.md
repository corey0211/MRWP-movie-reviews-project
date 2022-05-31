# MRWP-movie-reviews-project
This project takes a dataset of amazon movie reviews and utilizing a network and clustering algorithms. it explores which subnetworks of movies have high clustering coefficients. it also identifies movie genres utilizing a dataset of [xxx] this can be used to find which movie genres are enjoyed by the same people. 
[motivation]
the purpose of this project is to create a better understanding of how different movie genres are related from a consumers perspective. This knowledge can be used in order to improve movie reccomendations and create a general better understanding of movie audiance tastes. 
In order to start interacting with this project, make sure all frameworks from 'requirements.txt' are installed. 
a brief overview of what the code does: 
the file 'Group Project MRWP.ipynb' takes the file <<>>> and processes the data and creates the file 'PositiveReviews.csv', 'CompleteDataWithGenres.csv', '1%SampleDataset.csv', '10%Dataset.csv'
in the first section named "processing the Main Dataset" the file 'movies.txt' is read and the information is reorganized. When you run cell 4 you can see how the information of one review is organized in the 'movies.txt' file
in the second section called "getting the Reviews" the usefull information is filtered out (nammely, productId, userId and score) and saved as a list of list.
in the section "Exploring the Data" the reviews are counted and the dataset filtered out more
in "Reading the dataset into a Dataframe" a dataframe is created with columns called "Movie", "User" 

