# 以下を「app.py」に書き込み
import streamlit as st
import requests
import json
import torch
from transformers import BertForMaskedLM
from transformers import BertTokenizer
from transformers import BertForSequenceClassification, BertConfig
from transformers import BertJapaneseTokenizer
from transformers import BertForSequenceClassification, BertJapaneseTokenizer


st.write("モデルを読み込んでいます！")
import os

# 共有リンクからファイルIDを抽出
file_id = "1-1ZDrx8LvR4wdD654sBdua2il7l20Q-n"

# ダウンロードリンクを生成
download_link = f"https://drive.google.com/uc?id={file_id}"

# モデルをダウンロード
response = requests.get(download_link)

# モデルファイルを保存
with open("pytorch_model.bin", "wb") as f:
    f.write(response.content)

st.write("モデルを読み込みました1！")

# モデルを読み込む
loaded_model = BertForSequenceClassification.from_pretrained(
    "cl-tohoku/bert-base-japanese-whole-word-masking",  # 正しいモデル識別子を指定
    num_labels=9  # ラベルの数を指定（必要に応じて調整）
)

# モデルの保存
torch.save(loaded_model.state_dict(), "pytorch_model.bin")
# モデルの読み込み
loaded_model.load_state_dict(torch.load("pytorch_model.bin"))
st.write("モデルを読み込みました2！")

url3='.'
loaded_tokenizer = BertJapaneseTokenizer.from_pretrained(url3)
st.write("モデルを読み込みました3！")

st.title("「ニュースの分類」アプリ")
st.write("")
st.write("###### モデル ：Pretrained, Japanese BERT models （東北大学　乾研究室）")
st.write("###### ファインチューニングのコーパス：Livedoorニュースコーパス（ldcc-20140209.tar.gz）")
st.write("###### 分類クラス：「dokujo-tsushin」,「it-life-hack」,「kaden-channel」,「livedoor-homme」,「movie-enter」,「peachy」,「smax」,「sports-watch」,「topic-news」")
st.write("")
dirs=["「dokujo-tsushin」","「it-life-hack」","「kaden-channel」","「livedoor-homme」","「movie-enter」","「peachy」","「smax」","「sports-watch」","「topic-news」"]
text =  st.text_area("ニュースの記事を入力してください。", "首位・阪神は2位・広島との直接対決の初戦を制し、\
今季5度目の6連勝を飾った。チームは75勝44敗4分で貯金は今季最多の31、優勝マジックを「10」に減らした。\
今季19度目先発の村上頌樹（25）は、7回1/3（100球）を投げ、6安打1失点、四死球0の好投。\
自身初の2桁10勝目を挙げた。", height=250)

sample_text = text
sample_text = sample_text.translate(str.maketrans({"\n":"", "\t":"", "\r":"", "\u3000":""}))


max_length = 512
words = loaded_tokenizer.tokenize(sample_text)
word_ids = loaded_tokenizer.convert_tokens_to_ids(words)  # 単語をインデックスに変換
word_tensor = torch.tensor([word_ids[:max_length]])  # テンソルに変換

x = word_tensor  # GPU対応
y = loaded_model(x)  # 予測
pred = y[0].argmax(-1)  # 最大値のインデックス
st.write("## 予測結果")
st.write("## result:", dirs[pred])

st.write("")

st.write("")



