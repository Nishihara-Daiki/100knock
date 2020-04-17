"""
61. 単語の類似度
“United States”と”U.S.”のコサイン類似度を計算せよ．
"""

import sys
from q60 import load_w2v

def main():
	model = load_w2v(sys.argv[1])
	similarity = model.similarity('United_States', 'U.S.')
	print(similarity)


if __name__ == '__main__':
	main()
