import requests

api_key = "d8944af9de5c45b99ab0641a4b7217d6"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-03-12&sortBy=publishedAt&apiKey=" \
      "d8944af9de5c45b99ab0641a4b7217d6"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])