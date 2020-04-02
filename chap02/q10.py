"""
	10. 行数のカウント
	行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

import sys
length = len([line for line in sys.stdin])
print(length)
