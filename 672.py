def reverse_words(text):
    words = text.split(' ')
    reversed_list = []
    for word in words:
        reversed_list.append(word[::-1])
    return ' '.join(reversed_list)
line1 = input()
print(reverse_words(line1))
line2 = input()
print(reverse_words(line2))

