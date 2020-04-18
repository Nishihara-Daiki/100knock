"""
	65. アナロジータスクでの正解率
	64の実行結果を用い，意味的アナロジー（semantic analogy）と
	文法的アナロジー（syntactic analogy）の正解率を測定せよ．
"""

import sys

def main():
	syntactic, semantic = list(), list()
	with open(sys.argv[1]) as f:
		isSyntactic = True
		for line in f:
			line = line.rstrip()
			if line[0] == ':':
				isSyntactic = 'gram' in line
				continue
			_, _, _, label, pred, _ = line.split()
			if isSyntactic:
				syntactic.append(label == pred)
			else:
				semantic.append(label == pred)

	print('semantic accuracy = {}'.format(sum(semantic) / len(semantic)))
	print('syntactic accuracy = {}'.format(sum(syntactic) / len(syntactic)))




if __name__ == '__main__':
	main()
