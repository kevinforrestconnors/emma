# -*- coding: utf-8 -*-

import sys

corpus = "emma-modern-retelling.txt"

def correct_file_from_epub(file):

	num_parens_so_far = 0

	with open(file, 'r') as fi:

		new_lines = []

		for line in fi:

			new_line = line.split()

			for i, word in enumerate(new_line):

				if "â€“" in word:
					word = word.replace("â€“", "(") if num_parens_so_far % 2 == 0 else word.replace("â€“", ")")
					num_parens_so_far += 1

				if "â€™" in word or "â€˜" in word:
					word = word.replace("â€™", "'").replace("â€˜", "'")

				if "â€¦" in word:
					word = word.replace("â€¦", "…")

				new_line[i] = word
					
			new_lines.append(" ".join(new_line))

	with open("emma-modern-retelling-corrected.txt", 'w') as fo:
		for line in new_lines:
			fo.write(line+"\n")


correct_file_from_epub(corpus)