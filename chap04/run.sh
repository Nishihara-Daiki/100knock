#!/bin/bash

mkdir -p data

# cd data
# wget https://nlp100.github.io/data/neko.txt
# cd ..

# # MeCabのオプションでJSON形式にしておく
# cat data/neko.txt | mecab --bos-format="[" --node-format='{"surface":"%m","base":"%f[6]","pos":"%f[0]","pos1":"%f[1]"},' --eos-format="]\n" | sed 's/,]/]/g'> data/neko.txt.mecab


# python3 q30.py data/neko.txt.mecab | head
# # [[{'base': '一', 'pos': '名詞', 'pos1': '数', 'surface': '一'}],
# #  [],
# #  [{'base': '\u3000', 'pos': '記号', 'pos1': '空白', 'surface': '\u3000'},
# #   {'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞', 'surface': '吾輩'},
# #   {'base': 'は', 'pos': '助詞', 'pos1': '係助詞', 'surface': 'は'},
# #   {'base': '猫', 'pos': '名詞', 'pos1': '一般', 'surface': '猫'},
# #   {'base': 'だ', 'pos': '助動詞', 'pos1': '', 'surface': 'で'},
# #   {'base': 'ある', 'pos': '助動詞', 'pos1': '', 'surface': 'ある'},
# #   {'base': '。', 'pos': '記号', 'pos1': '句点', 'surface': '。'}],
# #  [{'base': '名前', 'pos': '名詞', 'pos1': '一般', 'surface': '名前'},


# python3 q31.py data/neko.txt.mecab | head -n5
# # 生れ
# # つか
# # し
# # 泣い
# # し


# python3 q32.py data/neko.txt.mecab | head -n5
# # 生れる
# # つく
# # する
# # 泣く
# # する


# python3 q33.py data/neko.txt.mecab | head -n5
# # 見当
# # 記憶
# # 話
# # 装飾
# # 突起


# python3 q34.py data/neko.txt.mecab | head -n5
# # 彼 の 掌
# # 掌 の 上
# # 書生 の 顔
# # はず の 顔
# # 顔 の 真中


# python3 q35.py data/neko.txt.mecab | head
# # 一
# #
# #  吾輩 猫 
# # 名前 
# #
# #  どこ 見当 
# # 何 所 ニャーニャー いた事 記憶 
# # 吾輩 ここ 人間 もの 
# #  あと それ 書生 人間中 一番獰悪 種族 そう 
# #  書生 の 我々 話 



python3 q36.py data/neko.txt.mecab


python3 q37.py data/neko.txt.mecab


python3 q38.py data/neko.txt.mecab


python3 q39.py data/neko.txt.mecab

