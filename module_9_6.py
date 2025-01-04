def all_variants(text):
    for i in range(len(text)):
        first = 0
        last = i # от 0 до 2
        while last < len(text):
            yield text[first:last+1]
            first, last = first+1, last+1

my_text = all_variants('abc')
for i in my_text:
    print (i)

