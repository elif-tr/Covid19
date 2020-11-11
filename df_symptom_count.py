import re
import pandas as pd

def symptoms_df(df_sym, symp):
    '''
    :param df_sym:
    :param symp: List of symptoms we want to check on the given data frame and get the count of occurance
    Function that produces the data frame of counts of symptoms that exist in the given data frame from the list of symptoms
    The produced data frame includes all the symptoms and how many times they appear in the dataframe
    '''
    df_test = df_sym.Sentence.str.extractall('({})'.format('|'.join(symp)), flags=re.IGNORECASE) \
                  .iloc[:, 0].str.get_dummies().sum(level=0)
    sum_column = df_test.sum(axis=0)

    df_symptom_count = pd.DataFrame({'Symptoms': sum_column.index, 'Counts': sum_column.values})
    df_symptom_count['Symptoms'] = df_symptom_count['Symptoms'].str.lower()
    sym_df = df_symptom_count.groupby('Symptoms').sum().sort_values(['Counts'], ascending=False)
    return sym_df
