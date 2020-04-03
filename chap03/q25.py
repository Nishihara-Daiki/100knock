"""
	25. テンプレートの抽出
	記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

from q20 import q20
import re


def q25():
	data = q20()

	texts = []
	flag = False
	for line in data.split('\n'):
		if '}}' == line:
			break
		if flag:
			texts.append(line)
		if '{{基礎情報' in line:
			flag = True

	r = re.compile(r'\|(.*) = (.*)')

	key2val = {}
	for line in '\n'.join(texts).replace('<br/>\n', '<br/>').split('\n'):
		match = r.match(line)
		key2val[match.group(1)] = match.group(2)
	return key2val

if __name__ == '__main__':
	print(q25())
