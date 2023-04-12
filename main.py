import requests
from send_email import send_email

api_key = "d8944af9de5c45b99ab0641a4b7217d6"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-03-12&sortBy=publishedAt&apiKey=" \
      "d8944af9de5c45b99ab0641a4b7217d6"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
