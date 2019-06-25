#!/usr/bin/python
# -*- coding:utf-8 -*-

import queue

def isInbound(coord, h, n, m):
	if coord[0] >= 0 and coord[0] < h \
			and coord[1] >= 0 and coord[1] < n \
			and coord[2] >= 0 and coord[2] < m:
		return True
	else:
		return False

def solution():
	with open('input.txt', 'r') as f:
		lines = f.readlines()

	arg = lines[0].split()
	m = int(arg[0])
	n = int(arg[1])
	h = int(arg[2])
	
	box = list()
	tmp_box = list()
	n_cnt = 0

	for line in lines[1:]:
		n_cnt += 1
		arr = map(int, line.split())
		tmp_box.append(arr)
		if n_cnt == n:
			box.append(tmp_box)
			n_cnt = 0
			tmp_box = list()

	q = queue.Queue()

	for i in range(h):
		for j in range(n):
			for k in range(m):
				if box[i][j][k] == 1:
					q.put([(i, j, k), 1])

	if q.qsize() == 0:
		print "-1"
		exit(1)
	last_cnt = 0

	while not q.empty():
		elem = q.get()
		x = elem[0][0]
		y = elem[0][1]
		z = elem[0][2]
		last_cnt = value = elem[1]

		if isInbound((x-1, y, z), h, n, m) == True and box[x-1][y][z] == 0:
			box[x-1][y][z] = value + 1
			q.put([(x-1, y, z), value + 1])

		if isInbound((x+1, y, z), h, n, m) == True and box[x+1][y][z] == 0:
			box[x+1][y][z] = value + 1
			q.put([(x+1, y, z), value + 1])

		if isInbound((x, y-1, z), h, n, m) == True and box[x][y-1][z] == 0:
			box[x][y-1][z] = value + 1
			q.put([(x, y-1, z), value + 1])

		if isInbound((x, y+1, z), h, n, m) == True and box[x][y+1][z] == 0:
			box[x][y+1][z] = value + 1
			q.put([(x, y+1, z), value + 1])

		if isInbound((x, y, z-1), h, n, m) == True and box[x][y][z-1] == 0:
			box[x][y][z-1] = value + 1
			q.put([(x, y, z-1), value + 1])

		if isInbound((x, y, z+1), h, n, m) == True and box[x][y][z+1] == 0:
			box[x][y][z+1] = value + 1
			q.put([(x, y, z+1), value + 1])

	print last_cnt - 1

def main():
	solution()

if __name__ == '__main__':
	main()
