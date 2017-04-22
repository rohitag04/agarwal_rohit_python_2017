<img src="extra/cover.jpg" alt="alt text" align="middle"/>
<p align="center"><i>Does Weather Affect the Stock Market? </i></p>

## Table of Contents
1. [Idea](#1-idea)
2. [Data Collection](#2-data-collection)
3. [Data Storing](#3-data-storing)
4. [Analysis 1](#4-analysis-1)
      * [4.1 Temperature Trend](#41-temperature-trend)
      * [4.2 Annual Mean Temperature Trend](#42-annual-mean-temperature-trend)
      * [4.3 Impact on OIL (Non Renewable)](#43-impact-on-oil)
      * [4.4 Impact on Solar Energy (Renewable)](#44-impact-on-solar-energy)
      * [4.5 Impact on Wind Energy (Renewable)](#45-impact-on-wind-energy)
5. [Analysis 2](#5-analysis-2)
      * [5.1 Annual means of stock situation of renewable and non- renewable energy companies](#51-stock-situation)
      * [5.2 Standard deviation of weather, oil, solar and wind](#52-standard-deviation)
6. [Analysis 3](#6-analysis-3)
      * [6.1 Daily percentage return of stocks of Oil & Solar & Wind](#61-percent-change)
      * [6.2 Analysed risk of the stock using VaR(Value at Risk](#62-risk-analysis)
7. [References](#7-references)

## 1. Idea
#### Does Weather Affect the Stock Market?

Despite the best efforts of many highly trained economists and market specialists, there is no widespread consensus about how, or even if, weather affects the performance of the stock market.

It seems commonsensical that it must have some impact, since weather is a ubiquitous phenomenon from which traders are never fully isolated. On the other hand, there isn't a clear-cut, logical reason to expect that rain on Wall Street or a hurricane in Mexico should systematically change valuations or trader optimism. 

> __"Ultimately it's an interesting question."__

__As it's an Interesting Question. Let's find How Weather affect Renewable & Non Renewable Energy.__

## 2. Data Collection
I have collected Historical Data for year 2012-2017 using two different API's.

Packages Used -:
- OS
- Request
- JSON
- Date

__API 1__.

1- Wunderground (Weather Forecast API)

  - Used Wunderground Historical Data API for New York.
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
  
 **Data Source:** https://github.com/JostineHo/mememoji_api
 
 
 __API 2__.

2- Quandl (Stock Exchange API)

  - Used Quandl Historical Data API for Stocks of major compnaies (OIL & Solar).
  - OIL & SOLAR in particular because idea is impact on renewable & non renewable energies.
  - Collected Data from year 2012-2017 (April).
  - Data is collected in form of JSON.
  - Naming Convention is given on compnay code basis. So, Every file is unique.
  - I have created one function that made an API call inside loop and download all Data in json.
  
  ##### NOTE- 
  - API key is save in Environment Variable.
  - Data is only collected for OIL & SOLAR.
  
 **Data Source:** https://github.com/JostineHo/mememoji_api
 
 
 __Data for Wind Energy Company__.
 
 3- As I haven't found data for WIND ENERGY Company.
  - So I have downloaded CSV file from Yahoo Finance Website for Wind Energy for year 2012-2017 (April).
  - Direct Hit the url using request library and saved the CSV file.
  
  **Data Source:** https://github.com/JostineHo/mememoji_api
 
  **Source Code:** https://github.com/JostineHo/mememoji_api


## 3. Data Storing
As Collected Data was in the form of JSON file So I filtered and Stored in CSV Format for Analysis.

Packages Used -:
- Re
- Shutil
- CSV

__Wundeground API__.
  - Looped through all JSON files.
  - Extracted useful information like (Max Temp, Min Temp etc.)
  - Stored all extracted information in one CSV file.
  
  **Data Source:** https://github.com/JostineHo/mememoji_api

__Quandl API__.
  - Looped through all JSON files.
  - Extracted useful information like (Low Price, HIgh Price ect.)
  - Stored all extracted information in differet CSV file for different companies.
  
  **Data Source:** https://github.com/JostineHo/mememoji_api
  
  __Wind Energy DATA__.
   - Created a link in order to request data from Yahoo Finance.
   - Directly saved in CSV format.
   
   **Data Source:** [VWS.csv](https://github.com/rohitag04/agarwal_rohit_python_2017/edit/master/Final%20Exam/extra/VWS.csv)
   
   **Source Code:** https://github.com/JostineHo/mememoji_api
   
   ## 4. Analysis 1
### Topic - Impact of Weather on Energy Sources.

Packages Used -:
- OS
- Panda
- Plotly Offline
- iPlots
- Graph Objects

### Step 1 (Temperature Trend)
  - Read Weather.CSV in order to create Scatter plot to see trend of Maximum Temp (C) on daily basis for year [2012, 2014, 2016]
  - As CSV file contain Date column so I parsed it while reading.
  - Split the Date column in Day & Month.
  - Used Plotly Graph Object Scatter function in order to create plot.
  
  <img src="analysis/ana_[1-3]/Analysis 1/Per Day Max Temp.png" />
  
  ##### After Analyzing the above graph we can say:
  - Every second year tempeature was increasing.
  - As we can see Red Color for 2016 is more compare to previous years.
  - 4(2012)
  - 7(2014)
  - 19(2016)

##### Note- 
  - As it's hard to spot rise in temparature on day basis.
##### So in order to make it visible I have plotted mean Tempearture for Every Year.

### Step 2 (Annual Mean Temperature Trend)
  - Used the same Data Frame in order to find the mean.
  - Group by on Date coumn on basis of year.
  - Calculated the Mean of Max Temp. for each Year.
  - Used Plotly Graph Object Bar Plot function in order to create plot.
  
  <img src="analysis/ana_[1-3]/Analysis 1/Annual Mean Temp.png" />
  
  ##### After Analyzing the above graph we can say:
  - There is a rise in Annual Mean each year.
  - Which clearly proves that Temp. is increasing each year.
  - Which means Global Warming is increasing each year.
  
  ##### Note-
  - The year 2016 ranks as the warmest on record. (Source: NASA/GISS).
  - GLOBAL WARMING is increasing.

### Step 3 (Impact on OIL (Non Renewable))
##### Does Global Warming affect Oil Production?

  - Used the weather Data Frame.
  - Read Oil Company Stock name CVX.
  - Merged two dataframes outerly on Date Columns.
  - Removed all NAN values in order to keep clean file.
  - Analysed only for year 2012 & 2016.
  - Used Double Y axis plot in order to show Weather & Stock.
  
  <img src="analysis/ana_[1-3]/Analysis 1/Weather VS OIL Stock.png" />
  
##### Assumption 1 -:
##### Although there is not more difference in stock price from 2012 to 2016 because .
  - We know Global Warming is increasing.
  - The Consumption of Crude OIL is not Decreasing but it is consistent because.
  - OIL is now mostly using in Vehicles and Country is not totally shifted to ELECTRIC CARS.
  - SO, There is not much more impact of Weather on use of OIL.
  - Majority of the times we can see as the Max Temp increases the Stock Price Decreases.
    
##### Assumption 2-:
  - As GLOBAL Waring Increasing
  - There should be a increase in the price of Solar Energy.
    
##### Now, Does Weather affects Solar Energy Generation.


### Step 4 (Impact on Solar Energy (Renewable))
##### Does Global Warming affect Solar Energy Generation?

  - Used the weather Data Frame.
  - Read Solar Energy Company Stock name FSLR (First Solar).
  - Merged two dataframes outerly on Date Columns.
  - Removed all NAN values in order to keep clean file.
  - Analysed only for year 2012 & 2016.
  - Used Double Y axis plot in order to show Weather & Stock.
  
  <img src="analysis/ana_[1-3]/Analysis 1/Weather VS Solar Stock.png" />
  
##### Assumptions 1 -:
##### Here I can see a huge difference in stock price because .
  - The Consumption of Solar Energy is increased from past years.
  - We can see the stock price is alomost doubled from 2012 to 2016.
  - Which indicates Global Warming is directly propotional to Renewable energy.
    
##### Assumption 2-:
  - There should be a increase in the price of Wind Energy.
    
##### Now, Does Weather affects Wind Energy Generation.

### Step 5 (Impact on Wind Energy (Renewable))
##### Does Global Warming affect Wind Energy Generation?

  - Used the weather Data Frame.
  - Read Wind Energy Company Stock name VWS (Vestas Wind).
  - Merged two dataframes outerly on Date Columns.
  - Removed all NAN values in order to keep clean file.
  - Analysed only for year 2012 & 2016.
  - Used Double Y axis plot in order to show Weather & Stock.
  
  <img src="analysis/ana_[1-3]/Analysis 1/Weather VS WIND Stock.png" />
  
##### Assumptions -:
##### Here I can see a Huge Huge difference in stock price.
  - We can see the stock price is alomost increased 80 times from 2012 to 2016.
  - Which indicates Global Warming is directly propotional to Renewable energy.
    
### Final Conclusion
  - Weather Plays a major role in stock price.
  - As Annual mean of weather is increasing every year.
  - Global Warming is also Increasing.
  - At the same time uses of Renewable Energy is also increasing Annualy.
  - Non Renewable energy is stagnant due to other usages.
  
##### Note-:
  - This Comparision is done on Annual Temperature.
  
  **Source Code:** [Analysis 1.ipynb]()
  
  
  ## 5. Analysis 2
### Topic - Percentage shift on Weather & Stock.

Packages Used -:
- OS
- Panda
- Numpy
- Matplotlib
- Seaborn
- Plotly Offline
- iPlots
- Graph Objects

### Step 1 (Annual means of stock situation of renewable and non- renewable energy companies)
  - Read all companies stock & weather csv file.
  - Merged tham all outerly using Date column.
  - Created new CSV name weatherStock csv that contain stock & weather data.
  - Read the new csv and filtered the data dropping year 2017 as we have less data for that year.
  - Created the new name stockWeather CSV and calculated Mean base of year for all years.
  - Used Plotly Graph Object Bar Plot function in order to create plot.
  
  **Data Source:** [WeatherStock.csv](https://github.com/rohitag04/agarwal_rohit_python_2017/blob/master/Final%20Exam/extra/weatherStock.csv) Store in Extra Folder
  
  **Data Source:** [StockWeather.csv](https://github.com/rohitag04/agarwal_rohit_python_2017/blob/master/Final%20Exam/analysis/ana_%5B1-3%5D/Analysis%202/stockWeather.csv)
  
  <img src="analysis/ana_[1-3]/Analysis 2/Mean.PNG" />
  
   ##### The Above plot describes:
   - The comparative study of annual means of stock situation of renewable and non- renewable energy companies
against the annual means of temperatures.
   - The study shows a stagnancy in the rise of non-renewable energy (oil) company's stock.
   - When the global oil dependancy is put under the microscope, it is realized that means of transport throughout the world depend on oil as fuel source.
   - Electricity supplied throughout the country through power plants is generated using similar means. 
   - The past decade has seen a steep rise in global temperatures and ancient and historical environmental studies have painted a grim picture revealing the current timeline to be the warmest.
   - The above plot reflects a magnanimous rise in wind power and solar power.
   - The rise in weather can be clearly marked from 2012, when the mean was meandering about 0.65, to 2016, when the mean has mounted to 0.94
   
 ### Step 2 (Standard deviation of weather, oil, solar and wind)
  - Used the same Data Frame.
  - Filtered on the year 2016.
  - Removed all NAN values.
  - Removed all Infinite values in order to clean Data Frame.
  - Calculated Percentage change on Max Temp. and Adj Close column of weather & stock.
  - Used seaborn distplot in order to show standard deviation.
  
  <img src="analysis/ana_[1-3]/Analysis 2/Daily Return.PNG" />
  
  ##### The Above plot describes:
   - TThe comparable analyses of the standard deviation of weather, oil, solar and wind.
   - Reflecting the gradual fall in the stock value of oil.
   - while a consistent rise of stocks of solar and wind companies when compared with shifts in temperatures.
   - When the sum of histogram values across the negative and positive deviation are compared a higher value (solar, wind and temperature) shows a tend towards rising value while a lower value (oil) elucidates a trend against the particular stock.
   
### Final Conclusion
  - Colloquially, nations have pushed for greater utilization of non-renewable energy sources to prevent the environment from distruction which will see the trend followed in the near future.
  - The rise of solar is consistently progressing, wind power consumption as a means to produce energy
has shot through the roof.
  - Oil meanwhile has simultaneously regressed.
  
##### Note-:
  - This Comparision is done on Annual Mean Temperature & Stock.
  
  **Source Code:** [Analysis 2.ipynb]()
   
   
 ## 6. Analysis 3
### Topic - Coorelation between Renewable & Non Renewable Energy Stocks.

Packages Used -:
- OS
- Panda
- Numpy
- Matplotlib
- Seaborn

### Step 1 (Daily percentage return of stocks of Oil & Solar & Wind)
  - Read all required CSV file using pandas.
  - created seperate dataframes for seperate CSV.
  - As CSV contains dates so I parsed it while reading using parse_dates
  - Task is to merge all csv outerly on Date Column
  - Saving the final CSV in Analysis 3 Folder for final Analysis.
  - As we know 2017 is running and I don't have enough Data to represent so I removed all Data for 2017.
  - I done the cleaning using drop NAN values.
  - Calculated Percentage Change of each company stock with related to past dates.
  - Plotted corelation between OIL & SOLAR & WIND.
  
  **Data Source:** [sotck.csv](https://github.com/rohitag04/agarwal_rohit_python_2017/blob/master/Final%20Exam/analysis/ana_%5B1-3%5D/Analysis%203/stock.csv)
  
  <img src="analysis/ana_[1-3]/Analysis 3/oilVSSolar.png" /> <img src="analysis/ana_[1-3]/Analysis 3/solarVSwind.png" /> <img src="analysis/ana_[1-3]/Analysis 3/windVSoil.png" />
  
#### RESULT FROM ALL  COORELATIONS
  - The correlation coefficient B/w OIL & SOLAR is 0.25.
  - The correlation coefficient B/w SOLAR & WIND  is 0.11.
  - The correlation coefficient B/w WIND & OIL is 0.13.
    
#### NOTE- AS The coorealtion coefficient is not a lot but after analysing above cooefiicients.
   - I can say OIL & SOLAR have some coorelation between them.
   
   
### Creating a Pair Plot for an automatic visual analysis of all the comparisons.

<img src="analysis/ana_[1-3]/Analysis 3/PairPlot.png" align='middle'/>

#### From Above We can say,
  -  A quick glance shows positive correlation between CVX and FSLR daily returns are rather high.


#### Now, will draw a correlation HeatMap plot with actual numerical values for the correlation between the stocks' daily return values.

<img src="analysis/ana_[1-3]/Analysis 3/heatMapCoorelation.png" align='middle'/>

#### Result from above coorealtion plot.
   - Just like we suspected in our Coorelation Plot, we see here that CVX and FSLR had the strongest correlation of daily stock return. 


### Step 2 (Analysed risk of the stock using VaR(Value at Risk)
  - Used the same data frame.
  - Calculated Mean, Standard Deviation of all companies stock.
  - Plotted Risk & Expected Retruns on X and Y axis.
  - Used Matplotlib Annotate function in order to plot.
  
  <img src="analysis/ana_[1-3]/Analysis 3/RiskVSReturns.png" align='middle'/>
  
#### From above Result-:
  - It seems that VWS(WIND) is the best choice.
  - If we can only choose 1 stock. As it has the highest expected returns and lowest risk.


#### Next, we find the Risk using Empirical Quantile .
- What is Empirical Quantile?
    - In statistics and the theory of probability, quantiles are cutpoints dividing the range of a probability distribution into contiguous intervals with equal probabilities, or dividing the observations in a sample in the same way. There is one less quantile than the number of groups created.
    
<img src="analysis/ana_[1-3]/Analysis 3/Empirical Quantile.PNG" align='middle'/>

#### Result from above
  - It means that with 90% confidence, our worst daily loss for VWS will not exceed by 4.5%.
  
### Final Conclusion
   - There is a coorelation between OIL & SOLAR.
   - VWS is the best choice to buy.
   - Daily Risk for VWS Stock will not increase 4.5 %.
   - Buying 1 Stock has highest expected returns & Lowest Risks.
   
 
## 7. References

1. https://climate.nasa.gov/vital-signs/global-temperature/

2. https://ntguardian.wordpress.com/2016/09/19/introduction-stock-market-data-python-1/

3. https://blog.nycdatascience.com/student-works/nyc-weather-affect-stock-market/
