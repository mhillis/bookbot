from stats import get_word_count
from stats import get_char_count
from stats import sort_char
import sys
def get_book_text(path_to_file):
	with open(path_to_file) as f:
		#do somthing with f (the file) here
		file_contents = f.read()
		return file_contents

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book = sys.argv[1] #getting path to the book from user
	text = get_book_text(book)
	wordCount = get_word_count(text)
	print("============ BOOKBOT ============")
	print("Analyzing book found at "+ sys.argv[1] + " ...")
	print("----------- Word Count ----------")
	print("Found " + str(len(wordCount)) + " total words")
	print("--------- Character Count -------")
	char_count = get_char_count(text)
	sorted_count = sort_char(char_count)
	for dict in sorted_count:
		if dict["char"].isalpha():
			print(str(dict["char"]) + ": " + str(dict["num"]))
main()
