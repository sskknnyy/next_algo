#!/usr/bin/python
# -*- coding:utf-8 -*-

## 잘못된 솔루션...(시간 제한을 고려하지 않음)
#def solution(w, h, x, y, t):
#	a = True
#	b = True
#	for i in range(t):
#		if x == w or x == 0:
#			a = not a
#		if y == h or y == 0:
#			b = not b
#
#		if a == True:
#			x += 1
#		else:
#			x -= 1
#		if b == True:
#			y += 1
#		else:
#			y -= 1
#	print x, y


def solution(w, h, x, y, t):
	tmp_x = x + t
	tmp_y = y + t
		
	if (tmp_x // w) & 1 == 0:
		res_x = tmp_x % w
	else:
		res_x = w - (tmp_x % w)

	if (tmp_y // h) & 1 == 0:
		res_y = tmp_y % h
	else:
		res_y = h - (tmp_y % h)

	print res_x, res_y

def main():
	w = 6
	h = 4
	x = 4
	y = 1
	t = 8
	solution(w, h, x, y, t)

if __name__ == '__main__':
	main()
