<!-- 🧋 奶茶風 README：金融新聞文本探勘與台股指數關聯性分析 -->

<p align="center">
  <img src="https://github.com/Sandyzhen/TWStockNews-NLP-Analysis/blob/main/image/%E9%87%91%E8%9E%8D%E6%96%87%E6%9C%AC.png" width="1000px" alt="Financial News Project Banner"/>
</p>

## 專案內容
以文本探勘結合台股資料，分析市場情緒與股價波動的潛在關聯。  
本專案針對鉅亨網新聞進行爬蟲、清理與關鍵字分析，並比對特定關鍵字（如「台積電」「輝達」）與台股指數、台積電股價的變化趨勢。

---

## 專案特色

🔍 擷取 2023/5/14–5/31 的鉅亨新聞共 1,537 篇  
📊 結合台積電與加權股價指數，分析關鍵詞出現頻率  
🧹 進行雜訊過濾與文本清理：去除網址、email、hashtag、HTML轉義字元等  
📈 使用關鍵字次數 vs. 指數變動趨勢圖表觀察潛在關聯  
☁️ 製作文字雲視覺化台積電與輝達相關新聞核心詞彙  

---

## 使用技術套件
![Python](https://img.shields.io/badge/PYTHON-6E6A75?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/PANDAS-7C7782?style=for-the-badge&logo=pandas&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BEAUTIFULSOUP-998B82?style=for-the-badge)
![Jieba](https://img.shields.io/badge/JIEBA-%E6%96%87%E5%AD%97%E6%96%B7%E8%A9%9E-AE9E8E?style=for-the-badge)
![WordCloud](https://img.shields.io/badge/WORDCLOUD-CBBFA5?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/MATPLOTLIB-D5C8A1?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/JUPYTER-EFE4CF?style=for-the-badge&logo=jupyter)





---
## 📁 專案架構
financial-news-analysis/
├── data/
│   └── 鉅亨新聞.csv                     # 已爬取的鉅亨網新聞資料
│
├── scripts/
│   ├── crawler.py # 爬蟲腳本：抓取鉅亨網最新新聞
│   ├── cleaner.py # 資料清理模組：移除 HTML 標籤與特殊符號
│   └── keyword_analysis and visualization.py # 關鍵詞分析與視覺化（長條圖、折線圖、文字雲）
│
├── report/
│   └── 金融大數據報告.pdf            # 專案分析報告與結果彙整
│
└── README.md                        # 專案說明與使用說明（建議補上）

---

## 專案成果展示
### 「輝達、台積電」相關文章進行情感與關鍵詞分析的文字雲視覺化
![TSMC Wordcloud](https://github.com/Sandyzhen/TWStockNews-NLP-Analysis/blob/main/image/%E5%8F%B0%E7%A9%8D.png)
![TSMC Wordcloud](https://github.com/Sandyzhen/TWStockNews-NLP-Analysis/blob/main/image/%E8%BC%9D%E9%81%94.png)



---

