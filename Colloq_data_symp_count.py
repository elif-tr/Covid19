
def symAndCount(dataframe):
    '''
    :param dataframe: It takes in a data frame of tagged sentences and split words
    :return: dictionary of all the marked symptoms and their counts of how many times they appear in the dataframe
    '''
    values_dict = {}
    sym_str = ''
    for i,row in enumerate(dataframe.values):

        if row[2]=='B-SYM'and dataframe.values[i+1][2] == 'O':
            if row[1].lower() in values_dict:
                values_dict[row[1].lower()]+=1
            else:
                values_dict[row[1].lower()] = 1
        if (row[2]=='B-SYM'and dataframe.values[i+1][2] == 'I-SYM') or row[2]=='I-SYM':
            sym_str +=str(row[1]).lower()+' '
            if dataframe.values[i+1][2] == 'O':
                sym_str = sym_str.strip()
                if sym_str in values_dict:
                    values_dict[sym_str]+=1
                else:
                    values_dict[sym_str] = 1
                sym_str = ''
    return values_dict