"""
	23. セクション構造
	記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
"""

from q20 import q20
import re

data = q20()

r = re.complile(r'(=+)([^=]*)=+')

for line in data.split('\n'):
	if len(line) > 0 and line[0] == '=':
		match = r.match(line)
		level = len(match.group(1)) - 1
		text = match.group(2)
		print('{}\t{}'.format(level, text))

