#!/usr/bin/python
# -*- coding:utf-8 -*-

def solution(a):
	total_cnt = 0
	stack_cnt = 0

	prev_char = ''

	for x in a:
		if x == "(":
			stack_cnt += 1
		else:
			if prev_char == "(" and x == ")":
				stack_cnt -= 1
				total_cnt += stack_cnt
			else:
				total_cnt += 1
				stack_cnt -= 1
		prev_char = x
	
	print total_cnt

				

def main():
	a = "()(((()())(())()))(())"
	#a = "(((()(()()))(())()))(()())"
	solution(a)

if __name__ == '__main__':
	main()
