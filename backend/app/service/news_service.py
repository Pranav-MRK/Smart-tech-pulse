import feedparser

TECH_RSS_FEEDS = [
    "https://techcrunch.com/feed/",
    "https://hnrss.org/frontpage",
]

def fetch_news():
    all_news = []

    for url in TECH_RSS_FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:  # limit for now
            news_item = {
                "title": entry.title,
                "link": entry.link,
                "summary": entry.summary if "summary" in entry else ""
            }
            all_news.append(news_item)

    return all_news

def filter_news_by_interests(news_list, interests):
    filtered_news =[]

    for news in news_list:
        content = (news["title"] + " " + news["summary"]).lower()
        for interest in interests:
            if interest.lower() in content:
                filtered_news.append(news)
                break

    return filtered_news
        