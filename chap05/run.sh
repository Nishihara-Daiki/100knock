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


python3 q45.py data/neko.txt.cabocha


python3 q46.py data/neko.txt.cabocha


python3 q47.py data/neko.txt.cabocha


python3 q48.py data/neko.txt.cabocha


python3 q49.py data/neko.txt.cabocha


