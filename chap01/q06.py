"""
	06. 集合
	“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
	XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

from q05 import getngram

x = 'paraparaparadise'
y = 'paragraph'
X = set(getngram(x, 2))
Y = set(getngram(y, 2))

print('X | Y = {}'.format(X | Y))
print('X & Y = {}'.format(X & Y))
print('X - Y = {}'.format(X - Y))
print('"se" in X = {}'.format(('s', 'e') in X))
print('"se" in Y = {}'.format(('s', 'e') in Y))
