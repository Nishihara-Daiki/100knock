"""
	21. カテゴリ名を含む行を抽出
	記事中でカテゴリ名を宣言している行を抽出せよ．
"""

from q20 import q20

data = q20()

for line in data.split('\n'):
	line = line
	if 'Category' in line:
		print(line)
