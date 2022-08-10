Describe the trend of lumber costs as well as other associated and possibly correlated other factors.  If feasible build a model to predit lumber prices based on times series as well as other factors.  The end user would be potential clients who are looking to build houses and helping them understand lumber costs and whether now or later is a better time to begin building.

Data Ingestion.  Python script to get webscrape data from https://markets.businessinsider.com/commodities/lumber-price or similar website.  Also utilize API for additional data with websites such as https://alpaca.markets/docs/api-references/market-data-api/Data Storage and/or https://www.econdb.com/api/series/?page=1Deployment and/or https://datausa.io/about/api/Testing/Robustness  and/or https://covidtracking.com/data/api/version-2 and/or https://developer.twitter.com/en/docs

Data Storage.  This should probably be mostly JSON files into MongoDB but may be SQL as well depending.

Processing.  Clean Data into a usable standardized format from different sources using Pandas in python or Spark.

Deployment.  Currently planning to use streamlit to deploy a webapp with interactive graphs.

Testing/Robustness.  Set up a cron job that pulls data daily.  Explore unit testing and OOP.
