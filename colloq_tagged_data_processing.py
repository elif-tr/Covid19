import numpy as np
import re
import pandas as pd


'''
This function takes in an already tagged colloquial data and any symptom list.
1. It put the split sentence words back together to create full sentences so that we can extract only the sentences that includes any of the symptoms
2. Removes the sentences where the length is 1 or less (i.e the ones that include only punctuation as a sentence)
3. Creates a dataframe with full text
4. Tokenize the full text to have 1 sentence per row 
5. Create a data frame that has one sentence per row
6. Extract only those sentences that include any of the symptoms
7.

'''


def colloquial_data_processing(tagged_data, symptom_list):
    '''
    Takes in the tagged data with 3 columns and the list of symptoms to search from,
    joins them back together to do a search of sentences that include any of the symptoms,
    eliminates the sentences that have 1 or less than 1 character, then splits those sentences into words
    and tokenizes them

    return data frame that includes only the sentences that mention one or more of the symptoms

    '''
    # Replace NaN values with emtpy spaces to match the original format
    tagged_data['Sentence'] = tagged_data['Sentence'].replace(np.nan, ' ')

    # Take in the data frame and create a list of sentences
    sent_value = []
    sentence = []
    for name, values in tagged_data.iterrows():

        if values['Sentence'].startswith('Sentence') == True:
            sent_value.append(sentence)
            sentence = []

        sentence.append(str(values['Words']))


    # -2- remove sentences that has lenght 1 or less
    sentence_list = []
    for sentence in sent_value:
        if len(sentence) <= 1:  # remove the sentences that have . or space as the only character
            continue

        full_txt = " ".join(sentence).strip()
        sentence_list.append(str(full_txt))

    #  -1- Join list together to have the full text to extract only the sentences that include symptoms
    full_Sent = " ".join(sentence_list)

    # -3- create a dataframe with the full text of words
    d = {'Sentence': [full_Sent]}
    col_df = pd.DataFrame(data=d)

    # -4- Tokenize the sentences to have one sentence per row
    sentences = []
    sentence_pattern = r'(?<=[^A-Z].[.?]) +(?=[A-Z])'
    for row in col_df.itertuples():
        for sentence in re.split(sentence_pattern, row[1]):
            sentences.append((row[0], sentence))

    # -5- data frame that has one sentence per row
    collo_df = pd.DataFrame(sentences, columns=['Index', 'Sentence'])

    collo_df.drop('Index', axis=1, inplace=True)

    # -6- Create a pattern to check for sentences that contain the symptoms
    new_pattern = '\\b' + '\\b|\\b'.join(symptom_list) + '\\b'
    colloqual_df = collo_df[collo_df['Sentence'].str.contains(new_pattern, flags=re.IGNORECASE)].copy()

    return sent_value, colloqual_df
