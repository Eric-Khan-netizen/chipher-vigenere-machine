import vigenere as vig
import sys


if sys.argv[2] == '-f':
	text = vig.import_file(sys.argv[3])
	key = sys.argv[5]
	print('Файл {0} получен'.format(sys.argv[3]))
else:
	text = sys.argv[2]
	key = sys.argv[3]

if sys.argv[1] == '-e':
	final_text = vig.enchipher(text, key)
	print('Текст зашифрован')
elif sys.argv[1] == '-d':
	final_text = vig.dechipher(text, key)
	print('Текст расшифрован')

if sys.argv[2] == '-f':
	vig.write_file(sys.argv[4], final_text)
	vig.write_file(sys.argv[4], final_text)
	print('Результат записан в файл {}'.format(sys.argv[4]))
else:
	print(final_text)
