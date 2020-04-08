"""
	43. 名詞を含む文節が動詞を含む文節に係るものを抽出Permalink
	名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
	ただし，句読点などの記号は出力しないようにせよ．
"""

from q41 import q41

sentences = q41()

for sentence in sentences:
	for chunk in sentence:
		if chunk.dst != -1 and '名詞' in {m.pos for m in chunk.morphs} and '動詞' in {m.pos for m in sentence[chunk.dst].morphs}:
			chunk_s = ' '.join(m.surface for m in chunk.morphs if m.pos != '記号')
			dstchunk_s = ' '.join(m.surface for m in sentence[chunk.dst].morphs if m.pos  != '記号')
			if chunk_s and dstchunk_s:
				print('{}\t{}'.format(chunk_s, dstchunk_s))
