"""
	28. MediaWikiマークアップの除去
	27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""

from q27 import q27
import re

def q28():
	key2val = q27()

	for key in key2val:
		key2val[key] = key2val[key].replace('[', '').replace(']', '')

	return key2val

if __name__ == '__main__':
	print(q28())
