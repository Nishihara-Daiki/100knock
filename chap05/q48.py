"""
	48. 名詞から根へのパスの抽出Permalink
	文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
	ただし，構文木上のパスは以下の仕様を満たすものとする．
	* 各文節は（表層形の）形態素列で表現する
	* パスの開始文節から終了文節に至るまで，各文節の表現を” -> “で連結する
	「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，
	次のような出力が得られるはずである．
		吾輩は -> 見た
		ここで -> 始めて -> 人間という -> ものを -> 見た
		人間という -> ものを -> 見た
		ものを -> 見た
"""

from q41 import q41

sentences = q41()


def get_chunk_to_root(chunk, sentence):
	chunk_chain = list()
	while True:
		chunk_chain.append(chunk)
		if chunk.dst == -1:
			break
		chunk = sentence[chunk.dst]
	return chunk_chain


if __name__ == '__main__':
	for sentence in sentences:
		for chunk in sentence:
			if chunk.find_morph(pos='名詞'):
				chunk_chain = get_chunk_to_root(chunk, sentence)
				if chunk_chain:
					chunk_chain = map(str, chunk_chain)
					print(' -> '.join(chunk_chain))
