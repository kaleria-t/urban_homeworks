import time

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range (1, word_count+1):
        file.write(f'Какое-то слово № {i} \n')
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

import threading
thread1 = threading.Thread(target=write_words(10, 'example5.txt'))
thread1.start()
thread2 = threading.Thread(target=write_words(30, 'example6.txt'))
thread2.start()
thread3 = threading.Thread(target=write_words(200, 'example7.txt'))
thread3.start()
thread4 = threading.Thread(target=write_words(100, 'example8.txt'))
thread4.start()