#資料清理
import re

RE_SUSPICIOUS = re.compile(r'[&;#<>{}\[\]\\]')

def impurity(text, min_len=10):
    """returns the share of suspicious characters in a text"""
    if text == None or len(text) < min_len:
        return 0
    else:
        return len(RE_SUSPICIOUS.findall(text))/len(text)


df['impurity'] = df['內容'].apply(impurity, min_len=10)
df[['內容', 'impurity']].sort_values(by='impurity', ascending=False).head(5)





import html

def clean(text):
    # convert html escapes like &amp; to characters.
    text = html.unescape(text)
    # markdown URLs like [Some text](https://....)
    text = re.sub(r'\[([^\[\]]*)\]\([^\(\)]*\)', r'\1', text)#中括號有跟網址的符號刪除
    # text or code in brackets like [0]
    text = re.sub(r'\[[^\[\]]*\]', ' ', text)#中括號裡面有文字跟數字清理掉
    # standalone sequences of specials, matches &# but not #cool
    text = re.sub(r'(?:^|\s)[&#<>{}\[\]+|\\:-]{1,}(?:\s|$)', ' ', text)
    # standalone sequences of hyphens like --- or ==
    text = re.sub(r'(?:^|\s)[\-=\+]{2,}(?:\s|$)', ' ', text)
    # sequences of white spaces
    #text=re.sub(r'\s+', '', text)
    text=re.sub(r'/', '', text)
    text = re.sub(r'<[^<>]*>', '', text)#標記式語言刪除
    #text=re.sub(r'[^\w\s]', '', text)
    return text.strip()

df['clean_text'] = df['內容'].map(clean)




from textacy.preprocessing import replace

df['clean_text'] = df['clean_text'].map(replace.urls)
df['clean_text'] = df['clean_text'].map(replace.emails)
df['clean_text'] = df['clean_text'].map(replace.hashtags)
df['clean_text'] = df['clean_text'].map(replace.user_handles)
df['clean_text'] = df['clean_text'].map(replace.hashtags)


#重新計算文章雜訊
df['impurity'] = df['clean_text'].apply(impurity, min_len=10)



#欄位重新命名，並且將雜訊欄位移除
df.rename(columns={'內容': 'Raw_text', 'Clean_text': '內容'}, inplace=True)
df.drop(columns=['impurity'], inplace=True)



#新增欄位
df["length"]=df["clean_text"].str.len()
df.describe().T

#觀察每一個類別新聞內容長度的平均值
result = df.groupby("類別").agg({"length":"mean"}).sort_values(by="length", ascending=False).reset_index()
result_top5 = result.head(5)
