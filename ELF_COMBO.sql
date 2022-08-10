CREATE TABLE ELF_COMBO AS


WITH LUMB AS
(SELECT
dc.date2 AS date
,avg("Close_Last")  AS Lumber_Price

FROM Lumber Lum

LEFT OUTER JOIN date_corp dc
ON Lum.Date = dc.Actual_Date

GROUP BY dc.date2
) ,

COV AS
(
SELECT
dc.date2 AS date
,avg(cv."actuals.newCases") as cases
,avg(cv."actuals.newDeaths") as deaths

FROM COVID cv

LEFT OUTER JOIN date_corp dc
ON cv.date = dc.Cov_Date

GROUP BY dc.date2
)

SELECT
cpi.date
,cpi.CPIUS AS "Consumer_Price_Index"
,u.URATEUS AS "Unemployment"
,a.ELEUS AS "Elect_Prod"
,b.EXPUS AS "Export_Goods_Services"
,c.GASDEMUS AS "Gas_Demand"
,d.GASODEMUS AS "Gasoline_Demand"
,e.GSPEUS AS "Gen_Govt_Tot_Expenditure"
,f.GDEBTUS AS "Govt_Debt"
,g.WAGEMANUS AS "Hourly_Wage_Manuf"
,h.HOUUS AS "Housing_Price"
,i.IMPUS AS "Import_Goods_Services"
,j.IPUS AS "Industrial_Production"
,k.POLIRUS AS "Interest_Rates"
,l.CIUS AS "Inventory_Change"
,m.JVRUS AS "Job_Vacancy_Rate"
,n.M3US AS "Money_Supply"
,o.OILDEMUS AS "Oil_Demand"
,p.OILPRODUS AS "Oil_Prod"
,q.PPIUS AS "Producer_Price_Index"
,r.RGDPUS AS "Real_GDP"
,s.RETAUS AS "Retail_Trade"
,t.SENTUS AS "Sentiment_Index"
,v.SEIUS AS "Stock_Exchange"
,w.Lumber_Price
,x.cases
,x.deaths


FROM Consumer_Price_Index cpi

LEFT OUTER JOIN Unemployment u
ON cpi.date = u.date

LEFT OUTER JOIN Elect_Prod a
ON cpi.date = a.date

LEFT OUTER JOIN Export_Goods_Services b
ON cpi.date = b.date

LEFT OUTER JOIN Gas_Demand c
ON cpi.date = c.date

LEFT OUTER JOIN Gasoline_Demand d
ON cpi.date = d.date

LEFT OUTER JOIN Gen_Govt_Tot_Expenditure e
ON cpi.date = e.date

LEFT OUTER JOIN Govt_Debt f
ON cpi.date = f.date

LEFT OUTER JOIN Hourly_Wage_Manuf g
ON cpi.date = g.date

LEFT OUTER JOIN Housing_Price h
ON cpi.date = h.date

LEFT OUTER JOIN Import_Goods_Services i
ON cpi.date = i.date

LEFT OUTER JOIN Industrial_Production j
ON cpi.date = j.date

LEFT OUTER JOIN Interest_Rates k
ON cpi.date = k.date

LEFT OUTER JOIN Inventory_Change l
ON cpi.date = l.date

LEFT OUTER JOIN Job_Vacancy_Rate m
ON cpi.date = m.date

LEFT OUTER JOIN Money_Supply n
ON cpi.date = n.date

LEFT OUTER JOIN Oil_Demand o
ON cpi.date = o.date

LEFT OUTER JOIN Oil_Prod p
ON cpi.date = p.date

LEFT OUTER JOIN Producer_Price_Index q
ON cpi.date = q.date

LEFT OUTER JOIN Real_GDP r
ON cpi.date = r.date

LEFT OUTER JOIN Retail_Trade s
ON cpi.date = s.date

LEFT OUTER JOIN Sentiment_Index t
ON cpi.date = t.date

LEFT OUTER JOIN Stock_Exchange v
ON cpi.date = v.date

LEFT OUTER JOIN LUMB w
ON date(cpi.date) = date(w.date)

LEFT OUTER JOIN COV x
ON date(cpi.date) = date(x.date)

;
