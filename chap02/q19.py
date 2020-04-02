"""
	19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
	各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""
import sys
from collections import Counter
for key,value in Counter(line.rstrip().split()[0] for line in sys.stdin).most_common():
	print(key)
