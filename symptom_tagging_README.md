
This module includes 2 functions:

    - Firtst one takes in a data frame and processes the sentences in each row 
    and splits them into one word per row and then tags them with b-sym 
    if it is a beginning of a symptom and i-sym if the word is continuing part of the b-sym
   

This code took a while to correctly implement it thus, please use the alternative code below for sanity checking when in doubt. 



#### This part of the code is for sanity checking on our sentences that contain multi word symptoms. 

    Firts extract only the symptoms with multi words
    Then use our pattern to check which sentences have multi word symptoms presents
    Export them to csv file, if needed
    
Extract the list of multi symptom words
      
    multi_word_symptoms = ([symptom for symptom in symptoms if len(symptom.split())>1])

pattern to check for words that have space before and after 
this is to prevent our search from getting distracted by words like 'Statistics' when we are
looking for 'tic' which is a problem that I encountered.

    pattern_multi = '\\b' + '\\b|\\b'.join(multi_word_symptoms) + '\\b'

Get the dataframe that contains multi words

    covid_df[covid_df['Sentence'].str.contains(pattern_multi)]

Export them to a csv file if needed
    
    multi_word_sentences.to_csv('/Users/elif/Desktop/multi_word_sentences.csv', index = False)
