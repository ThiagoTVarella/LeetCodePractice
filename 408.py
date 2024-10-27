def validWordAbbreviation(word: str, abbr: str) -> bool:
    # Consider two pointers, one for each string
    i, j = 0, 0

    # We will move the two pointers together and compare the characters

    # When the pointer for abbr hits a number, we keep going only with j to figure out what the number is
    # and then we check if the character of abbr after corresponts to word after that number

    while i < len(word) and j < len(abbr):
        if abbr[j].isalpha():
            if abbr[j] != word[i]:
                return False
            i += 1
            j += 1
        else:
            num = ''
            if abbr[j] == '0':
                return False
            while j < len(abbr):
                if abbr[j].isdigit():
                    num += abbr[j]
                    j += 1
                else:
                    break

            # print(num)
            i += int(num)
            # print(i,j)
            if i >= len(word):
                return False
        # print(i,j)

    return True