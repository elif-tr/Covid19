import pandas as pd
import re

'''
The function takes in a data frame where entire text from a paper is captured in one cell and splits those text into 
one sentence per row.
Output data frame includes one sentence per row and which paper id that sentence comes from.

'''

def split_sentences(df):
    '''
    Takes in a data frame where there are multiple sentences in one row and splits them into one row per sentence

    :param df: data frame that we would like to split
    :return a data frame with one sentence per row and what paper that sentence belongs to

    '''
    sentences = []
    sentence_pattern = r'(?<=[^A-Z].[.?]) +(?=[A-Z])'  # splitting criteria

    for row in df.itertuples():
        for sentence in re.split(sentence_pattern, row[2]):
            sentences.append((row[1], sentence))

    new_df = pd.DataFrame(sentences, columns=['Paper_Id', 'Sentence'])
    #Sentence ID will keep track of which sentences from the original dataframe will be retreived when we check for symptoms in each sentence.
    new_df['Sentence_ID'] = new_df.index + 1 #start the id values from 1
    return new_df


def sentence_w_symptoms(df, sym):
    '''
    Takes in a data frame and list of symptoms, returns a new data frame with sentences that include any of the symptoms

    :param df: data frame with multiple senteces per row
    :param sym: the symtoms that we would like to check in the data frame
    :return data frame of sentences that include one or more of the symptoms

    '''
    # match beginning of words and end of words for symptoms, not partial
    pattern = '\\b' + '\\b|\\b'.join(sym) + '\\b'
    final_df = df[df['Sentence'].str.contains(pattern, flags=re.IGNORECASE)].copy()

    return final_df





