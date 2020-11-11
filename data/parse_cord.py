import pandas as pd
import os
import json

''' 
This file takes in the meta data file from kaggle.com for the covid papers
based on the filtering dates entered in the second function it reads in those json files only
read_json function takes in the list of json files for the given filtered dates and outputs a 
data frame with paper_id, title of the paper and full text of the paper as final output.

Use this module when you need to extract papers from

https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge    
'''


def meta_data(folder_name, metadata="metadata.csv"):
    ''' Function that takes in the folder name and returns the data fram fro the meta data

    :param folder_name: name of folder where covid data is located
    :param metadata: file name for where metadata is saved
    :return: data frame of the metadata

    '''

    file_name = os.path.join(os.getcwd(), folder_name, metadata)
    data = pd.read_csv((file_name), usecols=['pdf_json_files', 'publish_time'], encoding='utf-8')
    return data


def json_files(data_dir, start_date='2020-05-01', end_date='2020-05-31'):
    '''Function that filters the meta data file for a time frame we want.
    If nothing specified, first week of may will be used

    :param start_date: reading in the json files from when they were published
    :param end_date: reading in the json files until when they were published
    :return: lisf of json file names that are within the specified publication date

    '''

    file = meta_data(data_dir)
    file['publication_date'] = pd.to_datetime(file['publish_time'])
    may_first_week = file[(file['publication_date'] > start_date) & (file['publication_date'] <= end_date)]

    pdf_json = list(may_first_week['pdf_json_files'].dropna())

    #Those files were separated by ; sign instead of , sign.
    all_files = []
    for file in pdf_json:
        all_files.extend(map(str.strip, file.split(";")))

    return all_files

# Extracting only the columns needed for our analysis
# Some of the code was take from: https://www.kaggle.com/davidbetancur8/symptoms-word-cloud
def read_json_files(file_list, data_dir):
    '''Function that takes in date filtered json files and outputs a data frame with only 3 columns:
    paper_id, title and body text of the paper

    :param file_list: list of json files that will be read in by locating in the directory
    :return: return a data frame of those json files with three columns only "paper_id", "title", "full_text"

    '''
    docs = []
    for file in file_list:
        file_name = os.path.join(os.getcwd(), data_dir, file)
        with open(file_name) as f:
            data_json = json.load(f)

        title = data_json["metadata"]["title"]
        paper_id = data_json['paper_id']

        full_text = ""
        i = 1
        for text in data_json["body_text"]:
            i += 1
            full_text += text["text"]
        docs.append([paper_id, title, full_text])

    df = pd.DataFrame(docs, columns=["paper_id", "title", "full_text"])

    return df