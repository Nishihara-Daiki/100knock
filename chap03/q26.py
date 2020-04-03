"""
	26. 強調マークアップの除去
	25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
"""

from q25 import q25

def q26():
	key2val = q25()

	for key in key2val:
		key2val[key] = key2val[key].replace("'''''", '').replace("'''", '').replace("''", '')

	return key2val

if __name__ == '__main__':
	print(q26())
