"""
	17. １列目の文字列の異なり
	1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．
"""

import sys


for line in sorted({line.rstrip().split('\t')[0] for line in sys.stdin}):
	print(line)
