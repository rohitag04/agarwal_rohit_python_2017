<img src="icon.png" align="right" />
# Midterm Project <img src="python.png" height="54px" width="200px" />
> This Project contains Analysis of two Data Sets.
  - Ernon Company Dataset.
  - New York Times Dataset.
    - Articles Archive.
    - User Comments.

# 1- Analysis on Enron Dataset
- More Information About Enron - [Enron Scandal] (http://www.investopedia.com/updates/enron-scandal-summary/)
- Note -: I have Done 3 types of Analysis of Enron Employee's emails.

# Analysis 1 (Topic Modelling on All Employees Sent Emails)
> What is Topic Modelling?
- Topic can be defined as “a repeating pattern of co-occurring terms in a corpus”.

### Step 1 (Data Preperation)
Packages Used -:
- GLOB
- OS
- Email Parser

I have read "Sent Items" folder of all Employees.
```
1- Lopped through each email and sent to Email Parser (get_payload()) in order to get the "Text Body".
2- Stored text body of all sent emails as txt file in seperate directory. [midterm/que[1-2]/ana_[1-3]/Topic Modelling/Sent Emails].
3- Read all sent emails txt files and stored in one LIST.
```
### Step 2 (Cleaning & Preprocessing)
Packges Used -:
- RE
- NLTK Stop Words
- NLTK Wordnet

In this step I have remove the punctuations, stopwords and normalize the List.
```
1- Looped through the List to remove all stopword using (nltk stopwords('english))
2- Removed all Punctuation from the List.
3- Normalized the Data List using (NLTK wordnet lemma.lemmatize(word)).
```
### Step 3 (Preparing Document-Term Matrix)
Packages Used-:
- Gensim

All the text documents combined is known as the corpus. To run any mathematical model on text corpus, it is a good practice to convert it into a matrix representation. LDA model looks for repeating term patterns in the entire DT matrix. 

```
1- Creating the term dictionary of data, where every unique term is assigned an index. 
2- Converting list of documents (corpus) into Document Term Matrix using dictionary prepared.
3- Created an object for LDA model and train it on Document-Term matrix using gensim library(Lda = gensim.models.ldamodel.LdaModel).
4- Running and Trainign LDA model on the document term matrix using gensim.
```

### Result of Topic Modelling
- Result is stored in [midterm/que[1-2]/ana_[1-3]/Topic Modelling/Sent Emails/result/topicModelling.png]
- See Attached image.
<img src ="que[1-2]/ana_[1-3]/Topic Modelling/result/topicModelling.PNG" />
```
Each line is a topic with individual topic terms. 
- Topic 1 - It Can be termed as Business.
- Topic 2 - It Can be termed as Legalities.
- Topic 3 - It Can be termed as Meeting.
- Topic 4 - It Can be termed as Meeting in casual tone.
```

### Conclusion from Above Analysis
- Topic 1 contains words that are directly related to the core business of Enron like "gas", "power" etc.
- Topic 2 while related to business seems to be more about the process rather than the content of the core business. 
  It has a lot of terms relevant to business legalities.
- Topic 3 contains a lot of meeting related words, perhaps they are from emails that were sent as meeting notices.
- Topic 4 also seems to be meeting-related but in a more casual tone and setting.


# Analysis 2



