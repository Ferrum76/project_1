def string_to_upper (s:str):
    '''Этот метод конвертирует строку в строку, состоящую из заглавных букв'''
    return s.upper()


def title_symbol_to_upper(s):
    '''Метод делает заглавными первые буквы каждого слова в строке, поступившей на вход функции'''
    return ' '.join(word[0].upper() + word[1:] if word else '' for word in s.split())
