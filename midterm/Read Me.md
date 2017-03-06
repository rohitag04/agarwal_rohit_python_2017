<img src="icon.png" align="right" />
# Midterm Project <img src="python.png" height="54px" width="200px" />
> This Project contains Analysis of two Data Sets.
  - Enron Company Dataset.
  - New York Times Dataset.
    - Articles Archive.
    - User Comments.

## 1- Analysis on Enron Dataset
- More Information About Enron - [Enron Scandal] (http://www.investopedia.com/updates/enron-scandal-summary/)
- Note -: I have Done 3 types of Analysis on Enron Employee's emails.

## Analysis 1 (Topic Modelling on All Employees Sent Emails)
#### File Name (Midterm_Question 1 (Analysis 1 - Topic Modeling).ipynb) stored in midterm/que[1-2]/ana_[1-3].ipynb/]
> What is Topic Modelling?
- Topic can be defined as “a repeating pattern of co-occurring terms in a corpus”.

### Step 1 (Data Preperation)
Packages Used -:
- GLOB
- OS
- Email Parser

I have read "Sent Items" folder of all Employees from the data provided by professor.
```
1- Initially the data was in MIME type format.
2- Lopped through each email and sent to Email Parser (get_payload()) in order to get the "Text Body".
3- Stored text body of all sent emails as txt file in seperate directory. [midterm/data/Topic Modelling/Sent Emails/*.txt].
4- Read all sent emails txt files and stored in one LIST.
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

#### Final Conclusion based on Analysis.
- Core business of Enron was related to Gas, Power. Some business legalities were going on due to which lot of meeting were conducted.
- These Legalities can be related to any thing.


## Analysis 2 (Analysis on TOP [To & FROM] emails in Enron Data Set)
#### File Name (Midterm_Question 1 (Analysis 2 - Top Email Analysis).ipynb) stored in midterm/que[1-2]/ana_[1-3].ipynb/]
> In this Analysis-:
- I wil find TOP employee who recieved & sent most emails from directory of Half of Millions emails.
- Then will predict result on those TOP employees.
- Then will Analyse their emails on year basis.

### Step 1 (Data Preperation)
Packages Used -:
- GLOB
- OS
- Email Parser

I have read "ALL" folder of all Employees from the data provided by professor.
```
1- Initially the data was in MIME type format.
2- Lopped through each email and sent to Email Parser (get_payload()) in order to get the "To" & "FROM".
3- Stored TO & FROM of all emails in two different List.
```

### Step 2 (Cleaning & Preprocessing)
Packages Used -:
- RE

In this step I have replaced all the tab's, newlines and spaces.
```
1- Looped through the List to remove all stab's, newlines and spaces.
```

### Step 3 (Finding Top 10 from LIST & thier Count)
Packages Used -:
- Counter
- Collections

In this step I have Found the TOP to & from emp emails.
```
1- Looped through the List to find top 10 using Counter Counter(to_email_list).most_common(10).
```
See attached Pic.
<img src ="que[1-2]/ana_[1-3]/Top Employee/result/count.PNG" />
```
After Seeing above result.
- We can Predict -: (To Email)
    - The top person is Richard Shapiro.
    - He was the Vice President and lobbyist (“bribery guy”) for Enron.
    - A lot of his emails are about handing dollars to politicians, and getting favourable laws passed.
    - The fact that he received the most emails shows he was in touch with everything that was happening.
    
- (From Email)
    - Kay Mann, He is the head of legal for Enron.
    - The fact that she sent so many emails is ironical, seeing as how Enron was breaking every law in the book 
      keep in mind that most employees, including Kay Mann, were innocent.
    - Only the top executives were guilty, and most went to prison.
    
    
- Funny Fact:
   - A company with such a active legal department, and yet the executives ignored (or didn’t care) about the law at all. 
```

### Step 4 (Analysis on above result)
Packages Used -:
- CSV

In this step, I am going to analyse all emails of employee in each category w.r.t year.
```
1- Created List of emp name empList = ['shapiro-r', 'mann-k'].
2- I looped thorugh each employee all folder and saved date in two different list.
3- Date was in word format but I formatted and collected year with count of emails of each employee.
4- I stored Year and Count in CSV format that can be find here [midterm/que[1-2]/ana_[1-3]/Top Employee/emp/*.csv]
```

### Step 5 (Reading CSV file and Plotting on Pie Chart)
Packages Used -:
- Matplotlib

In this step, I read csv data from csv file and plotted on pie chart.
```
1- Used Matplotlib library to conert number in to % to plot % of emails in particulat year.
2- These files are stored in [midterm/que[1-2]/ana_[1-3]/Top Employee/emp/result/*.png]
```
 see attached pic
<img src ="que[1-2]/ana_[1-3]/Top Employee/result/shapiro-r.png" /> 
<img src ="que[1-2]/ana_[1-3]/Top Employee/result/mann-k.png" />
 
### Conclusion from Above Analysis & Pictures
- As we know, The company went bankrupt in year 2001. So, it was obvious that the whole email transaction was occur in same year.
- Richard Shapiro, The company Vice President. We can see 94 % of email traffic in year 2001.
- Kay Mann, Legal Head. We can see 50% of email traffic, which shows he was not actual the part of Enron. But he was actively involved.

## 2- Analysis on NYT API(Archive & User Comments)
- This Analysis is related to Articles & User Comments
- API key is save in Environment Variable.
- Note -: I have Done 2 Analysis on Archive & 1 Analysis on User Comments.

## Analysis 1 (This Analysis is based on Categories & based on Categories (Donal Trump(sub-categories Articles))
#### File Name (Midterm_Question 1 (Analysis 1 - Topic Modeling).ipynb) stored in midterm/que[1-2]/ana_[1-3].ipynb/]

### Step 1 (Data Preperation)
Packages Used -:
- JSON
- OS
- Requests

I made an API call to NYT Archive website with month and year parameters.
I stored a data for Jan'17.
```
1- Initially, I made an API call to NYT website to store data in JSON file in my local Directory.
2- I looped through that JSON file in order to find useful information related to articles.
3- Data I found through JSON is all stored in text files in directory. [midterm/data/Articles/*.txt].
4- Read that Text file and stored in one list.
```
### Step 2 (Preprocessing of Text Files)
Packges Used -:
- GLOB
- RE

In this step I have read text file and find all the useful information.
```
1- We Know Jan'17 was the presidential month, So I looped the text file in order to find all Politics Articles.
2- Removed all Punctuation from the List.
3- Found top 10 articles with their count.
```
### Step 3 (Preparing CSV File & Plots)
Packages Used-:
- Matplotlib
- CSV

In this, I have stored the Ranked list in CSV file and Read that file to plot top Articles on BAR Chart. 

```
1- Created a CSV file that contains top 10 articles with Rank w.r.t count.
2- Read CSV file in order to plot bar graph using Matplotlib.
```
see picture attached. 
<img src="que[1-2]/ana_[1-3]/Articles/result/percentTopic.png" />
- Result is stored in [que[1-2]/ana_[1-3]/Articles/result/percentTopic.png]

### Analysis based on above bar graph.
- From above we can see Category Name Politics contains more articles w.r.t other articles.
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

#### Final Conclusion based on Analysis.
- Core business of Enron was related to Gas, Power. Some business legalities were going on due to which lot of meeting were conducted.
- These Legalities can be related to any thing.
