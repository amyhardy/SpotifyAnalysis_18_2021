"""A collection of functions for doing my project."""

from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

def random_playlist_generator(dataset):
    """
    ORIGINAL FUNCTION I ALTERED FROM A5
    TAKES IN DATAFRAME AND RETURNS SAMPLE OF 10
    IN THIS CASE, A PLAYLIST OF 10 SONGS
    """
    playlist = dataset.sample(10, replace = False)
    return playlist

def calculate_common(dataset, column):
    """ORIGINAL FUNCTION I ALTERED FROM A5 
    USING TYPE CASTING AND STRING CONCATENATION 
    SO IT TOLD US WHO HAD THE MOST AMOUNT OF SONGS
    ON THE CHART AND HOW MANY SONGS THEY HAD
    """
    val_counts = dataset[column].value_counts()
    return (str(val_counts.idxmax()) + " had the most songs on the top 200 list, with " + str(val_counts.max()) + " songs.")

def most_songs_on_chart(dataset, column):
    """
    ORIGINAL FUNCTION
    TAKES IN A DATAFRAME AND COLUMN AND CREATES A 
    BAR CHART OF THE 5 MOST COMMON COLUMN VALUES 
    AND HOW MANY VALUES THERE WERE
    """
    bar_plot = dict(Counter(dataset[column].values).most_common(5))
    plt.bar(*zip(*bar_plot.items()))
    plt.show()    
    return (Counter(dataset[column].values).most_common(5))
    
def make_autopct(values):
    """
    TAKES IN A SET OF VALUES 
    MAKES THEM DISPLAY AS THE VALUE ITSELF
    AND THE PERCENTAGE OF TOTAL VALUES
    NOT ORIGINAL CODE. FROM Stack Overflow
    """
    def my_autopct(pct):        
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d} ({p:.0f}%)'.format(p=pct,v=val)
    return my_autopct

def pie_chart(dataset, column):
    """
    ORIGINAL FUNCTION
    TAKES IN A DATAFRAME AND A COLUMN
    MAKES A PIE CHART SIMILAR TO THE BAR CHART
    """
    counts = (dataset[column].value_counts())[0:10]
    counts.plot.pie(label="", title="Top Ten Reoccuring Artists",autopct=make_autopct(counts),figsize=(7, 7))
    plt.show(block=True)
    return None

def print_top_ten(dataset):
    """ ORIGINAL FUNCTION
    TAKES IN ORDERED DATAFRAME
    RETURNS FIRST 10 
    """
    return (dataset[0:10])


def both_charts(dataset1, dataset2, column):
    """
    ORIGINAL FUNCTION
    TAKES IN TWO DATAFRAMES, COLUMN
    RETURNS A DATAFRAME OF ARTISTS
    WITH SONGS IN THE TOP 50 
    ON BOTH CHARTS
    """
    data_50top1 = dataset1[column][0:50].tolist()
    data_50top2 = dataset2[column][0:50].tolist()
    data_50top1_set = set(data_50top1)
    intersection = data_50top1_set.intersection(data_50top2)
    intersection_list = list(intersection)
    return (pd.DataFrame(intersection_list, columns=["Artists in Top 50 on Both Charts"]))


