"""
	33. サ変名詞
	サ変接続の名詞をすべて抽出せよ．
"""

from q30 import q30

data = q30()

for line in data:
	for token in line:
		if token['pos1'] == 'サ変接続':
			print(token['surface'])
