# 以下を「app.py」に書き込み

import os
from google.cloud import texttospeech
import requests
import io
import streamlit as st
from PIL import Image

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'onseigousei_secret.json'

def synthesize_speech(text, lang='日本語', gender='female'):
    gender_type = {
        'defalut': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
        'male': texttospeech.SsmlVoiceGender.MALE,
        'female': texttospeech.SsmlVoiceGender.FEMALE,
        'neutral': texttospeech.SsmlVoiceGender.NEUTRAL
    }
    lang_code = {
        '英語': 'en-US',
        '日本語': 'ja-JP'
    }
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=lang_code[lang], ssml_gender=gender_type[gender],name="ja-JP-Wavenet-D"
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response

import urllib.request

def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def mv_app(video_file_url, video_filename):
#    st.title('Video Player')
    if st.button('Play Video'):
#        video_file_url = 'https://drive.google.com/uc?export=download&id=YourFileID'  # Google Driveの動画ファイルのIDを指定してください
#        video_filename = 'video.mp4'
        download_file(video_file_url, video_filename)
        video_file = open(video_filename, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)


st.title('専門基礎３学期パーフェクトアプリ')

st.markdown('##### 問１　以下は、マイクロメータの測定誤差がでる原因である。')
st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ５問全て選んでから判定します。')
input_option1_1 = st.selectbox(
    '問1.1　（　　）調整を正しく行わなかった。',
    ('選んでください', '満点', '零点', '赤点','楽点',)
)
input_option1_2 = st.selectbox(
    '問1.2　マイクロメータの（　　）方法による誤差。',
    ('選んでください', '私事', '師事', '指示','支持',)
)
input_option1_3 = st.selectbox(
    '問1.3　測定面が正しく測定物に当たっていない。（（　　）て測定したとき）',
    ('選んでください', '傾け', '外向け', '内向け','下向け',)
)
input_option1_4 = st.selectbox(
    '問1.4　温度変化による誤差（測定時間が長いと、（　　）が伝わり金属は伸びます。）',
    ('選んでください', '室温', '内温', '外温','体温',)
)
input_option1_5 = st.selectbox(
    '問1.5　測定物を測定するときのラチェットストップを回す（　　）の誤差。',
    ('選んでください', '力', '音', '振動','意思',)
)
n_ok=0
input_data = None
if input_option1_1 == '零点':
    n_ok =n_ok+1 
if input_option1_2 == '支持':
    n_ok=n_ok+1 
if input_option1_3 == '傾け':
    n_ok=n_ok+1 
if input_option1_4 == '体温':
    n_ok=n_ok+1 
if input_option1_5 == '力':
    n_ok=n_ok+1
if n_ok==5:
    st.write('全問正解です。音声で確認してください。')
    input_data = '　　マイクロメータの測定誤差がでる原因は以下のようなものがあります。\
    零点調整を正しく行わなかった。\
    読み取り誤差。シンプルの数値を確定するためにスリーブの線に合わせて見ますが、目の位置や見る角度によって、誤差が出ます。\
    温度変化による誤差。測定時間が長いと、体温が伝わり金属は伸びます。マイクロメータの支持方法による誤差。\
    測定物を測定するときのラチェットストップを回す力の誤差。測定面が正しく測定物に当たっていない。傾けて測定したとき。\
    などです。'

    if st.button('問１の解答'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='female')
        st.audio(response.audio_content)
else :
    st.write('不正解です。何処かが間違っています。見直してください。')
st.write('')
st.write('')
st.write('')
st.write('')

st.markdown('##### 問２　以下は、マイクロメータの読み方についてである。')
st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ３問全て選んでから判定します。')
input_option2_1 = st.selectbox(
    '問2.1　マイクロメータのシンブルとスピンドルは一体で回転し、１回転（　　）mm正確に動きます。',
    ('選んでください','0.1', '0.5', '1.0',)
)
input_option2_2 = st.selectbox(
    '問2.2　シンブルの外周は、５０等分した目盛りが刻まれており、１目盛り（　　）mmになっています。',
    ('選んでください', '0.01', '0.05', '0.10',)
)
input_option2_3 = st.selectbox(
    '問2.3　マイクロメータを使うときはラチェットを（　　）かに回す',
    ('選んでください', '静', '賑や','遥')
)

n_ok=0
input_data = None
if input_option2_1 == '0.5':
    n_ok =n_ok+1 
if input_option2_2 == '0.01':
    n_ok=n_ok+1 
if input_option2_3 == '静':
    n_ok=n_ok+1 
if n_ok==3:
    st.write('全問正解です。音声で確認してください。')
    input_data = '　　マイクロメータの読み方については、以下の通りです。\
    マイクロメータのシンブルとスピンドルは一体で回転し、１回転0.5mm正確に動きます。\
    シンブルの外周は、５０等分した目盛りが刻まれており、１目盛り0.01mmになっています。\
    マイクロメータを使うときはラチェットを静かに回す。'

    if st.button('問２の解答'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='female')
        st.audio(response.audio_content)
else :
    st.write('不正解です。何処かが間違っています。見直してください。')
st.write('')
st.write('')
st.write('')
st.write('')

st.markdown('##### 問３　以下の図で示したマイクロメータの各部の名称を答えなさい')
st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ７問全て選んでから判定します。')
image = Image.open('maikuro_name.jpg')
st.image(image,use_column_width=True)

input_option3_1 = st.selectbox(
    '①の名称',('選んでください','クランプ', 'シンブル', 'ラチェット',\
    'アンビル','フレーム', 'スピンドル', 'スリーブ')
)
input_option3_2 = st.selectbox(
    '②の名称',('選んでください','クランプ', 'シンブル', 'ラチェット',\
    'アンビル','フレーム', 'スピンドル', 'スリーブ')
)
input_option3_3 = st.selectbox(
    '③の名称',('選んでください','クランプ', 'シンブル', 'ラチェット',\
    'アンビル','フレーム', 'スピンドル', 'スリーブ')
)
input_option3_4 = st.selectbox(
    '④の名称',('選んでください','クランプ', 'シンブル', 'ラチェット',\
    'アンビル','フレーム', 'スピンドル', 'スリーブ')
)
input_option3_5 = st.selectbox(
    '⑤の名称',('選んでください','クランプ', 'シンブル', 'ラチェット',\
    'アンビル','フレーム', 'スピンドル', 'スリーブ')
)
input_option3_6 = st.selectbox(
    '⑥の名称',('選んでください','クランプ', 'シンブル', 'ラチェット',\
    'アンビル','フレーム', 'スピンドル', 'スリーブ')
)
input_option3_7 = st.selectbox(
    '⑦の名称',('選んでください','クランプ', 'シンブル', 'ラチェット',\
    'アンビル','フレーム', 'スピンドル', 'スリーブ')
)

n_ok=0
input_data = None
if input_option3_1 == 'アンビル':
    n_ok =n_ok+1 
if input_option3_2 == 'スピンドル':
    n_ok=n_ok+1 
if input_option3_3 == 'スリーブ':
    n_ok=n_ok+1 
if input_option3_4 == 'ラチェット':
    n_ok=n_ok+1
if input_option3_5 == 'フレーム':
    n_ok=n_ok+1 
if input_option3_6 == 'クランプ':
    n_ok=n_ok+1 
if input_option3_7 == 'シンブル':
    n_ok=n_ok+1  
if n_ok==7:
    st.write('マイクロメータの名称、全問正解です。')
else :
    st.write('不正解です。何処かが間違っています。見直してください。')
st.write('')
st.write('')
st.write('')


st.markdown('##### 問４　以下の動画を視聴してから問いに答えなさい')
if st.button('問４：Play Video'):
    file_id = "1zI1o33IiblGtTmogzuuRxNhRZbrRbIsd" # 共有リンクからファイルIDを抽出
    download_link = f"https://drive.google.com/uc?id={file_id}" # ダウンロードリンクを生成
    response = requests.get(download_link)  # モデルをダウンロード
    with open("m1.mp4", "wb") as f: # モデルファイルを保存
        f.write(response.content)
    st.video("m1.mp4")

st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ３問全て選んでから判定します。')
input_option4_1 = st.selectbox(
    '問4.1　平均値を求めるエクセルの関数を選びなさい',
    ('選んでください', '=AVERAGE()', '=MEDIAN()', '=MODE()')
)
input_option4_2 = st.selectbox(
    '問4.2　中央値を求めるエクセルの関数を選びなさい',
    ('選んでください', '=AVERAGE()', '=MEDIAN()', '=MODE()')
)
input_option4_3 = st.selectbox(
    '問4.3　最頻値を求めるエクセルの関数を選びなさい',
    ('選んでください', '=AVERAGE()', '=MEDIAN()', '=MODE()')
)
n_ok=0
input_data = None
if input_option4_1 == '=AVERAGE()':
    n_ok =n_ok+1 
if input_option4_2 == '=MEDIAN()':
    n_ok=n_ok+1 
if input_option4_3 == '=MODE()':
    n_ok=n_ok+1 
if n_ok==3:
    st.write('全問正解です。')
else :
    st.write('不正解です。何処かが間違っています。動画を見直してください。')
st.write('')
st.write('')
st.write('')


st.markdown('##### 問５　以下の動画を視聴してから問いに答えなさい')
if st.button('問５：Play Video'):
    file_id = "1tYKDUikEnwG5sBU84nrYVBbh8HrJbSqh" # 共有リンクからファイルIDを抽出
    download_link = f"https://drive.google.com/uc?id={file_id}" # ダウンロードリンクを生成
    response = requests.get(download_link)  # モデルをダウンロード
    with open("m2.mp4", "wb") as f: # モデルファイルを保存
        f.write(response.content)
    st.video("m2.mp4")

st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ３問全て選んでから判定します。')
input_option5_1 = st.selectbox(
    '問5.1　最大値を求めるエクセルの関数を選びなさい',
    ('選んでください', '=MAX()', '=MINN()', '=(最大値)-(最小値)')
)
input_option5_2 = st.selectbox(
    '問5.2　最小値を求めるエクセルの関数を選びなさい',
    ('選んでください', '=MAX()', '=MINN()', '=(最大値)-(最小値)')
)
input_option5_3 = st.selectbox(
    '問5.3　範囲を求めるエクセルの関数を選びなさい',
    ('選んでください', '=MAX()', '=MINN()', '=(最大値)-(最小値)')
)
n_ok=0
input_data = None
if input_option5_1 == '=MAX()':
    n_ok =n_ok+1 
if input_option5_2 == '=MINN()':
    n_ok=n_ok+1 
if input_option5_3 == '=(最大値)-(最小値)':
    n_ok=n_ok+1 
if n_ok==3:
    st.write('全問正解です。')
else :
    st.write('不正解です。何処かが間違っています。動画を見直してください。')
st.write('')
st.write('')
st.write('')

#https://drive.google.com/file/d/1UnimUwdLjS4Y3TKSRtOsqq18cQERflbD/view?usp=sharing
st.markdown('##### 問６　以下の動画を視聴してから問いに答えなさい')
if st.button('問６：Play Video'):
    file_id = "1UnimUwdLjS4Y3TKSRtOsqq18cQERflbD" # 共有リンクからファイルIDを抽出
    download_link = f"https://drive.google.com/uc?id={file_id}" # ダウンロードリンクを生成
    response = requests.get(download_link)  # モデルをダウンロード
    with open("m3.mp4", "wb") as f: # モデルファイルを保存
        f.write(response.content)
    st.video("m3.mp4")
image3 = Image.open('toi3.jpg')
st.image(image3,use_column_width=True)
st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ２問全て選んでから判定します。')
input_option6_1 = st.selectbox(
    '問6.1　C7セルに入れる関数を選びなさい',
    ('選んでください', '=IF(C7>=0,"OK","NG")', '=$B$4-$C$4*B7', '=IF(C7>=0,"NG","OK")')
)
input_option6_2 = st.selectbox(
    '問6.2　D7セルに入れる関数を選びなさい',
    ('選んでください', '=IF(C7>=0,"OK","NG")', '=$B$4-$C$4*B7', '=IF(C7>=0,"NG","OK")')
)
n_ok=0
input_data = None
if input_option6_1 == '=$B$4-$C$4*B7':
    n_ok =n_ok+1 
if input_option6_2 == '=IF(C7>=0,"OK","NG")':
    n_ok=n_ok+1 
if n_ok==2:
    st.write('全問正解です。')
else :
    st.write('不正解です。何処かが間違っています。動画を見直してください。')
st.write('')
st.write('')
st.write('')

#https://drive.google.com/file/d/18Kwu9foqxlTzUSwdgbunvW4Nld_4ApW3/view?usp=sharing
st.markdown('##### 問７　以下の動画を視聴してから問いに答えなさい')
if st.button('問７：Play Video'):
    file_id = "18Kwu9foqxlTzUSwdgbunvW4Nld_4ApW3" # 共有リンクからファイルIDを抽出
    download_link = f"https://drive.google.com/uc?id={file_id}" # ダウンロードリンクを生成
    response = requests.get(download_link)  # モデルをダウンロード
    with open("m4.mp4", "wb") as f: # モデルファイルを保存
        f.write(response.content)
    st.video("m4.mp4")

st.markdown('##### 適する用語をプルダウンからを選んでください。')
#st.markdown('##### ３問全て選んでから判定します。')
input_option7_1 = st.selectbox(
    '問4.1　相関係数を求めるエクセルの関数を選びなさい',
    ('選んでください', '=CORREL(C4:C8,D4:D8)', '=CORREL(C4,D4)', '=CORREL(C4:C8)')
)

n_ok=0
input_data = None
if input_option7_1 == '=CORREL(C4:C8,D4:D8)':
    n_ok =n_ok+1 
if n_ok==1:
    st.write('正解です。')
else :
    st.write('不正解です。何処かが間違っています。動画を見直してください。')
st.write('')
st.write('')
st.write('')

# https://drive.google.com/file/d/1N4oz_jj1KfLtX_jCrLZCPb7sVmg52754/view?usp=sharing
st.markdown('##### 問８　以下の動画を視聴してから問いに答えなさい')
if st.button('問８：Play Video'):
    file_id = "1N4oz_jj1KfLtX_jCrLZCPb7sVmg52754" # 共有リンクからファイルIDを抽出
    download_link = f"https://drive.google.com/uc?id={file_id}" # ダウンロードリンクを生成
    response = requests.get(download_link)  # モデルをダウンロード
    with open("m5.mp4", "wb") as f: # モデルファイルを保存
        f.write(response.content)
    st.video("m5.mp4")
image8 = Image.open('toi7.jpg')
st.image(image8,use_column_width=True)
st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ２問全て選んでから判定します。')
input_option8_1 = st.selectbox(
    '問8.1　エクセルのグラフにおいてオプションを追加するボタンはどれか',
    ('選んでください', '+', '-', '*')
)
input_option8_2 = st.selectbox(
    '問8.2　グラフにおいて外れ値は誰か',
    ('選んでください', 'A', 'B', 'C', 'D')
)
n_ok=0
input_data = None
if input_option8_1 == '+':
    n_ok =n_ok+1 
if input_option8_2 == 'D':
    n_ok=n_ok+1 
if n_ok==2:
    st.write('全問正解です。')
else :
    st.write('不正解です。何処かが間違っています。動画を見直してください。')
st.write('')
st.write('')
st.write('')

# https://drive.google.com/file/d/1qa4j5mNrAKrGM_Zu_0W09NBZtKmEfnOa/view?usp=sharing
st.markdown('##### 問９　以下の動画を視聴してから問いに答えなさい')
if st.button('問９：Play Video'):
    file_id = "1qa4j5mNrAKrGM_Zu_0W09NBZtKmEfnOa" # 共有リンクからファイルIDを抽出
    download_link = f"https://drive.google.com/uc?id={file_id}" # ダウンロードリンクを生成
    response = requests.get(download_link)  # モデルをダウンロード
    with open("m6.mp4", "wb") as f: # モデルファイルを保存
        f.write(response.content)
    st.video("m6.mp4")
image9 = Image.open('toi9.jpg')
st.image(image9,use_column_width=True)
st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ３問全て選んでから判定します。')
input_option9_1 = st.selectbox(
    '問9.1　C4セルに入れる乱数の関数を選びなさい',
    ('選んでください', '=RANDBETWEEN(10)', '=RANDBETWEEN(1)', '=RANDBETWEEN(1,10)')
)
input_option9_2 = st.selectbox(
    '問9.2　D4セルに入れる関数を選びなさい',
    ('選んでください', '=IF(C4=0,"OK","NG")', '=IF(C4=1,"OK","NG")', '=IF(C4=1,"NG","OK")')
)
input_option9_3 = st.selectbox(
    '問9.3　再試行させる場合のキーを選びなさい',
    ('選んでください', 'F4', 'F7', 'F9')
)
n_ok=0
input_data = None
if input_option9_1 == '=RANDBETWEEN(1,10)':
    n_ok =n_ok+1 
if input_option9_2 == '=IF(C4=1,"OK","NG")':
    n_ok=n_ok+1 
if input_option9_3 == 'F9':
    n_ok=n_ok+1 
if n_ok==3:
    st.write('全問正解です。')
else :
    st.write('不正解です。何処かが間違っています。動画を見直してください。')
st.write('')
st.write('')
st.write('')



st.markdown('### 問題は以上です。')










