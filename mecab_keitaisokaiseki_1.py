"""
このプログラムはNEologed辞書を使ったMeCab形態素解析プログラムです.

"""

import MeCab
import sys, codecs
import pandas as pd
import os

#作業ディレクトリの指定
os.chdir('"作業ディレクトリ"')

#辞書を指定
m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

#ファイルの読み込み
t = open(""解析したいファイル"", 'rb').read()
text = t.decode('UTF-8')

#空の文字列にparse(構文解析)することでバグを防ぐ
m.parse('')
node = m.parseToNode(text)


while node:
    #単語を取得
    word = node.surface
    #品詞を取得
    pos = node.feature.split(",")[1]
    #print(word, pos)
    #以前のコード：
    print('{},{}'.format(word, pos))
    #これが動かなかった
    
    #次の単語に進める
    node = node.next
    
