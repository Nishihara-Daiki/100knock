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
# 吾輩 は -> 5
# ここ で -> 2
# 始め て -> 3
# 人間 という -> 4
# もの を -> 5
# 見 た 。 -> -1


python3 q42.py data/neko.txt.cabocha | head
# 吾輩 は	猫 で ある
# 名前 は	無い
# まだ	無い
# どこ で	生れ た か
# 生れ た か	つか ぬ
# とんと	つか ぬ
# 見当 が	つか ぬ
# 何 でも	薄暗い
# 薄暗い	所 で
# じめじめ し た	所 で


python3 q43.py data/neko.txt.cabocha | head
# どこ で	生れ た か
# 見当 が	つか ぬ
# 所 で	泣い て
# ニャーニャー	泣い て
# いた事 だけ は	記憶 し て いる
# 吾輩 は	見 た
# ここ で	始め て
# もの を	見 た
# あと で	聞く と
# 我々 を	捕え て


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



python3 q49.py data/neko.txt.cabocha


