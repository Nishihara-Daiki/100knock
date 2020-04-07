#!/bin/bash

mkdir -p data

wget -P data https://nlp100.github.io/data/neko.txt
cat <(echo '<root>') \
	<(cat data/neko.txt | cabocha -I0 -O4 -f3) \
	<(echo '</root>') \
	> data/neko.txt.cabocha


python3 q40.py data/neko.txt.cabocha
# 　	記号	空白	　
# 吾輩	名詞	代名詞	吾輩
# は	助詞	係助詞	は
# 猫	名詞	一般	猫
# で	助動詞	*	だ
# ある	助動詞	*	ある
# 。	記号	句点	。


python3 q41.py data/neko.txt.cabocha


python3 q42.py data/neko.txt.cabocha


python3 q43.py data/neko.txt.cabocha


python3 q44.py data/neko.txt.cabocha


python3 q45.py data/neko.txt.cabocha


python3 q46.py data/neko.txt.cabocha


python3 q47.py data/neko.txt.cabocha


python3 q48.py data/neko.txt.cabocha


python3 q49.py data/neko.txt.cabocha


