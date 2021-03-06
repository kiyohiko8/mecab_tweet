"""
このプログラムはNEologed辞書を使った最新版MeCab形態素解析プログラム(一般・固有名詞抽出版)です.
+ できること
	- 読み込んだテキストの形態素解析
	- NEologdを用いた固有名詞抽出
	- 抽出した名詞を分かち書き化
"""
#必要なモジュールのインポート
import MeCab
import sys, codecs
import pandas as pd
import numpy as np
import os

#作業ディレクトリの指定
os.chdir('"作業ディレクトリ"')

#辞書を指定
m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

#ファイルの読み込み
t = open(""ファイル名"", 'rb').read()
text = t.decode('UTF-8')


#wordlistの作成
wordlist = []
#空の文字列にparse(構文解析)することでバグを防ぐ
m.parse('')
node = m.parseToNode(text)



while node:
    #単語を取得
    word = node.surface
    #品詞を取得
    pos = node.feature.split(",")[1]
    if pos == "一般":
    	wordlist.append(word)
    	
    elif pos == "固有名詞":
    	wordlist.append(word)
    
    #次の単語に進める
    node = node.next
    
wordlist2 = np.array(wordlist)
    
    
#ツイートを分かち書きしたものを表示する
wakati = wordlist2
wakati = " ".join(wakati)
print(wakati)


"""    
####形態素解析
#語と品詞の配列を作成
wordlist = []

#空の文字列にparseすることでバグを防ぐ
m.parse('')
node = m.parseToNode(text)

while node:
    #単語を取得
    word = node.surface
    
    #品詞を取得
    pos = node.feature.split(",")[1]
    
    #それぞれを配列に追加
    wordlist.append([word, pos])
    
    #次の単語に進める
    node = node.next
    
wordlist2 = np.array(wordlist)
    
print(wordlist2)
    
    
####分かち書きテキストの作成
#ツイートを分かち書きしたものを表示する
wakati = wordlist2
wakati = " ".join(wakati)
print(wakati)
"""

