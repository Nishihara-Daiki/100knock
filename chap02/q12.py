"""
	12. 1列目をcol1.txtに，2列目をcol2.txtに保存
	各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

import sys

with open(sys.argv[1], 'w') as f1, open(sys.argv[2], 'w') as f2:
	for line in sys.stdin:
		line = line.rstrip().split('\t')
		f1.write(line[0] + '\n')
		f2.write(line[2] + '\n')
