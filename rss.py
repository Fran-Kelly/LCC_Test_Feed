from datetime import datetime
import os

RSS_FILE = "public/feed.xml"

def generate_rss(items):
    os.makedirs("public", exist_ok=True)
    rss_items = ""
    for item in items:
        rss_items += f"""
        <item>
            <title>{item['title']}</title>
            <link>{item['link']}</link>
            <description>{item['summary']}</description>
            <pubDate>{item['date']}</pubDate>
        </item>
        """
    rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
    <channel>
        <title>Liverpool Council AI Feed</title>
        <link>https://github.com/YOURNAME/lcc-newsfeed</link>
        <description>AI-generated summaries of Liverpool City Council reports</description>
        {rss_items}
    </channel>
    </rss>
    """
    with open(RSS_FILE, "w", encoding="utf-8") as f:
        f.write(rss_content)
    print(f"RSS feed updated: {RSS_FILE}")
