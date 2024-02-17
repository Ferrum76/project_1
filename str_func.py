def string_to_upper (s:str):
    '''Этот метод конвертирует строку в строку, состоящую из заглавных букв'''
    return s.upper()


def title_symbol_to_upper(s):
    '''Метод делает заглавными первые буквы каждого слова в строке, поступившей на вход функции'''
    arr = s.split(" ")
    for i in range(len(arr)):
        arr[i] = arr[i][0].upper() + arr[i][1:]

    return " ".join(arr)
