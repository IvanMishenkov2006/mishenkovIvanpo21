def find_shortest_word(s):#заголовок функции
    words=s.split()#Разбиваю строку на слова
    shortest_word = words[0]#Предполагаю, что самое короткое слово - это 1 слово
    for word in words:
        if len(word)<len(shortest_word):
            shortest_word=word# Если будет найдено слово с меньше,значит обновляется переменная shortest_word
    return shortest_word
sentence=input("Введите строку:")
shortest_word=find_shortest_word(sentence)
print("Самое короткое слово в строке:",shortest_word)