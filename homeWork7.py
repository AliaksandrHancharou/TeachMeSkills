palindrome_tuple = ('дед', 'морковь', 'яблоко', 'пейзаж', 'потоп', 'топот', 'рябина', 'шалаш')

def palindrome(words: tuple) -> tuple:
    if words == words[::-1]:
        return True
    else:
        return False

palindrome_filter = filter(palindrome, palindrome_tuple)

print(list(palindrome_filter))