import re
def repl(m):
    '''
    regular expression function that replaces symptoms with BSYM if .group(0) is one word
    or BSYM + ISYM if multiple words - this function looks for spaces in the given words

    m.group(0) - first match
    '''
    return ' '.join(['BSYM'] + ['ISYM'] * (m.group(0).count(' ')))


# %%

def symptom_search(df, sym):
    pattern = '\\b' + '\\b|\\b'.join(sym) + '\\b'
    df['Token'] = df['Sentence'].str.replace(pattern, repl, flags = re.IGNORECASE)
    df['Sentence_ID'] = ['Sentence #%s' % i for i in range(1, len(df) + 1)]

    return df
