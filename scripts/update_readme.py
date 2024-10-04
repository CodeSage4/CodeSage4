import requests
import json

def get_latest_ai_news():
    url = "https://newsapi.org/v2/everything?q=artificial%20intelligence&apiKey=YOUR_API_KEY"
    response = requests.get(url)
    news_items = response.json()['articles'][:3]  # Get the latest 3 articles
    return news_items

def generate_readme_content(news_items):
    content = "### 📢 Did You Know?\n"
    for article in news_items:
        content += f"- **{article['title']}**: {article['description']} [Read more]({article['url']})\n"
    return content

if __name__ == "__main__":
    news = get_latest_ai_news()
    readme_content = generate_readme_content(news)
    
    # Overwrite the README file
    with open("README.md", "w") as file:
        file.write(readme_content)
