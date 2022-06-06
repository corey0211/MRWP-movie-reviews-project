# MRWP-movie-reviews-project
This project builds mainly on the Amazon Movie Reviews dataset to create a network of movie co-reviews ("co-liking") and applies the Louvain clustering algorithm in order to investigate whether movie communitites correspond roughly to genre. 
The main contribution of this project is thus to the field of recommender systems mostly studied from a machine learning perspective (and based on social sciences knowledge) in order to allow for a better understanding and thus improvement of those systems through a network science lens.

# File Overview
In order to start interacting with this project, make sure all frameworks from 'requirements.txt' are installed. 

## Main files
The three main code files, which should be run in this exact order are: 
1. Group Project MRWP.ipynb
2. network creation.ipynb
3. Percentages.ipynb

For more information on each file see below.

## Additional files
- 1%SampleDataset.csv: 1% of the preprocessed data (for testing purpose)
- 10%Dataset.csv: 10% of the preprocessed data used subsequently in network creation.ipynb and Percentages.ipynb
- All _genre_ categories excel format.xlsx: manual overview of all movie categories
- MRWP Final Project.pptx: presentation slides
- SampleNetwork.csv:sample network using the 1%SampleDataset.csv (for testing purpose)
- 10%Network.csv: [https://drive.google.com/file/d/1tlq_Wsc-UE8_s-w8P19AXXaSCV75Mron/view?usp=sharing]: link to download 10%Network.csv to be able to run the Percentages.ipynb file quickly (instead of needing to run both other main files which are quite time consuming)(1)

## Datasets
### Amazon Movie Reviews
This is the main dataset and should be downloaded to \MRWP-movie-reviews-project-main from [https://snap.stanford.edu/data/web-Movies.html].
### Labels on Amazon Movie Reviews Dataset
The "labels.csv" file is the additional dataset containing the movies and their associated categories 

## Additional Information
In general, using the 10%Network.csv and 10%Dataset.csv file found under "Additional files", the first two main files (Group Project MRWP.ipynb
and network creation.ipynb) do not need to be run for getting the results of this project, computed by Percentages.ipynb.

### file Group Project MRWP.ipynb
To run the 'Group Project MRWP.ipynb' it is required to download the Amazon Movie Reviews dataset as described above. 

The main aim of this file is to preprocess the data for the network building and percentage analysis.

Throughout the process, four files are saved seperately in order to be able to run the two following main files independently: 'PositiveReviews.csv', 'CompleteDataWithGenres.csv', '1%SampleDataset.csv', '10%Dataset.csv'. 

#### For more detail : the file is divided into 10 steps:
1. "processing the Main Dataset": the dataset is read and the information is reorganized 
2. "getting the Reviews": the useless information is filtered out and list of lists (reviews) is created
3. "Exploring the Data": data exploration and removing "bad reviews"
4. "Reading the dataset into a Dataframe": a dataframe (df) with all information is created 
5. "the Final Dataframe": some more general information and saving the file 'PositiveReviews.csv' 
6. "Prepare the Dataset with the Categories": the file "labels.csv" gets read in and cleaned of empty categories, non-movies
7. "Towards Merging the Information of both Datasets": remove non-overlapping movies and merge dataframes
8. "Saving the Data for Easier Accessibility": data saved to 'CompleteDataWithGenres.csv' and save 1% sample '1%SampleDataset.csv'
9. "Reducting the Dataset Size by Genre": text mining to re-format categories, defining some genres and removing accordingly movies, save as '10%Dataset.csv'
10. "Dictionary with Movie as Key and Genre as Value": a dictionary called 'with product id and corresponding genre 

### file Network Creation.ipynb
This file mainly aims at building the Network of co-reviews.

This file requires the previously saved '10%Dataset.csv' and SampleDataset.csv" (for testing) files from Group Project MRWP.ipynb

This code creates a network of nodes ('Movie') with edges which are weighted based on how many amazon users positively reviewed both of the the 2 movies which are connected by said edge. 

Nota Bene: the network creation algorithm is of quadratic order and thus takes quite some time to run, although the outter for-loop loops over the entire dataframe and the inner for-loop only runs over the amount of reviews per user and the size of the inner for-loop decreases in size with each iteration of the outter for-loop the rendering still is slow. 

1% data takes minutes to render, 10% of the data (the 10%Network producted) takes hours and 100% of the data takes days (on our particular device).

#### For more detail: important cells
- In the 5th cell a test is done with a made up dataframe of 10 movies. It can be easily confirmed the resulting network corresponds to the dataframe input.
- In the 6th cell a network is rendered based on the 1% sample dataset and saved as 'SampleNetwork.csv'. 
- In the 7th cell the same thing is done for the 10%dataset and the network is saved as '10%Network.csv'.

### file Percentages.ipynb
This file mainly aims at performing the clustering of movies and subsequently render the percentage of genre majority movie clusters.

This file requires the 10%Network.csv' and the "10%Dataset.csv". The Louvain algorithm is imported from the python_louvain module, using the 'community' library.

The final results of our project can be found under "Final Project Results - Percentage of Movie Clusters with Genre Majority".
