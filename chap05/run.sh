#!/bin/bash

mkdir -p data

wget -P data https://nlp100.github.io/data/neko.txt
cat <(echo '<root>') \
	<(cat data/neko.txt | cabocha -I0 -O4 -f3) \
	<(echo '</root>') \
	> data/neko.txt.cabocha


python3 q40.py data/neko.txt.cabocha
# 　	　	記号	空白
# 吾輩	吾輩	名詞	代名詞
# は	は	助詞	係助詞
# 猫	猫	名詞	一般
# で	だ	助動詞	*
# ある	ある	助動詞	*
# 。	。	記号	句点


python3 q41.py data/neko.txt.cabocha
# 吾輩は -> 5
# ここで -> 2
# 始めて -> 3
# 人間という -> 4
# ものを -> 5
# 見た。 -> -1


python3 q42.py data/neko.txt.cabocha | head
# 吾輩は	猫である
# 名前は	無い
# まだ	無い
# どこで	生れたか
# 生れたか	つかぬ
# とんと	つかぬ
# 見当が	つかぬ
# 何でも	薄暗い
# 薄暗い	所で
# じめじめした	所で


python3 q43.py data/neko.txt.cabocha | head
# どこで	生れたか
# 見当が	つかぬ
# 所で	泣いて
# ニャーニャー	泣いて
# いた事だけは	記憶している
# 吾輩は	見た
# ここで	始めて
# ものを	見た
# あとで	聞くと
# 我々を	捕えて


python3 q44.py data/neko.txt.cabocha


python3 q45.py data/neko.txt.cabocha | head
# 生れる	で
# つく	か が
# 泣く	で
# する	だけ て は
# 始める	で
# 見る	は を
# 聞く	で
# 捕える	を
# 煮る	て
# 食う	て


python3 q46.py data/neko.txt.cabocha | head
# 生れる	で	　どこで 
# つく	か が	生れたか 見当が 
# 泣く	で	所で 
# する	だけ て は	いた事だけは 泣いて いた事だけは 
# 始める	で	ここで 
# 見る	は を	吾輩は ものを 
# 聞く	で	あとで 
# 捕える	を	我々を 
# 煮る	て	捕えて 
# 食う	て	煮て 



python3 q47.py data/neko.txt.cabocha > data/q47.txt

cat data/q47.txt | cut -f1 -d '	' | sort | uniq -c | sort -r | head -n5
#  34 事を云う
#  31 顔をする
#  29 事をする
#  25 返事をする
#  19 挨拶をする

cat data/q47.txt | cut -f1,2 -d '	' | sort | uniq -c | sort -r | head -n5
#   9 心を置く	に
#   6 事をする	に
#   5 心を取る	に ば
#   5 人を思う	と
#   4 挨拶をする	から



python3 q48.py data/neko.txt.cabocha | head
# 一
# 吾輩は -> 猫である。
# 猫である。
# 名前は -> 無い。
# 　どこで -> 生れたか -> つかぬ。
# 見当が -> つかぬ。
# 何でも -> 薄暗い -> 所で -> 泣いて -> 記憶している。
# 所で -> 泣いて -> 記憶している。
# ニャーニャー -> 泣いて -> 記憶している。
# いた事だけは -> 記憶している。



python3 q49.py data/neko.txt.cabocha | head -n 20
# Xは -> Yである。
# 　Xで -> 生れたか | Yが | つかぬ。
# Xでも -> 薄暗い -> Yで
# Xでも -> 薄暗い -> Yで | Y | 泣いて
# Xでも -> 薄暗い -> Yで -> 泣いて | Yだけは | 記憶している。
# Xでも -> 薄暗い -> Yで -> 泣いて -> Yしている。
# Xで | Y | 泣いて
# Xで -> 泣いて | Yだけは | Yしている。
# Xで -> 泣いて -> Yしている。
# X -> 泣いて | Yだけは | Yしている。
# X -> 泣いて -> Yしている。
# Xだけは -> Yしている。
# Xは | Yで -> 始めて -> 人間という -> ものを | 見た。
# Xは | Yという -> ものを | 見た。
# Xは | Yを | 見た。
# Xで -> 始めて -> Yという
# Xで -> 始めて -> Yという -> Yを
# Xという -> Yを
# Xで -> 聞くと | Yは | 種族であったそうだ。
# Xで -> 聞くと | Yという -> 人間中で | 種族であったそうだ。


