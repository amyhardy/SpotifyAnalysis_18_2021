"""Test for my functions.
"""

from functions import calculate_unique, random_playlist_generator, calculate_common, most_songs_on_chart, make_autopct, pie_chart, print_top_ten


  
def test_calculate_unique():
    
    assert callable(calculate_unique)

def random_playlist_generator():
    
    assert callable(random_playlist_generator)

def test_calculate_common():
    """
    I REFERED TO LECTURE17 FOR THIS TEST
    """
    assert callable(calculate_common)
    test_df = pd.DataFrame({'ID' : [1, 2, 3], 
                        'response' : ['a', 'a', 'b']})
    assert isinstance(calculate_common(test_df, 'response'), str)
       
def test_most_songs_on_chart():
    """
    I REFERED TO LECTURE17 FOR THIS TEST
    """
    assert callable(most_songs_on_chart)
    test_df = pd.DataFrame({'ID' : [1, 2, 3], 
                    'response' : ['a', 'a', 'b']})
    assert isinstance(most_songs_on_chart(test_df, 'response'), list)   

def test_make_autopct():
    
    assert callable(make_autopct)
    
def test_pie_chart():
    
    assert callable(pie_chart)

def test_print_top_ten():
    
    assert callable(print_top_ten)

  