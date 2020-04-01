"""
	08. 暗号文
	与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
	+ 英小文字ならば(219 - 文字コード)の文字に置換
	+ その他の文字はそのまま出力
	この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

def cipher(s):
	def _cipher(c):
		n = ord(c)
		return chr(219 - n) if ord('a') <= n <= ord('z') else c
	return ''.join([_cipher(c) for c in s])


original = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
encoded = cipher(original)
decoded = cipher(encoded)

print('original sentence = ' + original)
print('encoded sentence  = ' + encoded)
print('decoded sentence  = ' + decoded)
