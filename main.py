def get_book_text(path_to_file):
	with open(path_to_file) as f:
		#do somthing with f (the file) here
		file_contents = f.read()
		return file_contents
def get_word_count(book):
	return book.split()

def main():
	wordCount = get_word_count(get_book_text("./books/frankenstein.txt"))
	print(str(len(wordCount)) + " words found in the document")
main()
