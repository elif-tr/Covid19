## COVID19 related papers that published during the first week of May, 2020

This file takes in the meta data file from kaggle.com for the covid papers
based on the filtering dates entered in the second function it reads in those json files only
read_json function takes in the list of json files for the given filtered dates and outputs a 
data frame with paper_id, title of the paper and full text of the paper as final output.

Use this module when you need to extract papers from

https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge  

### Working with meta data file

First read in the meta data file to filter the papers for the time frame we want.

### 1. Encountered Problem: Files that contain multiple papers

I observed that some of the files contain more than one paper which makes it harder for us to read them in individually. For that, we will bring all our json files into same format of containing 1 file per document.

### Extracting only the columns needed for our analysis 

Some of the code was take from: https://www.kaggle.com/davidbetancur8/symptoms-word-cloud
