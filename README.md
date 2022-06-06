# MRWP-movie-reviews-project
This project builds mainly on the Amazon Movie Reviews dataset to create a network of movie co-reviews ("co-liking") and applies the Louvain clustering algorithm in order to investigate whether movie communitites correspond roughly to genre. 
The main contribution of this project is thus to the field of recommender systems mostly studied from a machine learning perspective (and based on social sciences knowledge) in order to allow for a better understanding and thus improvement of those systems through a network science lens.
In order to start interacting with this project, make sure all frameworks from 'requirements.txt' are installed. 
The three main code files are: 
- Group Project MRWP.ipynb
- network creation.ipynb
- Percentages.ipynb

and should be run in this exact order. For more information on each file see below.

### file Group Project MRWP.ipynb
The file 'Group Project MRWP.ipynb' takes the file <<>>> and processes the data and creates the file 'PositiveReviews.csv', 'CompleteDataWithGenres.csv', '1%SampleDataset.csv', '10%Dataset.csv'. 
If all of these files are present in your folder and you do not wish to change any parameters or use this code for your own project you can skip to the next section.
What the code does:
In the first section named "processing the Main Dataset" the file 'movies.txt' is read and the information is reorganized. 
When you run cell 4 you can see how the information of one review is organized in the 'movies.txt' file

In the second section called "getting the Reviews" the usefull information is filtered out (nammely, productId, userId and score) and saved as a list of list.

In the section "Exploring the Data" the reviews are counted and the dataset filtered out more

In the section "Reading the dataset into a Dataframe" a dataframe (df) is created with columns called "Movie", "User" and "Score" a visualization of the dataframe can also be found here. 

In the section "the Final Dataframe" some general information on the dataframe thusfar can be found and the dataframe so far gets saved in the file 'PositiveReviews.csv' which did not get used in the end.

In the section "Prepare the Dataset with the Categories" the file "labels.csv" gets read in, this is a dataframe with columns "Movie" (which is the amazon productId) and "Category". 
This dataframe get's cleaned by removing all empty category rows, removing all non-movies and changing the format of the categories.

In the section "Towards Merging the Information of both Datasets" first all movies which are in the categories dataset but not in our main dataframe get removed and then the dataframes get merged.

In the section "Saving thhe Data for Easier Accessibility" the dataframe that was just created gets saved to 'CompleteDataWithGenres.csv'. 
From the same dataframe a fraction of 0.01 gets saved as '1%SampleDataset.csv'

In the section "Reducting the Dataset Size by Genre" the categories are reformatted and A list of the most common categories is created in 8th cell of this subsection. 
In order to investigate different genres change the 'defined_genres' in the 9th cell, for our project and findings however don't make any changes. 
At the end of this section the dataframe containing only the chosen genres is saved as '10%Dataset.csv'.

In "Dictionary with Movie as Key and Genre as Value" a dictionary called 'dict_mvs_genre' is created with product id as input and genre as output. 
Only movies from the 10%Dataset are included in this. 


### file Network Creation.ipynb
The file 'Network Creation' takes the files "SampleDataset.csv" and "10%Dataset.csv" as imput. 
If either of these files are missing from you zip or you want to adjust the genres for your own project make sure you run 'Group Project MRWP.ipynb' first. 
Much like the previous code, this code does not need to be run unless you want to use this for your own project or a different implementation. 
If this is not the case you can move on to the next section.

What the code does: 
This code is able to create a network of nodes ('Movie') with edges which are weighted based on how many amazon users positiely reviewed bothof the the 2 movies which are connected by said edge. 
In the 5th cell a test is done with a made up dataframe of 10 movies. 
It can be easily confirmed the resulting network corresponds to the dataframe input.
In the 6th cell a network is rendered based on the 1% sample dataset and saved as 'SampleNetwork.csv'. 
In the 7th cell the same thing is done for the 10%dataset and the network is saved as '10%Network.csv'.
Important to note if you do desire to run the code again is that the rendering is of quadratic order. 
Although the outter for-loop loops over the entire dataframe and the inner for-loop only runs over the amount of reviews per user and the size of the inner for-loop decreases in size with each iteration of the outter for-loop the rendering still is slow. 
1% data takes minutes to render, 10% of the data takes hours and 100% of the data takes days (on our particular device).

### file Percentages.ipynb
in the file "Percentages.ipynb" the file '10%Network.csv' is imported and the louvain algorithm from the 'community' library is used in oder to identify clusters of movies which were enjoyed together. 
when you are only interested in seeing our results you should scroll down all the way to the section which says "Results for the Percentages in dataframe" 
if you go the route of observing different genres than the ones we have chosen you need to change the cells in the section called "Ratio of partitions corresponding to each genre" and replace each genre with one you've chosen. 
[go more into detail and if it's added talk about the graph drawing]
