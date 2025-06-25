import requests
import pandas as pd
from datetime import datetime
import time as t

# API URL
base_url = "https://api.cnyes.com/media/api/v1/newslist/category/tw_stock?page={}&limit=30&showOutsource=1"

# 初始化
all_data = []
title_set = set()

for page in range(1, 4):  # 自行調整頁數
    url = base_url.format(page)
    print(f"📄 抓取第 {page} 頁：{url}")

    try:
        response = requests.get(url)
        response.raise_for_status()
        articles = response.json()['items']['data']
    except Exception as e:
        print(f"⚠️ 第 {page} 頁解析失敗：{e}")
        continue

    for article in articles:
        title = article["title"]
        if title in title_set:
            continue

        news_id = article["newsId"]
        link = f"https://news.cnyes.com/news/id/{news_id}?exp=a"
        content = article.get("content", "")
        category = article.get("categoryName", "")

        # 解析時間
        timestamp = article.get("publishAt")
        news_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M") if timestamp else "無時間"

        all_data.append({
            "標題": title,
            "連結": link,
            "類別": category,
            "內容": content,
            "時間": news_time
        })

        title_set.add(title)
        t.sleep(0.1)  # 小延遲防止封鎖

# 存入 CSV
df = pd.DataFrame(all_data)
df.to_csv("鉅亨新聞.csv", index=False, encoding="utf-8-sig")
print(f"✅ 完成，共抓取 {len(df)} 筆資料，已存入鉅亨新聞.csv")

#定義雜訊
import re
RE_SUSPICIOUS = re.compile(r'[&#<>;{}\[\]\\]')

def impurity(text, min_len=10):
    """returns the share of suspicious characters in a text"""
    if text == None or len(text) < min_len:
        return 0
    else:
        return len(RE_SUSPICIOUS.findall(text))/len(text)


df['impurity'] = df['內容'].apply(impurity, min_len=10)
df.columns
df[['內容', 'impurity']].sort_values(by='impurity', ascending=False).head(3)



#雜訊清理
import html

def clean(text):
    # convert html escapes like &amp; to characters.
    text = html.unescape(text) #in this example, this part does nothing
    # tags like <tab>
    text = re.sub(r'<[^<>]*>', ' ', text)
    # markdown URLs like [Some text](https://....)
    text = re.sub(r'\[([^\[\]]*)\]\([^\(\)]*\)', r'\1', text)
    # text or code in brackets like [0]
    text = re.sub(r'\[[^\[\]]*\]', ' ', text)
    # standalone sequences of specials, matches &# but not #cool
    text = re.sub(r'(?:^|\s)[&#<>{}\[\]+|\\:-]{1,}(?:\s|$)', ' ', text)
    # standalone sequences of hyphens like --- or ==
    text = re.sub(r'(?:^|\s)[\-=\+]{2,}(?:\s|$)', ' ', text)
    # sequences of white spaces
    text = re.sub(r'\s+', '', text)
    return text.strip()

df['clean_text'] = df['內容'].apply(clean)

df['impurity']   = df['內容'].apply(impurity, min_len=20)

df[['clean_text', 'impurity']].sort_values(by='impurity', ascending=False) \
                              .head(3)


#normalization
import textacy.preprocessing as tprep
#you need to install textacy
def normalize(text):
    text = tprep.normalize.hyphenated_words(text)
    text = tprep.normalize.quotation_marks(text)
    text = tprep.normalize.unicode(text)
    text = tprep.remove.accents(text)
    return text

#Data masking
from textacy.preprocessing import replace

df['clean_text'] = df['clean_text'].map(replace.urls)
df['clean_text'] = df['clean_text'].map(replace.emails)
df['clean_text'] = df['clean_text'].map(replace.hashtags)
df['clean_text'] = df['clean_text'].map(replace.user_handles)
df['clean_text'] = df['clean_text'].map(normalize)


df.rename(columns={'內容': 'raw_text', 'clean_text': '內容'}, inplace=True)
df.drop(columns=['impurity'], inplace=True)

df['impurity'] = df['clean_text'].apply(impurity, min_len=10)
