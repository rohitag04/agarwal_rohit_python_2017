<img src="icon.png" align="right" />
# Midterm Project <img src="python.png" height="54px" width="200px" />
> This Project contains Analysis of two Data Sets.
  - Ernon Company Dataset.
  - New York Times Dataset.
    - Articles Archive.
    - User Comments.

## 1- Analysis on Enron Dataset
- More Information About Enron - [Enron Scandal] (http://www.investopedia.com/updates/enron-scandal-summary/)
- Note -: I have Done 3 types of Analysis of Enron Employee's emails.

## Analysis 1 (Topic Modelling on All Employees Sent Emails)
> What is Topic Modelling?
- Topic can be defined as “a repeating pattern of co-occurring terms in a corpus”.

### Step 1 (Data Reading & Cleaning)
Packages Used -:
- GLOB
- OS
- Email Parser
- RE

I have read "Sent Items" folder of all Employees.
'''
1- Lopped through each email and sent to Email Parser in order to get the "Text Body".
'''

