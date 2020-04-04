"""
	35. 名詞の連接
	名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

from q30 import q30

data = q30()

for line in data:
	isreturned = False
	for token in line:
		if token["pos"] == '名詞':
			print(token["surface"], end='')
			isreturned = False
		elif not isreturned:
			print(' ', end='')
			isreturned = True
	print()