from nltk import word_tokenize
import pandas as pd

'''
Module that splits sentences into one word per row and then tags them with b-sym and i-sym
Output file is sentence number, words on that sentence per row and the tag for each row - 3 columns
'''

def tokenize_sentences(frame):
    '''

    :param frame: Data frame that has the sentence_id and one sentence per row - 2 columns in total
    :return: data frame that tags symptoms as b-sym if the word is beginning of a symptom and i-sym if it is the continuing word for a symtom
    '''
    words = []
    i = 0
    for j, row in frame.iterrows():
        for word, temptag in zip(word_tokenize(row['Sentence']), word_tokenize(row['Token'])):
            if temptag == 'BSYM':
                tag = 'B-SYM'
            elif temptag == 'ISYM':
                tag = 'I-SYM'
            else:
                tag = 'O'
            words.append((row['Sentence_ID'], word, tag))

    tag_df = pd.DataFrame(words, columns=['Sentence_ID', 'Words', 'Tag'])
    return tag_df


def remove_duplicate_sentence_ids(df):
    '''
    Takes in the data frame where the same sentence numbers are repeated multiple times and returns a df
    that repeats sentence number only once for the entire row of words that it has

    '''
    is_duplicate = df['Sentence_ID'].duplicated()

    df['Sentence_ID'] = df['Sentence_ID'].where(~is_duplicate, ' ')
    tagged_data = df[['Sentence_ID', 'Words', 'Tag']]
    return tagged_data