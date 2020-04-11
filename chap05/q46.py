"""
	46. 動詞の格フレーム情報の抽出Permalink
	45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
	45の仕様に加えて，以下の仕様を満たすようにせよ．
	* 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
	* 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
	「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． 
	この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
	「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
		始める  で      ここで
		見る    は を   吾輩は ものを
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
			idx_varb2joshi[key] += [(k, chunk) for k in kakus]

	for key,value in sorted(idx_varb2joshi.items()):
		varb = key.split(' ')[1]
		kakus, kaku_chunks = zip(*sorted(value, key=lambda x: x[0]))
		kaku_chunks = map(str, kaku_chunks)
		print('{}\t{}\t{} '.format(varb, ' '.join(kakus), ' '.join(kaku_chunks)))
