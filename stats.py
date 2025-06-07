def get_word_count(book):
	return book.split()

def get_char_count(book):
	char_count = {}
	book = book.lower()
	for char in book:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count
def sort_char(char_count):
	def sort_on(dict):
		return dict["num"]

	list_of_dicts = []
	for char, num in char_count.items():
		new_dict = {"char": char, "num": num}
		list_of_dicts.append(new_dict)
	list_of_dicts.sort(reverse=True, key=sort_on)
	return list_of_dicts
