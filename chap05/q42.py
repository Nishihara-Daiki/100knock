"""
	42. 係り元と係り先の文節の表示
	係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
	ただし，句読点などの記号は出力しないようにせよ．
"""

from q41 import q41

sentences = q41()

for sentence in sentences:
	for chunk in sentence:
		if chunk.dst != -1:
			chunk_s = ''.join(morph.surface for morph in chunk.morphs if morph.pos != '記号')
			dstchunk_s = ''.join(morph.surface for morph in sentence[chunk.dst].morphs if morph.pos != '記号')
			if chunk_s and dstchunk_s:
				print(chunk_s + '\t' + dstchunk_s)
