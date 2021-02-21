#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	characters = []
	alphanum = []
	for char in text:
		characters.append(char)

	for letters in characters:
		if letters.isalnum() == True:
			alphanum.append(1)
		else:
			continue
	return (len(alphanum))




def get_word_length_histogram(text):
	return [0]

def format_histogram(histogram):
	ROW_CHAR = "*"

	return ""

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	return ""


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
