Abstract

The goal of this project was to make an end to end data pipeline with lumber pricing data as well as economic data and Covid data to compare and help explain the recent volatility in the lumber market.  Data was ingested, stored, processed, and then deployed to an app as well as scheduled for regular updates.   

Design

The design of this project was mostly around working through the steps of a data pipeline.  The lumber, economic, and covid data is readily available.  It needed to be pulled and then stored in a database.  Since the data is from several different sources it needed to be cleaned, aggregated, and standardized so it could be exported as one table.  It also need to be normalized so that it could be graphed in an easily comparable way.  Finally the data had to be deployed to an app so that it could be easily consumed.

Data

The dataset started as 28 different tables from different sources that were either webscraped or pulled through API's.  Most of the data consisted of a two column table with date and metric.  The date fields as well as the overall scale of the metrics was inconsistent.

Algorithms

The data was partially cleaned and aggregated in sql so it could be easily combined into a single table. The data was then further cleaned and normalized through a python script with pandas.

Tools

Tools used included Requests, BeautifulSoup, pandas, and selenium for webscraping and pulling from APIs.  SQL and pandas were used for processing.  AWS was used for scheduling updates to the data.  Streamlit, plotly, pandas, and git hub were used for deploying the app.


Communication

Slides and visuals presented included the data pipeline and screen shots of the finished app and the sql processing.  The final app is deployed on the Streamlit Cloud.  The address is https://matt-redmond-eng-streamlitapp-8t78po.streamlitapp.com/ The app is interactive and features a date range input as well as the ability to compare any or all of 20 different metrics.



