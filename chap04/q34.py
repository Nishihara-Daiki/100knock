"""
	34. 「AのB」
	2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

from q30 import q30

data = q30()

for line in data:
	for token1,token2,token3 in zip(line[:-2], line[1:-1], line[2:]):
		if token1['pos'] == '名詞' and token2['surface'] == 'の' and token3['pos'] == '名詞':
			print(token1['surface'], token2['surface'], token3['surface'])
