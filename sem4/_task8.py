# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def remove_s_at_the_end_of_word(*words):
    '''
    Удаляет s в конце слов, заменяя исходное слово с s на None (исключая одиночную s)
    '''
    word = list(words)
    for i in range(len(word)):
        if word[i].endswith('s') and word[i] != 's':
            word.append(word[i][:-1])
            word[i] = None
    return word


print(remove_s_at_the_end_of_word('numbers', 'string', 's', 'arrays', 'function'))
