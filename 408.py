def valid_abbr(word: str, abbr: str) -> bool:

    word_pointer = 0
    abbr_pointer = 0

    while abbr_pointer < len(abbr) and word_pointer < len(word):
        if abbr[abbr_pointer] != word[word_pointer]:
            if not abbr[abbr_pointer].isdigit() or abbr[abbr_pointer] == '0':
                return False
            num = 0
            while abbr[abbr_pointer].isdigit():
                num = 10*num + int(abbr[abbr_pointer])
                abbr_pointer += 1
            word_pointer += num
        else:
            abbr_pointer += 1
            word_pointer += 1

    if word_pointer > len(word):
        return False

    return True


print(valid_abbr('apple','a21e'))


    # # Define two pointers
    # word_pointer = 0
    # abbr_pointer = 0

    # # Run through pointers
    # while word_pointer < len(word):
    #     # Read relevant characters
    #     word_ch = word[word_pointer]
    #     abbr_ch = abbr[abbr_pointer]

    #     # Check if characters are equal
    #     if word_ch == abbr_ch:
    #         word_pointer += 1
    #         abbr_pointer += 1

    #     else:
    #         # If not number, end
    #         if not abbr_ch.isdigit():
    #             return False

    #         # Read number from string
    #         number = ''
    #         while abbr_ch.isdigit():
    #             number += abbr_ch
    #             abbr_pointer += 1
    #             # Read new character from abbreviation, otherwise break
    #             if abbr_pointer < len(abbr):
    #                 abbr_ch = abbr[abbr_pointer]
    #             else:
    #                 break
    #         # If number started with 0
    #         if number[0] == '0':
    #             return False
    #         # Add number to word pointer
    #         else:
    #             number = int(number)
    #             word_pointer += number
    # if word_pointer > len(word):
    #     return False

    # return True