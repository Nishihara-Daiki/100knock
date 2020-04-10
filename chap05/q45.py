"""
	45. 動詞の格パターンの抽出Permalink
	今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 
	動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． 
	ただし，出力は以下の仕様を満たすようにせよ．
	* 動詞を含む文節において，最左の動詞の基本形を述語とする
	* 述語に係る助詞を格とする
	* 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
	「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
	この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
	「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
		始める  で
		見る    は を
"""

from q41 import q41
from collections import defaultdict

sentences = q41()

for sentence in sentences:
	idx_varb2joshi = defaultdict(list)
	for chunk in sentence:
		kakus = chunk.find_morph_surface(pos='助詞')
		jutugos = sentence[chunk.dst].find_morph(pos='動詞')
		if kakus and jutugos and chunk.dst != -1:
			key = str(chunk.dst) + ' ' + jutugos[0].base
			idx_varb2joshi[key] += kakus

	for key,value in sorted(idx_varb2joshi.items()):
		print('{}\t{}'.format(key.split(' ')[1], ' '.join(sorted(value))))
