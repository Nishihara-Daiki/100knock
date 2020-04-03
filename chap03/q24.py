"""
	24. ファイル参照の抽出
	記事から参照されているメディアファイルをすべて抜き出せ．
"""

from q20 import q20
import re

data = q20()

r = re.compile(r'ファイル:([^\|]*)')

for line in data.split('\n'):
	ref = r.match(line)
	if ref:
		print(ref.group(1))
