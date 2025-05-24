import requests
import smtplib


stock_key="FD0UMLSXLVJH4IFO"
news_key="3395aae9f11a4f70a78466dc9d8e5c64"


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



stock_params={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_key,
}
response=requests.get(STOCK_ENDPOINT, params=stock_params)
data=response.json()["Time Series (Daily)"]

data_list=[value for (key, value) in data.items()]

yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]

day_before_data=data_list[1]
day_before_closing_price=day_before_data["4. close"]

abs_diff=float(abs(float(yesterday_closing_price)-float(day_before_closing_price)))


diff_percent=(abs_diff/float(yesterday_closing_price))*100

if diff_percent>5:
    news_paras = {
        "apiKey": news_key,
        "qInTitle": COMPANY_NAME
    }

    news_responese=requests.get(NEWS_ENDPOINT, params=news_paras)
    news_data=news_responese.json()["articles"]
    three_articles=news_data[:3]

    formatted_articles=[f"Headline: {article['title']}, \nBrief: {article['description']}" for article in three_articles]

    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login("shoaibmunavary@gmail.com", "****************")
    for article in formatted_articles:
        connection.sendmail(
            from_addr="shoaibmunavary@gmail.com",
            to_addrs="shoaibmunavary@gmail.com",
            msg=article
        )



