class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        for i in args:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for k in self.file_names: # k - имя файла внутри списка
            with open(k, encoding='utf-8') as file:
                list_words_for_all_words = [] # список, в который вносятся значения для словаря (для ключа 'k')
                for str_ in file:
                    str_ = str_.lower()
                    p = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for elem in p:
                        if elem in str_:
                            str_ = str_.replace(elem, '')
                    str_ = str_.split()
                    list_words_for_all_words.append(str_) # список дополяется, если в текстовом файле больше 1й строки
                    all_words[k] = list_words_for_all_words
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            n = 0
            find_word = {}
            for i in words:
                n += 1
                if i == word:
                    find_word[name] = n
                    break
        return find_word

    def count(self, word):
        a = {}
        for name, words in self.get_all_words().items():
            dict_for_count = {}
            count_word = 0
            for i in words:
                if i == word:
                    count_word += 1
            dict_for_count[name] = count_word
        return dict_for_count

p = WordsFinder('module_7_3.txt')
print(p.get_all_words())
print(p.find(['новая', 'строка']))
print(p.count(['это', 'текст', 'text', 'text']))