"""
	31. 動詞
	動詞の表層形をすべて抽出せよ．
"""

from q30 import q30

data = q30()

for line in data:
	for token in line:
		if token["pos"] == "動詞":
			print(token["surface"])
