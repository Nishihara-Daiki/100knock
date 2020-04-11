"""
	47. 機能動詞構文のマイニングPermalink
	動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
	46のプログラムを以下の仕様を満たすように改変せよ．
	* 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
	* 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
	* 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
	* 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
	例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．
		返事をする      と に は        及ばんさと 手紙に 主人は
	このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
	* コーパス中で頻出する述語（サ変接続名詞+を+動詞）
	* コーパス中で頻出する述語と助詞パターン
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
		kakus, kaku_chunks = map(list, zip(*sorted(value, key=lambda x: x[0])))
		if 'を' in kakus and len(kakus) > 1:
			wo_idx = kakus.index('を')
			wo_kaku = kakus.pop(wo_idx)
			wo_kaku_chunk = kaku_chunks.pop(wo_idx)
			kaku_chunks = map(str, kaku_chunks)
			varb = str(wo_kaku_chunk) + varb
			print('{}\t{}\t{} '.format(varb, ' '.join(kakus), ' '.join(kaku_chunks)))
