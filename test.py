target_word = "active".split()

user_enter = "aaples".split()

dict_char_target = {
        "a" : 1,
        "e" : 2,
        ...
}


dict_char_user= {}

for char in dict_char_user.keys():
    if char in target_word:
        if user_enter.index(char) == target_word.index(char):
            # green
            ...
        else:
            if dict_char_target[char] > 0:

                # change color to yellow 
                dict_char_target[char] -= 1
            else:
                # black