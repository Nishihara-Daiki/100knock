"""
	02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
	「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

s = ''
for a,b in zip('パトカー','タクシー'):
	s += a + b
print(s)
