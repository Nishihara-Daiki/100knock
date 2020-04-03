"""
	27. 内部リンクの除去
	26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
"""

from q26 import q26
import re

def q27():
	key2val = q26()

	r = re.compile(r'\[\[([^|\]]*)(\|.*)*\]\]')

	for key,val in key2val.items():
		key2val[key] = r.sub('\\1', val)

	return key2val


if __name__ == '__main__':
	print(q27())
