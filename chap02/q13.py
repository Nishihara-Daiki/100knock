"""
	13. col1.txtとcol2.txtをマージ
	12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""

import sys

with open(sys.argv[1], 'r') as f1, open(sys.argv[2], 'r') as f2, open(sys.argv[3], 'w') as f3:
	for line1, line2 in zip(f1, f2):
		line1 = line1.rstrip()
		line2 = line2.rstrip()
		f3.write('{}\t{}\n'.format(line1, line2))
