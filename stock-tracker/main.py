import requests
from twilio.rest import Client

# import alpha_vantage

STOCK_NAME = "TSL"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "Z7H1CVSFN6YN77OA"
NEWS_API_KEY = "d1f8dcd966454940ac8444e16ae00ebf"
TWILIO_SID = "AC39c138c4366aa813e00a71e29f34a95c"
TWILIO_AUTH_TOKEN = "965d12c98b6e9d36afedaff3b55fb786"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
# how can we change the large dictionary into a list
data_list = [value for (key, value) in data.items()]
# print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)
difference = abs(float(yesterday_closing_price) -
                 float(day_before_yesterday_closing_price))
print(difference)
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)
if diff_percent > 1:
    news_params = {
        "apikey": NEWS_API_KEY,
        "q": COMPANY_NAME,

    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    three_articles = articles[:3]
    # print(three_articles)
    formatted_articles = [
        f"Headline:{article['title']}.\nBrief: {article['description']}" for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        print(article)
        message = client.messages.create({body=article,from= "+15167306982",to = "+12066370459",})
