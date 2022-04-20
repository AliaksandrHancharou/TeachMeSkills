palindrome_tuple = ('дед', 'морковь', 'яблоко', 'пейзаж', 'потоп', 'топот', 'рябина', 'шалаш')

#   1
def palindrome_v1(words: tuple) -> tuple:
    if words == words[::-1]:
        return True
    else:
        return False
    
palindrome_filter = filter(palindrome_v1, palindrome_tuple)

print(list(palindrome_filter))

#   2
def palindrome_v2(words: tuple) -> tuple:
    return list(filter(lambda x: x == x[::-1], words))

print(palindrome_v2(palindrome_tuple))


#   №1
some_words = list(map(str, input().split()))
some_words[0], some_words[1] = some_words[1], some_words[0]
delimiter = '!'
print(f'!{some_words[0]} {delimiter} {some_words[1]}!')

#   №2
print('!{} ! {}!'.format(some_words[0], some_words[1]))

#   №3
print('!%s ! %s!' % (some_words[0], some_words[1]))