# def get_book_text(filepath):
#     with open(filepath) as f:
#         file_contents = f.read()
#         print(file_contents)  # Proper indentation
from stats import text_count,count_char,sort_on
import sys
def get_book_text(path):
    	with open(path) as f:
        	return f.read()

def main():
	try:
		book_path = f"{sys.argv[1]}"
		text = get_book_text(book_path)
		num_words = text_count(text)
		chars_dict = count_char(text)
		print('============ BOOKBOT ============')
		print(f'Analyzing book found at {book_path}')
		print('----------- Word Count ----------')
		print(f"Found {num_words} total words")
		print('--------- Character Count -------')
		char_list = list(chars_dict.items())
		for i,k in char_list:
			if i.isalpha():
				print(f"{i}: {k}")
		print('============= END ===============')
	except Exception as e:
		print('Usage: python3 main.py <path_to_book>' )
		sys.exit(1)

main()