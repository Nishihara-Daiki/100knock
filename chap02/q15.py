"""
	15. 末尾のN行を出力
	自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

import sys

lines = []
N = int(sys.argv[1])

for line in sys.stdin:
	if len(lines) >= N:
		lines = lines[1:]
	lines.append(line.rstrip())

for line in lines:
	print(line)
