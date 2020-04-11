"""
	49. 名詞間の係り受けパスの抽出Permalink
	文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
	ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．
	* 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）
	  を” -> “で連結して表現する
	* 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
	また，係り受けパスの形状は，以下の2通りが考えられる．
	* 文節iから構文木の根に至る経路上に文節jが存在する場合:
	  文節iから文節jのパスを表示
	* 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから
	  文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を” | “で連結して表示
	例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）
	から，次のような出力が得られるはずである．
		Xは | Yで -> 始めて -> 人間という -> ものを | 見た
		Xは | Yという -> ものを | 見た
		Xは | Yを | 見た
		Xで -> 始めて -> Y
		Xで -> 始めて -> 人間という -> Y
		Xという -> Y
"""

from q41 import q41
from q48 import get_chunk_to_root
from itertools import combinations

sentences = q41()

for sentence in sentences:
	chunks = [chunk for chunk in sentence if chunk.has_pos('名詞')]
	for i, j in combinations(chunks, 2):
		for n in range(len(i.morphs)):
			if i.morphs[n].pos == '名詞':
				i.morphs[n].surface = 'X'
		for n in range(len(j.morphs)):
			if j.morphs[n].pos == '名詞':
				j.morphs[n].surface = 'Y'
		path_i = get_chunk_to_root(i, sentence)
		path_j = get_chunk_to_root(j, sentence)
		if j in path_i:	# i -> j
			idx = path_i.index(j)
			path_i = path_i[:idx+1]
			print(' -> '.join(map(str, path_i)))
		else:	# i -> k,   j -> k
			overlap_num = len(set(path_i) & set(path_j))
			k = path_i[len(path_i) - overlap_num]
			path_i2k = map(str, path_i[:len(path_i) - overlap_num])
			path_j2k = map(str, path_j[:len(path_j) - overlap_num])
			print('{} | {} | {}'.format(' -> '.join(path_i2k), ' -> '.join(path_j2k), k))