"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

import sys

N = int(sys.argv[3])
fs = [open(sys.argv[2] + str(i), 'w') for i in range(N)]
with open(sys.argv[1], 'r') as f:
	for i,line in enumerate(f):
		fs[i % N].write(line)
