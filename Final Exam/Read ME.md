<img src="extra/cover.jpg" alt="alt text" align="middle"/>
<p align="center"><i>Does Weather Affect the Stock Market? </i></p>

## Table of Contents
1. [Idea](#1-idea)
2. [Data Collection](#2-data-collection)
3. [Data Storing](#3-data-storing)
4. [Analysis 1](#4-analysis-1)
5. [Analysis 2](#5-analysis-2)
6. [Analysis 3](#6-analysis-3)
7. [References](#7-references)

## 1 Idea
#### Does Weather Affect the Stock Market?

Despite the best efforts of many highly trained economists and market specialists, there is no widespread consensus about how, or even if, weather affects the performance of the stock market.

It seems commonsensical that it must have some impact, since weather is a ubiquitous phenomenon from which traders are never fully isolated. On the other hand, there isn't a clear-cut, logical reason to expect that rain on Wall Street or a hurricane in Mexico should systematically change valuations or trader optimism. 

> __"Ultimately it's an interesting question."__

__As it's an Interesting Question. Let's find a relation between them.__

## 2 Data Collection
I have collected Historical Data for year 2012-2017 using two different API's.

Packages Used -:
- OS
- Request
- JSON
- Date

__API 1__

1- Wunderground API (Weather Forecast API)

  - Used wunderground Historical Data API for New York.
  - New York in particular because Stock Exchange is located there.
  - Collected Data on daily basis from year 2012-2017 (April).
  - Data is collected in form of JSON.
  - Naming Convention is given on date basis. So, Every file is unique.
  - There are total of around 1800 Json Files.
  - I have created one function that made an API call inside loop and download all Data in json.
  
  ##### NOTE- 
  - Data is collected on daily basis because of per day limit.
  - Daily limit was 500. So, All Data is collected in 4 days.
  - API key is save in Environment Variable.
  - Data is only collected for New York City.
  
 **Source Code:** https://github.com/JostineHo/mememoji_api
 **Data Source:** https://github.com/JostineHo/mememoji_api





