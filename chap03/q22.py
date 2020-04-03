"""
	22. カテゴリ名の抽出
	記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

from q20 import q20
import re

data = q20()

category = re.compile(r'\[\[Category:([^\|]+).*\]\]')
for line in data.split('\n'):
	if 'Category' in line:
		print(category.match(line).group(1))
