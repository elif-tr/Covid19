## Text splitting

The first function takes in a data frame where entire text from a paper is captured in one cell and splits those text into 
one sentence per row.
Output data frame includes one sentence per row and which paper id that sentence comes from.

## Important:

I used nltk to split the text into sentences however, it did not do aa good job.
Thus, I switched the code to use regular expression which is outperforming the nltk tokenizer especially with colloquial data. 

## Extracting the sentences with symptoms only

The second function takes in the data frame with no titles and extracts only the sentences that mentions any of the symptoms from the list of symptoms that is provided

    -The df no title data frame is created beacuse I encountered a problem with extracting sentences that included any of the symptoms
    For simplicity I removed the title column 

Symptoms list is left out of the module so that it can be updated when needed.