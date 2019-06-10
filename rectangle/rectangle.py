#!/usr/bin/python
# -*- coding:utf-8 -*-

def solution():
	with open('INPUT.TXT', 'r') as f:
		lines = f.readlines()
	input_coord = list()
	for line in lines:
		arr = line.strip().split(' ')
		input_coord.append(arr)
	## 사각형이 서로 겹치거나 - a
	## 사각형의 선이 겹치거나 - b
	## 사각형의 점이 겹치거나 - c
	## 안겹치거나 - d
	out_file = open('OUTPUT.TXT', 'w')
	for e in input_coord:
		x1 = e[0]
		y1 = e[1]
		p1 = e[2]
		q1 = e[3]
		x2 = e[4]
		y2 = e[5]
		p2 = e[6]
		q2 = e[7]
		#print x1, y1, p1, q1, x2, y2, p2, q2
		if (x1 == p2 and (y1 == q2 or q1 == y2)) or (p1 == x2 and (y1 == q2 or q1 == y2)):
			out_file.write("c\n")
		elif x1 == p2 or x2 == p1 or y1 == q2 or y2 == q1:
			out_file.write("b\n")
		elif x1 < p2 or y1 > q2 or x2 > p1 or y2 > q1:
			out_file.write("a\n")
		else:
			out_file.write("d\n")
	out_file.close()


def main():
	solution()

if __name__ == '__main__':
	main()
